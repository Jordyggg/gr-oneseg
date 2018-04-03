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

#ifndef INCLUDED_ONESEG_BYTE_DEINTERLEAVER_IMPL_H
#define INCLUDED_ONESEG_BYTE_DEINTERLEAVER_IMPL_H

#include <oneseg/byte_deinterleaver.h>

namespace gr {
  namespace oneseg {

    class byte_deinterleaver_impl : public byte_deinterleaver
    {
     private:
      static const int d_SYNC;
      static const int d_TSP_SIZE; 
      static const int d_I;
      static const int d_M;
      
      int d_noutput; 
      //TODO circular_buffers are superior to deques. 
      //We should eventually migrate to them. 
      std::vector< std::deque<unsigned char> * > d_shift;

     public:
      byte_deinterleaver_impl();
      ~byte_deinterleaver_impl();

      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      // Where all the action really happens
      int general_work(int noutput_items,
               gr_vector_int &ninput_items, 
		       gr_vector_const_void_star &input_items,
		       gr_vector_void_star &output_items);
    };

  } // namespace oneseg
} // namespace gr

#endif /* INCLUDED_ONESEG_BYTE_DEINTERLEAVER_IMPL_H */

