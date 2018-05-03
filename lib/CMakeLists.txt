# Copyright 2011,2012,2016 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})
list(APPEND oneseg_sources
    ofdm_synchronization_1seg_impl.cc
    tmcc_decoder_1seg_impl.cc
    frequency_deinterleaver_1seg_impl.cc
    time_deinterleaver_1seg_impl.cc
    symbol_demapper_1seg_impl.cc
    bit_deinterleaver_impl.cc
    viterbi_decoder_impl.cc
    byte_deinterleaver_impl.cc
    energy_descrambler_impl.cc
    d_viterbi.c
    d_metrics.c
    d_tab.c
    reed_solomon_dec_isdbt_impl.cc )

set(oneseg_sources "${oneseg_sources}" PARENT_SCOPE)
if(NOT oneseg_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT oneseg_sources)

add_library(gnuradio-oneseg SHARED ${oneseg_sources})
target_link_libraries(gnuradio-oneseg ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-oneseg PROPERTIES DEFINE_SYMBOL "gnuradio_oneseg_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-oneseg PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
include(GrMiscUtils)
GR_LIBRARY_FOO(gnuradio-oneseg RUNTIME_COMPONENT "oneseg_runtime" DEVEL_COMPONENT "oneseg_devel")

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})
list(APPEND test_oneseg_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_oneseg.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_oneseg.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_reed_solomon_dec_isdbt.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_energy_descrambler.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_byte_deinterleaver.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_viterbi_decoder.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_bit_deinterleaver.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_symbol_demapper_1seg.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_time_deinterleaver_1seg.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_frequency_deinterleaver_1seg.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_tmcc_decoder_1seg.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_ofdm_synchronization_1seg.cc
    )

add_executable(test-oneseg ${test_oneseg_sources})

target_link_libraries(
  test-oneseg
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-oneseg
)

GR_ADD_TEST(test_oneseg test-oneseg)

########################################################################
# Print summary
########################################################################
message(STATUS "Using install prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "Building for version: ${VERSION} / ${LIBVER}")

