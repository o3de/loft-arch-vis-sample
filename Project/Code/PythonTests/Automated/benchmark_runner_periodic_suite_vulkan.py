"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""
import pytest
import ly_test_tools.launchers.platforms.base
from Automated.benchmark_runner_periodic_suite_common import LoftSampleFrameTimingTest_GatherBenchmarkMetrics_Common
from Automated.benchmark_runner_periodic_suite_common import LoftSampleFrameTimingTest_SendBenchmarkMetrics_Common
from Automated.benchmark_runner_periodic_suite_common import filebeat_service_running

@pytest.mark.parametrize('launcher_platform', ['windows'])
@pytest.mark.parametrize("project", ["LoftSample"])
@pytest.mark.usefixtures("clean_loftsample_gamelauncher_logs", "loftsample_gamelauncher_log_monitor")
class TestPerformanceBenchmarksPeriodicSuite:

    @pytest.mark.parametrize('rhi', ['-rhi=vulkan'])
    def test_LoftSampleFrameTimingTest_GatherBenchmarkMetrics_Vulkan(
            self, request, workspace, launcher_platform, rhi, loftsample_gamelauncher_log_monitor):
            LoftSampleFrameTimingTest_GatherBenchmarkMetrics_Common(self, request, workspace, rhi, loftsample_gamelauncher_log_monitor)


    @pytest.mark.skipif(not filebeat_service_running(), reason="filebeat service not running")
    def test_LoftSampleFrameTimingTest_SendBenchmarkMetrics_Vulkan(
            self, request, editor, workspace, project, launcher_platform, level):
        """
        Gathers the Vulkan benchmark metrics and uses filebeat to send the metrics data.
        """

        LoftSampleFrameTimingTest_SendBenchmarkMetrics_Common(
                    workspace, launcher_platform, rhi)

