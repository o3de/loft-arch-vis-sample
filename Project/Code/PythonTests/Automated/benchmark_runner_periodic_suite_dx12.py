"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""
import logging
import os
import subprocess
import psutil

import pytest

import ly_test_tools.environment.process_utils as process_utils
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


@pytest.mark.parametrize('launcher_platform', ['windows'])
@pytest.mark.parametrize("project", ["LoftSample"])
@pytest.mark.usefixtures("clean_loftsample_gamelauncher_logs", "loftsample_gamelauncher_log_monitor")
class TestPerformanceBenchmarksPeriodicSuite:

    @pytest.mark.parametrize('rhi', ['-rhi=dx12'])
    def test_LoftSampleFrameTimingTest_GatherBenchmarkMetrics_DX12(
            self, request, workspace, launcher_platform, rhi, loftsample_gamelauncher_log_monitor):
        cmd = os.path.join(workspace.paths.build_directory(),
                           'LoftSample.GameLauncher.exe '
                           f'--project-path={workspace.paths.project()} '
                           '--rhi dx12 ',
                           '--regset="/O3DE/Performance/FrameTimeRecording/Activate=true"',
                           '--regset="/O3DE/Performance/FrameTimeRecording/QuitOnComplete=true"',
                           '--regset="/O3DE/Performance/FrameTimeRecording/ProfileName=LoftSampleFrameTime_dx12"',
                           '+loadlevel levels\archvis\loft\interior_03.spawnable')

        def teardown():
            process_utils.kill_processes_named(['AssetProcessor', 'LoftSample.GameLauncher'], ignore_extensions=True)
        request.addfinalizer(teardown)

        # Execute test.
        process_utils.safe_check_call(cmd, stderr=subprocess.STDOUT, encoding='UTF-8', shell=True)
        try:
            expected_lines = ["Script: OutputProfileData complete"]
            loftsample_gamelauncher_log_monitor.monitor_log_for_lines(expected_lines, timeout=180)
        except ly_test_tools.log.log_monitor.LogMonitorException as e:
            raise LoftSampleException(f'Data capturing did not complete in time for RHI {rhi}, got error: {e}')

    @pytest.mark.skipif(not filebeat_service_running(), reason="filebeat service not running")
    def test_LoftSampleFrameTimingTest_SendBenchmarkMetrics_DX12(
            self, request, editor, workspace, project, launcher_platform, level):
        """
        Gathers the DX12 benchmark metrics and uses filebeat to send the metrics data.
        """

        aggregator = BenchmarkDataAggregator(workspace, logger, 'periodic')
        aggregator.upload_metrics('dx12')

