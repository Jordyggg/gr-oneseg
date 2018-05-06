# Install script for directory: /home/jordy/gr-oneseg/grc

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gnuradio/grc/blocks" TYPE FILE FILES
    "/home/jordy/gr-oneseg/grc/oneseg_ofdm_synchronization_1seg.xml"
    "/home/jordy/gr-oneseg/grc/oneseg_tmcc_decoder_1seg.xml"
    "/home/jordy/gr-oneseg/grc/oneseg_frequency_deinterleaver_1seg.xml"
    "/home/jordy/gr-oneseg/grc/oneseg_time_deinterleaver_1seg.xml"
    "/home/jordy/gr-oneseg/grc/oneseg_symbol_demapper_1seg.xml"
    "/home/jordy/gr-oneseg/grc/oneseg_bit_deinterleaver.xml"
    "/home/jordy/gr-oneseg/grc/oneseg_viterbi_decoder.xml"
    "/home/jordy/gr-oneseg/grc/oneseg_byte_deinterleaver.xml"
    "/home/jordy/gr-oneseg/grc/oneseg_energy_descrambler.xml"
    "/home/jordy/gr-oneseg/grc/oneseg_reed_solomon_dec_isdbt.xml"
    "/home/jordy/gr-oneseg/grc/oneseg_mer_one_seg.xml"
    )
endif()

