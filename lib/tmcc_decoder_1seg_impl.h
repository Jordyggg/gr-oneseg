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

#ifndef INCLUDED_ONESEG_TMCC_DECODER_1SEG_IMPL_H
#define INCLUDED_ONESEG_TMCC_DECODER_1SEG_IMPL_H

#include <oneseg/tmcc_decoder_1seg.h>
#include <stdio.h>

namespace gr {
    namespace oneseg {

        class tmcc_decoder_1seg_impl : public tmcc_decoder_1seg
        {
            private:
                /*TYPE DEFINITION*/
                /*These types are used while decoding the TMCC carrier*/
                typedef enum _modulation_scheme{QPSK = 1, QAM16, QAM64, M_UNUSED=7 } modulation_scheme_t;
                typedef enum _convolutional_code{RATE_1_2, RATE_2_3, RATE_3_4, RATE_5_6, RATE_7_8, C_UNUSED=7 } convolutional_code_t;
                typedef enum _interleaving_length{I_0_0_0, I_4_2_1, I_8_4_2, I_16_8_4, I_UNUSED=7} interleaving_length_t;
                typedef enum _number_segments{SEG_1=1, SEG_2, SEG_3, SEG_4, SEG_5, SEG_6, SEG_7, SEG_8, SEG_9, SEG_10, SEG_11, SEG_12, SEG_13, S_UNUSED=15 } number_segments_t;

                /*ATTRIBUTES*/

                static const int tmcc_carriers_size_2k;
                static const int tmcc_carriers_2k[];
                static const int tmcc_carriers_size_4k;
                static const int tmcc_carriers_4k[];
                static const int tmcc_carriers_size_8k;
                static const int tmcc_carriers_8k[];

                int tmcc_carriers_size;
                const int * tmcc_carriers;

                static const int d_ac_carriers_2k[];
                static const int ac_carriers_size_2k;
                static const int d_ac_carriers_4k[];
                static const int ac_carriers_size_4k;
                static const int d_ac_carriers_8k[];
                static const int ac_carriers_size_8k;

                int ac_carriers_size;
                const int * d_ac_carriers;

                static const int d_data_carriers_per_segment_2k;
                static const int d_data_carriers_per_segment_4k;
                static const int d_data_carriers_per_segment_8k;
                static const int d_carriers_per_segment_2k;

                // Number of data carriers per segment
                int d_data_carriers_per_segment;

                static const int sp_per_segment_2k;
                static const int sp_per_segment_4k;
                static const int sp_per_segment_8k;

                int sp_per_segment;

                // Number of active carriers
                int d_active_carriers;

                //the total data carriers
                int d_total_data_carriers;

                // Number of symbols per frame
                static const int d_symbols_per_frame;

                // Number of carriers per segment
                int d_carriers_per_segment;

                static const int d_tmcc_sync_size;

                // Keeps the rcv TMCC data, is a FIFO
                // TODO circular_buffers are superior to deques. 
                // We should migrate them all. 
                std::deque<char> d_rcv_tmcc_data;
                // Keeps the TMCC sync sequence
                std::deque<char> d_tmcc_sync_evenv;
                std::deque<char> d_tmcc_sync_oddv;

                static const int d_tmcc_sync_even[];
                static const int d_tmcc_sync_odd[];

                // TMCC parity check matrix
                static const char d_h[];

                // whether or not the decoded TMCC parameters should be printed. 
                bool d_print_params; 

                // Keep TMCC carriers values from previous symbol
                gr_complex * d_prev_tmcc_symbol;

                // See if the symbol index is known
                int d_symbol_index_known;

                // indicates whether the last symbol was a frame end
                bool d_frame_end;
                // indicates whther a re-sync should signaled downstream
                bool d_resync;

                // Symbol Index
                int d_symbol_index;

                int number_symbol;

                // how many symbols ago we saw a complete tmcc
                int d_since_last_tmcc;

                // a list of the data carriers for the current configuration (mode), one 
                // list per symbol. 
                int * d_data_carriers; 


                /*METHODS*/

                /*!
                 * This method checks whether or not the BCH code in d_rcv_tmcc_data is correct. 
                 */
                int tmcc_parity_check();

                void print_modulation_scheme(modulation_scheme_t modulation_scheme);
                void print_convolutional_code(convolutional_code_t convolutional_code);
                void print_interleaving_length(interleaving_length_t interleaving_length);
                void print_number_segments(number_segments_t number_segments);

                /*! 
                 * Prints the decoded TMCC in d_rcv_tmcc_data in a somewhat nice and human-readable format. 
                 */
                int tmcc_print();

                /*!
                 * \brief The method decodes the TMCC carriers of a given symbol, thus appending a new bit 
                 * to those received so far. If 203 were received since the last complete tmcc, we check whether 
                 * the sync word if present at the beginning, and if it passes the BCH parity code. 
                 *
                 * Our present implementation simply performs the differential demodulation (TMCC is transmitted in 
                 * DBPSK) for every carrier, and then performs a majority vote between all carriers to verify which
                 * bit was sent. 
                 */
                int process_tmcc_data(const gr_complex * in);

                /*!
                 * Sets several parameters used throughout the rest of the methods
                 */
                void set_carriers_parameters(int payload);

                /*!
                 *  it constructs the d_data_carriers list, which contains the list of carriers that have actual DTV data. 
                 */
                void construct_data_carriers_list();

            public:
                tmcc_decoder_1seg_impl(int mode, bool print_params);
                ~tmcc_decoder_1seg_impl();

                // Where all the action really happens
                int work(int noutput_items,
                        gr_vector_const_void_star &input_items,
                        gr_vector_void_star &output_items);
        };

    } // namespace oneseg
} // namespace gr

#endif /* INCLUDED_ONESEG_TMCC_DECODER_1SEG_IMPL_H */

