#
# Copyright (c) Contributors to the Open 3D Engine Project.
# For complete copyright and license terms please see the LICENSE at the root of this distribution.
#
# SPDX-License-Identifier: Apache-2.0 OR MIT
#
#

################################################################################
# Automated Tests
################################################################################

if(NOT PAL_TRAIT_BUILD_TESTS_SUPPORTED OR NOT PAL_TRAIT_BUILD_HOST_TOOLS)
    return()
endif()

o3de_pal_dir(pal_dir ${CMAKE_CURRENT_LIST_DIR}/Platform/${PAL_PLATFORM_NAME} "${gem_restricted_path}" "${gem_path}" "${gem_parent_relative_path}")
include(${pal_dir}/PAL_${PAL_PLATFORM_NAME_LOWERCASE}.cmake)

if(PAL_TRAIT_LOFT_SAMPLE_PERF_DX12_TESTS_SUPPORTED)
    ly_add_pytest(
        NAME LoftSample::PeriodicPerformanceBenchmarks_DX12
        PATH ${CMAKE_CURRENT_LIST_DIR}/Automated/benchmark_runner_periodic_suite_dx12.py
        TEST_REQUIRES gpu
        TEST_SUITE main
        TEST_SERIAL
        TIMEOUT 1200
        RUNTIME_DEPENDENCIES
            AssetProcessor
            AssetProcessorBatch
            LoftSample.GameLauncher
            LoftSample.Assets
    )
endif()

if(PAL_TRAIT_LOFT_SAMPLE_PERF_VULKAN_TESTS_SUPPORTED)
    ly_add_pytest(
        NAME LoftSample::PeriodicPerformanceBenchmarks_Vulkan
        PATH ${CMAKE_CURRENT_LIST_DIR}/Automated/benchmark_runner_periodic_suite_vulkan.py
        TEST_REQUIRES gpu
        TEST_SUITE main
        TEST_SERIAL
        TIMEOUT 1200
        RUNTIME_DEPENDENCIES
            AssetProcessor
            AssetProcessorBatch
            LoftSample.GameLauncher
            LoftSample.Assets
    )
endif()

