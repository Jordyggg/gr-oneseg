INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_ONESEG oneseg)

FIND_PATH(
    ONESEG_INCLUDE_DIRS
    NAMES oneseg/api.h
    HINTS $ENV{ONESEG_DIR}/include
        ${PC_ONESEG_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    ONESEG_LIBRARIES
    NAMES gnuradio-oneseg
    HINTS $ENV{ONESEG_DIR}/lib
        ${PC_ONESEG_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(ONESEG DEFAULT_MSG ONESEG_LIBRARIES ONESEG_INCLUDE_DIRS)
MARK_AS_ADVANCED(ONESEG_LIBRARIES ONESEG_INCLUDE_DIRS)

