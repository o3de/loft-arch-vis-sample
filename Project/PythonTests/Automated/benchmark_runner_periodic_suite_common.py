"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""
import logging
import os
import subprocess
import psutil

import ly_test_tools.environment.process_utils as process_utils
import ly_test_tools.environment.file_system as file_system
import ly_test_tools.launchers.platforms.base
from ly_test_tools.benchmark.data_aggregator import BenchmarkDataAggregator

logger = logging.getLogger(__name__)

def filebeat_service_running():
    """
    Checks if the filebeat service is currently running on the OS.
    :return: True if filebeat service detected and running, False otherwise.
    """
    result = False
    try:
        filebeat_service = psutil.win_service_get('filebeat')
        filebeat_service_info = filebeat_service.as_dict()
        if filebeat_service_info['status'] == 'running':
            result = True
    except psutil.NoSuchProcess:
        return result

    return result


class LoftSampleException(Exception):
    """Custom Exception class for LoftSample tests."""
    pass


def LoftSampleFrameTimingTest_GatherBenchmarkMetrics_Common(
        self, request, workspace, rhi, loftsample_gamelauncher_log_monitor):
    benchmark_name = f'LoftSample_{rhi}'
    cmd = os.path.join(workspace.paths.build_directory(),
                        'LoftSample.GameLauncher.exe '
                        f'--project-path={workspace.paths.project()} '
                        f'--rhi {rhi} '
                        '--regset="/O3DE/Performance/FrameTimeRecording/Activate=true" '
                        '--regset="/O3DE/Performance/FrameTimeRecording/QuitOnComplete=false" '
                        f'--regset="/O3DE/Performance/FrameTimeRecording/ProfileName={benchmark_name}" '
                        '+loadlevel levels/archvis/loft/interior_03.spawnable')

    def teardown():
        process_utils.kill_processes_named(['AssetProcessor', 'LoftSample.GameLauncher'], ignore_extensions=True)
    request.addfinalizer(teardown)

    # delete any pre-existing data
    benchmark_data_folder = [os.path.join(
            workspace.paths.project(), "user", "Scripts", "PerformanceBenchmarks", benchmark_name)]
    file_system.delete(benchmark_data_folder, True, True)


    # Execute test.
    launcherPid = subprocess.Popen(cmd, stderr=subprocess.STDOUT, encoding='UTF-8', shell=True).pid
    try:
        expected_lines = ["(Script) - OutputProfileData complete"]
        loftsample_gamelauncher_log_monitor.monitor_log_for_lines(expected_lines, timeout=180)
    except ly_test_tools.log.log_monitor.LogMonitorException as e:
        raise LoftSampleException(f'Data capturing did not complete in time for RHI {rhi}, got error: {e}')

def LoftSampleFrameTimingTest_SendBenchmarkMetrics_Common(
        workspace, launcher_platform, rhi):
    """
    Gathers the benchmark metrics and uses filebeat to send the metrics data.
    """

    aggregator = BenchmarkDataAggregator(workspace, logger, 'periodic')
    aggregator.upload_metrics(f'{launcher_platform}_{rhi}')

