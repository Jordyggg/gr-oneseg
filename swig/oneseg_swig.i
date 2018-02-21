/* -*- c++ -*- */

#define ONESEG_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "oneseg_swig_doc.i"

%{
#include "oneseg/ofdm_synchronization_1seg.h"
%}

%include "oneseg/ofdm_synchronization_1seg.h"
GR_SWIG_BLOCK_MAGIC2(oneseg, ofdm_synchronization_1seg);
