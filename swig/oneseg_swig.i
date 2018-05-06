/* -*- c++ -*- */

#define ONESEG_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "oneseg_swig_doc.i"

%{
#include "oneseg/ofdm_synchronization_1seg.h"
#include "oneseg/tmcc_decoder_1seg.h"
#include "oneseg/frequency_deinterleaver_1seg.h"
#include "oneseg/time_deinterleaver_1seg.h"
#include "oneseg/symbol_demapper_1seg.h"
#include "oneseg/bit_deinterleaver.h"
#include "oneseg/viterbi_decoder.h"
#include "oneseg/byte_deinterleaver.h"
#include "oneseg/energy_descrambler.h"
#include "oneseg/reed_solomon_dec_isdbt.h"
#include "oneseg/mer_one_seg.h"
%}

%include "oneseg/ofdm_synchronization_1seg.h"
GR_SWIG_BLOCK_MAGIC2(oneseg, ofdm_synchronization_1seg);
%include "oneseg/tmcc_decoder_1seg.h"
GR_SWIG_BLOCK_MAGIC2(oneseg, tmcc_decoder_1seg);
%include "oneseg/frequency_deinterleaver_1seg.h"
GR_SWIG_BLOCK_MAGIC2(oneseg, frequency_deinterleaver_1seg);
%include "oneseg/time_deinterleaver_1seg.h"
GR_SWIG_BLOCK_MAGIC2(oneseg, time_deinterleaver_1seg);
%include "oneseg/symbol_demapper_1seg.h"
GR_SWIG_BLOCK_MAGIC2(oneseg, symbol_demapper_1seg);

%include "oneseg/bit_deinterleaver.h"
GR_SWIG_BLOCK_MAGIC2(oneseg, bit_deinterleaver);
%include "oneseg/viterbi_decoder.h"
GR_SWIG_BLOCK_MAGIC2(oneseg, viterbi_decoder);
%include "oneseg/byte_deinterleaver.h"
GR_SWIG_BLOCK_MAGIC2(oneseg, byte_deinterleaver);
%include "oneseg/energy_descrambler.h"
GR_SWIG_BLOCK_MAGIC2(oneseg, energy_descrambler);
%include "oneseg/reed_solomon_dec_isdbt.h"
GR_SWIG_BLOCK_MAGIC2(oneseg, reed_solomon_dec_isdbt);
%include "oneseg/mer_one_seg.h"
GR_SWIG_BLOCK_MAGIC2(oneseg, mer_one_seg);
