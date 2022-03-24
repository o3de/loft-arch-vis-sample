

set(gem_path ${CMAKE_CURRENT_LIST_DIR})
set(gem_json ${gem_path}/gem.json)
o3de_restricted_path(${gem_json} gem_restricted_path gem_parent_relative_path)

o3de_pal_dir(pal_dir ${CMAKE_CURRENT_LIST_DIR}/Platform/${PAL_PLATFORM_NAME} "${gem_restricted_path}" "${gem_path}" "${gem_parent_relative_path}")


# We are on a supported platform, so add the Loft target
# Note: We include the common files and the platform specific files which are set in Loft_files.cmake and
# in ${pal_dir}/loft_${PAL_PLATFORM_NAME_LOWERCASE}_files.cmake
ly_add_target(
    NAME LoftSample.Static STATIC
    NAMESPACE Gem
    FILES_CMAKE
        loft_files.cmake
        ${pal_dir}/loft_${PAL_PLATFORM_NAME_LOWERCASE}_files.cmake
    INCLUDE_DIRECTORIES
        PUBLIC
            Include
    BUILD_DEPENDENCIES
        PRIVATE
            AZ::AzGameFramework
            Gem::Atom_AtomBridge.Static
)

ly_add_target(
    NAME LoftSample ${PAL_TRAIT_MONOLITHIC_DRIVEN_MODULE_TYPE}
    NAMESPACE Gem
    FILES_CMAKE
        loft_shared_files.cmake
        ${pal_dir}/loft_shared_${PAL_PLATFORM_NAME_LOWERCASE}_files.cmake
    INCLUDE_DIRECTORIES
        PUBLIC
            Include
    BUILD_DEPENDENCIES
        PRIVATE
            Gem::LoftSample.Static
            AZ::AzCore
)

# if enabled, LoftSample is used by all kinds of applications
ly_create_alias(NAME LoftSample.Builders NAMESPACE Gem TARGETS Gem::LoftSample)
ly_create_alias(NAME LoftSample.Tools    NAMESPACE Gem TARGETS Gem::LoftSample)
ly_create_alias(NAME LoftSample.Clients  NAMESPACE Gem TARGETS Gem::LoftSample)
ly_create_alias(NAME LoftSample.Servers  NAMESPACE Gem TARGETS Gem::LoftSample)

################################################################################
# Gem dependencies
################################################################################

# Enable the enabled_gems for the Project:
ly_enable_gems(PROJECT_NAME LoftSample GEM_FILE enabled_gems.cmake)

# Add project to the list server projects to create the Loft.ServerLauncher
if(PAL_TRAIT_BUILD_SERVER_SUPPORTED)
    set_property(GLOBAL APPEND PROPERTY LY_LAUNCHER_SERVER_PROJECTS LoftSample)
endif()

