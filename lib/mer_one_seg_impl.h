/* -*- c++ -*- */
/* 
 * Copyright 2018 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_ONESEG_MER_ONE_SEG_IMPL_H
#define INCLUDED_ONESEG_MER_ONE_SEG_IMPL_H

#include <oneseg/mer_one_seg.h>
#include <oneseg/demapper.h>
#include <oneseg/mer.h>

namespace gr {
  namespace oneseg {

    class mer_one_seg_impl : public mer_one_seg
    {
     private:
      int d_nsamples, d_count;
      double d_alpha;
      demapper *d_demapper;
      mer *d_mer;
      int d_dim_constellation;
      // Message port name
      pmt::pmt_t d_mer_port;
 
     public:
     /*
      * The private constructor.
      *
      * Receives the symbol table and the averaging parameter alpha. 
      * The symbol table is used by the demapper.cc class. 
      * The parameter alpha is used by the mer.cc class to average MER. 
      */

      mer_one_seg_impl(const std::vector<gr_complex> &symbol_table, double alpha);
      ~mer_one_seg_impl();

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace oneseg
} // namespace gr

#endif /* INCLUDED_ONESEG_MER_ONE_SEG_IMPL_H */

