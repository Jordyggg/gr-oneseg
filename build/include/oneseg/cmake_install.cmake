# Install script for directory: /home/jordy/gr-oneseg/include/oneseg

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/oneseg" TYPE FILE FILES
    "/home/jordy/gr-oneseg/include/oneseg/api.h"
    "/home/jordy/gr-oneseg/include/oneseg/ofdm_synchronization_1seg.h"
    "/home/jordy/gr-oneseg/include/oneseg/tmcc_decoder_1seg.h"
    "/home/jordy/gr-oneseg/include/oneseg/frequency_deinterleaver_1seg.h"
    "/home/jordy/gr-oneseg/include/oneseg/time_deinterleaver_1seg.h"
    "/home/jordy/gr-oneseg/include/oneseg/symbol_demapper_1seg.h"
    "/home/jordy/gr-oneseg/include/oneseg/bit_deinterleaver.h"
    "/home/jordy/gr-oneseg/include/oneseg/viterbi_decoder.h"
    "/home/jordy/gr-oneseg/include/oneseg/byte_deinterleaver.h"
    "/home/jordy/gr-oneseg/include/oneseg/energy_descrambler.h"
    "/home/jordy/gr-oneseg/include/oneseg/reed_solomon_dec_isdbt.h"
    )
endif()

