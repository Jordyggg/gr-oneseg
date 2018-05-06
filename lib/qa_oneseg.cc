/*
 * Copyright 2012 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * GNU Radio is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * GNU Radio is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with GNU Radio; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

/*
 * This class gathers together all the test cases for the gr-filter
 * directory into a single test suite.  As you create new test cases,
 * add them here.
 */

#include "qa_oneseg.h"
#include "qa_ofdm_synchronization_1seg.h"
#include "qa_tmcc_decoder_1seg.h"
#include "qa_frequency_deinterleaver_1seg.h"
#include "qa_time_deinterleaver_1seg.h"
#include "qa_symbol_demapper_1seg.h"
#include "qa_bit_deinterleaver.h"
#include "qa_viterbi_decoder.h"
#include "qa_byte_deinterleaver.h"
#include "qa_energy_descrambler.h"
#include "qa_reed_solomon_dec_isdbt.h"
#include "qa_mer_one_seg.h"

CppUnit::TestSuite *
qa_oneseg::suite()
{
  CppUnit::TestSuite *s = new CppUnit::TestSuite("oneseg");
  s->addTest(gr::oneseg::qa_ofdm_synchronization_1seg::suite());
  s->addTest(gr::oneseg::qa_tmcc_decoder_1seg::suite());
  s->addTest(gr::oneseg::qa_frequency_deinterleaver_1seg::suite());
  s->addTest(gr::oneseg::qa_time_deinterleaver_1seg::suite());
  s->addTest(gr::oneseg::qa_symbol_demapper_1seg::suite());
  s->addTest(gr::oneseg::qa_bit_deinterleaver::suite());
  s->addTest(gr::oneseg::qa_viterbi_decoder::suite());
  s->addTest(gr::oneseg::qa_byte_deinterleaver::suite());
  s->addTest(gr::oneseg::qa_energy_descrambler::suite());
  s->addTest(gr::oneseg::qa_reed_solomon_dec_isdbt::suite());
  s->addTest(gr::oneseg::qa_mer_one_seg::suite());

  return s;
}
