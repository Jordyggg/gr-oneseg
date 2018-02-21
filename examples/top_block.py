#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Feb 21 16:59:26 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sys


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self, carriers=1024, guarda=1/8.0):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.carriers = carriers
        self.guarda = guarda

        ##################################################
        # Variables
        ##################################################
        self.snr = snr = 10
        self.rho = rho = 10.0**(snr/10.0)/(10.0**(snr/10.0)+1)

        ##################################################
        # Blocks
        ##################################################
        self.single_pole_iir_filter_xx_0 = filter.single_pole_iir_filter_ff(0.01, 1)
        self.blocks_sub_xx_1 = blocks.sub_ff(1)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_sample_and_hold_xx_0_0 = blocks.sample_and_hold_ff()
        self.blocks_sample_and_hold_xx_0 = blocks.sample_and_hold_ff()
        self.blocks_peak_detector_xb_0_0 = blocks.peak_detector_fb(2, 0.25, 30, 0.0005)
        self.blocks_peak_detector_xb_0 = blocks.peak_detector_fb(0.2, 0.25, 30, 0.0005)
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((rho, ))
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_moving_average_xx_0_1 = blocks.moving_average_cc(int(guarda*carriers), 1, 4000)
        self.blocks_moving_average_xx_0_0_0 = blocks.moving_average_ff(int(guarda*(carriers)), 1.0/2.0, 4000)
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, carriers)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_1 = blocks.complex_to_mag(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_frequency_modulator_fc_0_0 = analog.frequency_modulator_fc(-1.0/(carriers))
        self.analog_dpll_bb_0_0 = analog.dpll_bb(int((carriers)*(1+guarda)), 0.01)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_dpll_bb_0_0, 0), (self.blocks_sample_and_hold_xx_0, 1))    
        self.connect((self.analog_frequency_modulator_fc_0_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_moving_average_xx_0_0_0, 0))    
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_sample_and_hold_xx_0, 0))    
        self.connect((self.blocks_complex_to_mag_1, 0), (self.blocks_divide_xx_0, 0))    
        self.connect((self.blocks_complex_to_mag_1, 0), (self.blocks_sub_xx_0, 0))    
        self.connect((self.blocks_complex_to_mag_1, 0), (self.blocks_sub_xx_1, 1))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))    
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_peak_detector_xb_0_0, 0))    
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_sample_and_hold_xx_0_0, 0))    
        self.connect((self.blocks_moving_average_xx_0_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_moving_average_xx_0_0_0, 0), (self.blocks_sub_xx_1, 0))    
        self.connect((self.blocks_moving_average_xx_0_1, 0), (self.blocks_complex_to_arg_0, 0))    
        self.connect((self.blocks_moving_average_xx_0_1, 0), (self.blocks_complex_to_mag_1, 0))    
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_moving_average_xx_0_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_sub_xx_0, 1))    
        self.connect((self.blocks_multiply_xx_0, 0), (self, 0))    
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self, 1))    
        self.connect((self.blocks_peak_detector_xb_0, 0), (self.analog_dpll_bb_0_0, 0))    
        self.connect((self.blocks_peak_detector_xb_0_0, 0), (self.blocks_sample_and_hold_xx_0_0, 1))    
        self.connect((self.blocks_sample_and_hold_xx_0, 0), (self.single_pole_iir_filter_xx_0, 0))    
        self.connect((self.blocks_sample_and_hold_xx_0_0, 0), (self.blocks_nlog10_ff_0_0, 0))    
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_peak_detector_xb_0, 0))    
        self.connect((self.blocks_sub_xx_0, 0), (self, 2))    
        self.connect((self.blocks_sub_xx_1, 0), (self.blocks_divide_xx_0, 1))    
        self.connect((self, 0), (self.blocks_complex_to_mag_squared_0_0, 0))    
        self.connect((self, 0), (self.blocks_delay_0_0, 0))    
        self.connect((self, 0), (self.blocks_multiply_conjugate_cc_0, 0))    
        self.connect((self, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.analog_frequency_modulator_fc_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_carriers(self):
        return self.carriers

    def set_carriers(self, carriers):
        self.carriers = carriers
        self.blocks_moving_average_xx_0_1.set_length_and_scale(int(self.guarda*self.carriers), 1)
        self.blocks_moving_average_xx_0_0_0.set_length_and_scale(int(self.guarda*(self.carriers)), 1.0/2.0)
        self.blocks_delay_0_0.set_dly(self.carriers)
        self.analog_frequency_modulator_fc_0_0.set_sensitivity(-1.0/(self.carriers))

    def get_guarda(self):
        return self.guarda

    def set_guarda(self, guarda):
        self.guarda = guarda
        self.blocks_moving_average_xx_0_1.set_length_and_scale(int(self.guarda*self.carriers), 1)
        self.blocks_moving_average_xx_0_0_0.set_length_and_scale(int(self.guarda*(self.carriers)), 1.0/2.0)

    def get_snr(self):
        return self.snr

    def set_snr(self, snr):
        self.snr = snr
        self.set_rho(10.0**(self.snr/10.0)/(10.0**(self.snr/10.0)+1))

    def get_rho(self):
        return self.rho

    def set_rho(self, rho):
        self.rho = rho
        self.blocks_multiply_const_vxx_0.set_k((self.rho, ))


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
