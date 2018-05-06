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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "mer_one_seg_impl.h"

namespace gr {
  namespace oneseg {

    mer_one_seg::sptr
    mer_one_seg::make(const std::vector<gr_complex> &symbol_table, double alpha)
    {
      return gnuradio::get_initial_sptr
        (new mer_one_seg_impl(symbol_table, alpha));
    }


    mer_one_seg_impl::mer_one_seg_impl(const std::vector<gr_complex> &symbol_table, double alpha)
      : gr::sync_block("mer_one_seg", io_signature::make(1, 1, sizeof(gr_complex)),
		      io_signature::make(1, 1, sizeof(float)))
    {

        d_nsamples =10000 ;//number of samples to send a message with MER value 
        d_count = 0;// sample's counter

	d_alpha = alpha;
      	d_mer_port = pmt::string_to_symbol("mer_msg");
      	message_port_register_out(d_mer_port);
      	d_dim_constellation = symbol_table.size();
      	d_demapper = new demapper(symbol_table);
        d_mer = new mer(d_alpha);
    }


    mer_one_seg_impl::~mer_one_seg_impl()
    {
    }

    int
    mer_one_seg_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
 	const gr_complex *in = (const gr_complex*)input_items[0];
      	float *mer_out = NULL;
        mer_out = (float *) output_items[0];
     	gr_complex iq_true;
	// cosntellation_value is the point of the constellation in decimal notation
      	int constellation_value=0;
      	double i,q,i_true,q_true;
	for(int j=0; j < noutput_items; j++) {
	      	iq_true = d_demapper->demap(in[j],constellation_value);
			mer_out[j]=d_mer->update_mer(in[j],iq_true);
			d_count ++;
			if(d_count > d_nsamples) {
				// Post a message with the latest MER value
				message_port_pub(d_mer_port, pmt::from_double(mer_out[j]));
				d_count =0;	
        	}
	}
        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace mer */
} /* namespace gr */

