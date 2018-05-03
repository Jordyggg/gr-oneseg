#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Receptor_FullSeg
# Description: recieves isdbtb full seg signal
# Generated: Wed May  2 15:40:59 2018
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from MER_FULL_SEG import MER_FULL_SEG  # grc-generated hier_block
from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from SYNC import SYNC  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import isdbt
import numpy as np
import sip


class Jordy_ggg_fullseg(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Receptor_FullSeg")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Receptor_FullSeg")
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

        self.settings = Qt.QSettings("GNU Radio", "Jordy_ggg_fullseg")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.mode = mode = 3
        self.total_carriers = total_carriers = 2**(10+mode)
        self.samp_usrp = samp_usrp = 7.69231e6
        self.samp_rate = samp_rate = 8e6*64/63
        self.inter = inter = 1664
        self.guard = guard = 1/16.0
        self.decim = decim = 1575
        self.data_carriers = data_carriers = 13*96*2**(mode-1)
        self.center_freq = center_freq = 575.143e6
        self.active_carriers = active_carriers = 13*108*2**(mode-1)+1
        self.C = C = 0
        self.B = B = 12
        self.A = A = 1

        ##################################################
        # Blocks
        ##################################################
        self._mode_options = (3, 2, 1, )
        self._mode_labels = ('3 (8k)', '2 (4k)', '1 (2k)', )
        self._mode_tool_bar = Qt.QToolBar(self)
        self._mode_tool_bar.addWidget(Qt.QLabel('Mode'+": "))
        self._mode_combo_box = Qt.QComboBox()
        self._mode_tool_bar.addWidget(self._mode_combo_box)
        for label in self._mode_labels: self._mode_combo_box.addItem(label)
        self._mode_callback = lambda i: Qt.QMetaObject.invokeMethod(self._mode_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._mode_options.index(i)))
        self._mode_callback(self.mode)
        self._mode_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_mode(self._mode_options[i]))
        self.top_layout.addWidget(self._mode_tool_bar)
        self._guard_options = (1/4.0, 1/8.0, 1/16.0, 1/32.0, )
        self._guard_labels = ('1/4', '1/8', '1/16', '1/32', )
        self._guard_tool_bar = Qt.QToolBar(self)
        self._guard_tool_bar.addWidget(Qt.QLabel('Guard Interval'+": "))
        self._guard_combo_box = Qt.QComboBox()
        self._guard_tool_bar.addWidget(self._guard_combo_box)
        for label in self._guard_labels: self._guard_combo_box.addItem(label)
        self._guard_callback = lambda i: Qt.QMetaObject.invokeMethod(self._guard_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._guard_options.index(i)))
        self._guard_callback(self.guard)
        self._guard_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_guard(self._guard_options[i]))
        self.top_layout.addWidget(self._guard_tool_bar)
        self._center_freq_tool_bar = Qt.QToolBar(self)
        self._center_freq_tool_bar.addWidget(Qt.QLabel('Frecuency'+": "))
        self._center_freq_line_edit = Qt.QLineEdit(str(self.center_freq))
        self._center_freq_tool_bar.addWidget(self._center_freq_line_edit)
        self._center_freq_line_edit.returnPressed.connect(
        	lambda: self.set_center_freq(eng_notation.str_to_num(str(self._center_freq_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._center_freq_tool_bar)
        self.Tabber = Qt.QTabWidget()
        self.Tabber_widget_0 = Qt.QWidget()
        self.Tabber_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tabber_widget_0)
        self.Tabber_grid_layout_0 = Qt.QGridLayout()
        self.Tabber_layout_0.addLayout(self.Tabber_grid_layout_0)
        self.Tabber.addTab(self.Tabber_widget_0, 'Spectrum')
        self.Tabber_widget_1 = Qt.QWidget()
        self.Tabber_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tabber_widget_1)
        self.Tabber_grid_layout_1 = Qt.QGridLayout()
        self.Tabber_layout_1.addLayout(self.Tabber_grid_layout_1)
        self.Tabber.addTab(self.Tabber_widget_1, 'Constellation')
        self.Tabber_widget_2 = Qt.QWidget()
        self.Tabber_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tabber_widget_2)
        self.Tabber_grid_layout_2 = Qt.QGridLayout()
        self.Tabber_layout_2.addLayout(self.Tabber_grid_layout_2)
        self.Tabber.addTab(self.Tabber_widget_2, 'Van de Beek')
        self.Tabber_widget_3 = Qt.QWidget()
        self.Tabber_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tabber_widget_3)
        self.Tabber_grid_layout_3 = Qt.QGridLayout()
        self.Tabber_layout_3.addLayout(self.Tabber_grid_layout_3)
        self.Tabber.addTab(self.Tabber_widget_3, 'Measurements')
        self.top_grid_layout.addWidget(self.Tabber, 0,0,0,0)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	(int(total_carriers*(1+guard))), #size
        	samp_rate, #samp_rate
        	'ML OFDM Synchronization', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-0.02, 0.0015)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', '')
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.Tabber_grid_layout_2.addWidget(self._qtgui_time_sink_x_0_win, 0,1,1,1)
        self.qtgui_number_sink_0_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_VERT,
            1
        )
        self.qtgui_number_sink_0_1.set_update_time(0.10)
        self.qtgui_number_sink_0_1.set_title("Modulation Error Rate B")
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_1.set_min(i, 0)
            self.qtgui_number_sink_0_1.set_max(i, 50)
            self.qtgui_number_sink_0_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_1.set_label(i, labels[i])
            self.qtgui_number_sink_0_1.set_unit(i, units[i])
            self.qtgui_number_sink_0_1.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_1.enable_autoscale(False)
        self._qtgui_number_sink_0_1_win = sip.wrapinstance(self.qtgui_number_sink_0_1.pyqwidget(), Qt.QWidget)
        self.Tabber_grid_layout_3.addWidget(self._qtgui_number_sink_0_1_win, 1,1,1,1)
        self.qtgui_number_sink_0_0_1_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_VERT,
            1
        )
        self.qtgui_number_sink_0_0_1_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_1_0.set_title("BER Viterbi")
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_1_0.set_min(i, 0)
            self.qtgui_number_sink_0_0_1_0.set_max(i, 1)
            self.qtgui_number_sink_0_0_1_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_1_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_1_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_1_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_1_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_0_1_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_1_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_1_0.pyqwidget(), Qt.QWidget)
        self.Tabber_grid_layout_3.addWidget(self._qtgui_number_sink_0_0_1_0_win, 0,2,1,1)
        self.qtgui_number_sink_0_0_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_VERT,
            1
        )
        self.qtgui_number_sink_0_0_1.set_update_time(0.10)
        self.qtgui_number_sink_0_0_1.set_title("BER Viterbi")
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_1.set_min(i, 0)
            self.qtgui_number_sink_0_0_1.set_max(i, 1)
            self.qtgui_number_sink_0_0_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_1.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_1.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_1.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_0_1.enable_autoscale(False)
        self._qtgui_number_sink_0_0_1_win = sip.wrapinstance(self.qtgui_number_sink_0_0_1.pyqwidget(), Qt.QWidget)
        self.Tabber_grid_layout_3.addWidget(self._qtgui_number_sink_0_0_1_win, 1,2,1,1)
        self.qtgui_number_sink_0_0_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_VERT,
            1
        )
        self.qtgui_number_sink_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0_0_0.set_title("BER Reed Solomon")
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_0_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0_0_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0_0_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_0_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.Tabber_grid_layout_3.addWidget(self._qtgui_number_sink_0_0_0_0_0_win, 0,3,1,1)
        self.qtgui_number_sink_0_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_VERT,
            1
        )
        self.qtgui_number_sink_0_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0_0.set_title("BER Reed Solomon")
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.Tabber_grid_layout_3.addWidget(self._qtgui_number_sink_0_0_0_0_win, 1,3,1,1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_VERT,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("Modulation Error Rate A")
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, 0)
            self.qtgui_number_sink_0.set_max(i, 50)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.Tabber_grid_layout_3.addWidget(self._qtgui_number_sink_0_win, 0,1,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_RECTANGULAR, #wintype
        	center_freq, #fc
        	samp_rate, #bw
        	"Incoming spectrum", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(10, -140)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.Tabber_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,1)
        self.qtgui_const_sink_x_0_1_0 = qtgui.const_sink_c(
        	0*96*2**(mode-1), #size
        	'Constellation', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_1_0.enable_grid(False)
        self.qtgui_const_sink_x_0_1_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_0_1_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.Tabber_grid_layout_1.addWidget(self._qtgui_const_sink_x_0_1_0_win, 2,0,2,2)
        self.qtgui_const_sink_x_0_1 = qtgui.const_sink_c(
        	12*96*2**(mode-1), #size
        	'Constellation_Layer_B', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_1.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1.enable_autoscale(False)
        self.qtgui_const_sink_x_0_1.enable_grid(False)
        self.qtgui_const_sink_x_0_1.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_0_1.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_1_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.Tabber_grid_layout_1.addWidget(self._qtgui_const_sink_x_0_1_win, 0,2,1,1)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
        	data_carriers, #size
        	'Constellation_Layer_All', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_0_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.Tabber_grid_layout_1.addWidget(self._qtgui_const_sink_x_0_0_win, 2,2,1,1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1*96*2**(mode-1), #size
        	'Constellation_Layer_A', #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.Tabber_grid_layout_1.addWidget(self._qtgui_const_sink_x_0_win, 0,0,1,1)
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 6e6/2.0, 0.5e6, firdes.WIN_HAMMING, 6.76))
        self.isdbt_tmcc_decoder_0 = isdbt.tmcc_decoder(3, True)
        self.isdbt_time_deinterleaver_0 = isdbt.time_deinterleaver(3, 1, 4, 12, 2, 0, 0)
        self.isdbt_sync_and_channel_estimation_0 = isdbt.sync_and_channel_estimation(8192, 5617, 200)
        self.isdbt_symbol_demapper_0 = isdbt.symbol_demapper(3, 1, 4, 12, 64, 0, 64)
        self.isdbt_subset_of_carriers_0_0_0 = isdbt.subset_of_carriers(data_carriers, 0, 0)
        self.isdbt_subset_of_carriers_0_0 = isdbt.subset_of_carriers(data_carriers, 0, A*96*2**(mode-1)-1)
        self.isdbt_subset_of_carriers_0 = isdbt.subset_of_carriers(data_carriers, 384, 4991)
        self.isdbt_ofdm_sym_acquisition_0 = isdbt.ofdm_sym_acquisition(total_carriers, int(guard*total_carriers), 10)
        self.isdbt_frequency_deinterleaver_0 = isdbt.frequency_deinterleaver(True, 3)
        self.isdbt_channel_decoding_0_0 = isdbt.isdbt_channel_decoding(
            layer_segments=1,
            mode=3,
            constellation_size=4,
            rate=1,
        )
        self.isdbt_channel_decoding_0 = isdbt.isdbt_channel_decoding(
            layer_segments=12,
            mode=3,
            constellation_size=64,
            rate=2,
        )
        self.fft_vxx_0 = fft.fft_vcc(total_carriers, True, (window.rectangular(total_carriers)), True, 1)
        self.blocks_vector_to_stream_0_2_1_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, C*96*2**(mode-1)+1)
        self.blocks_vector_to_stream_0_2_1 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 4608)
        self.blocks_vector_to_stream_0_2_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, data_carriers)
        self.blocks_vector_to_stream_0_2 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, A*96*2**(mode-1))
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_to_vector_0_0_0 = blocks.stream_to_vector(gr.sizeof_char*1, 188)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_char*1, 188)
        self.blocks_null_sink_0_0_0_0 = blocks.null_sink(gr.sizeof_char*188)
        self.blocks_null_sink_0_0_0 = blocks.null_sink(gr.sizeof_char*188)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_char*384)
        self.blocks_file_source_1_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/jordy/Descargas/569MHz_recording/569MHz_recording.dat', True)
        self.SYNC_0 = SYNC(
            guarda=guard,
            mode=mode,
        )
        self.MER_FULL_SEG_0 = MER_FULL_SEG(
            Modulation_Scheme_A=(1+1j, 1-1j, -1+1j, -1-1j)/np.sqrt(2),
            Modulation_Scheme_B=(7+7j, 7+5j, 5+7j, 5+5j, 7+1j, 7+3j, 5+1j, 5+3j, 1+7j, 1+5j, 3+7j, 3+5j, 1+1j, 1+3j, 3+1j, 3+3j, 7-7j, 7-5j, 5-7j, 5-5j, 7-1j, 7-3j, 5-1j, 5-3j, 1-7j, 1-5j, 3-7j, 3-5j, 1-1j, 1-3j, 3-1j, 3-3j, -7+7j, -7+5j, -5+7j, -5+5j, -7+1j, -7+3j, -5+1j, -5+3j, -1+7j, -1+5j, -3+7j, -3+5j, -1+1j, -1+3j, -3+1j, -3+3j, -7-7j, -7-5j, -5-7j, -5-5j, -7-1j, -7-3j, -5-1j, -5-3j, -1-7j, -1-5j, -3-7j, -3-5j, -1-1j, -1-3j, -3-1j, -3-3j)/np.sqrt(42),
            Modulation_Scheme_C=(3+3j, 3+1j, 1+3j, 1+1j, 3-3j, 3-1j, 1-3j, 1-1j, -3+3j, -3+1j, -1+3j, -1+1j, -3-3j, -3-1j, -1-3j, -1-1j)/np.sqrt(10),
            alpha=0.05,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.MER_FULL_SEG_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.MER_FULL_SEG_0, 1), (self.qtgui_number_sink_0_1, 0))    
        self.connect((self.SYNC_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_file_source_1_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.blocks_null_sink_0_0_0, 0))    
        self.connect((self.blocks_stream_to_vector_0_0_0, 0), (self.blocks_null_sink_0_0_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.low_pass_filter_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.blocks_vector_to_stream_0_2, 0), (self.MER_FULL_SEG_0, 0))    
        self.connect((self.blocks_vector_to_stream_0_2, 0), (self.qtgui_const_sink_x_0, 0))    
        self.connect((self.blocks_vector_to_stream_0_2_0, 0), (self.qtgui_const_sink_x_0_0, 0))    
        self.connect((self.blocks_vector_to_stream_0_2_1, 0), (self.MER_FULL_SEG_0, 1))    
        self.connect((self.blocks_vector_to_stream_0_2_1, 0), (self.qtgui_const_sink_x_0_1, 0))    
        self.connect((self.blocks_vector_to_stream_0_2_1_0, 0), (self.MER_FULL_SEG_0, 2))    
        self.connect((self.blocks_vector_to_stream_0_2_1_0, 0), (self.qtgui_const_sink_x_0_1_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.isdbt_sync_and_channel_estimation_0, 0))    
        self.connect((self.isdbt_channel_decoding_0, 0), (self.blocks_stream_to_vector_0_0, 0))    
        self.connect((self.isdbt_channel_decoding_0, 1), (self.qtgui_number_sink_0_0_0_0, 0))    
        self.connect((self.isdbt_channel_decoding_0, 2), (self.qtgui_number_sink_0_0_1, 0))    
        self.connect((self.isdbt_channel_decoding_0_0, 0), (self.blocks_stream_to_vector_0_0_0, 0))    
        self.connect((self.isdbt_channel_decoding_0_0, 1), (self.qtgui_number_sink_0_0_0_0_0, 0))    
        self.connect((self.isdbt_channel_decoding_0_0, 2), (self.qtgui_number_sink_0_0_1_0, 0))    
        self.connect((self.isdbt_frequency_deinterleaver_0, 0), (self.isdbt_time_deinterleaver_0, 0))    
        self.connect((self.isdbt_ofdm_sym_acquisition_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.isdbt_subset_of_carriers_0, 0), (self.blocks_vector_to_stream_0_2_1, 0))    
        self.connect((self.isdbt_subset_of_carriers_0_0, 0), (self.blocks_vector_to_stream_0_2, 0))    
        self.connect((self.isdbt_subset_of_carriers_0_0_0, 0), (self.blocks_vector_to_stream_0_2_1_0, 0))    
        self.connect((self.isdbt_symbol_demapper_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.isdbt_symbol_demapper_0, 1), (self.isdbt_channel_decoding_0, 0))    
        self.connect((self.isdbt_symbol_demapper_0, 0), (self.isdbt_channel_decoding_0_0, 0))    
        self.connect((self.isdbt_sync_and_channel_estimation_0, 0), (self.isdbt_tmcc_decoder_0, 0))    
        self.connect((self.isdbt_time_deinterleaver_0, 0), (self.blocks_vector_to_stream_0_2_0, 0))    
        self.connect((self.isdbt_time_deinterleaver_0, 0), (self.isdbt_subset_of_carriers_0, 0))    
        self.connect((self.isdbt_time_deinterleaver_0, 0), (self.isdbt_subset_of_carriers_0_0, 0))    
        self.connect((self.isdbt_time_deinterleaver_0, 0), (self.isdbt_subset_of_carriers_0_0_0, 0))    
        self.connect((self.isdbt_time_deinterleaver_0, 0), (self.isdbt_symbol_demapper_0, 0))    
        self.connect((self.isdbt_tmcc_decoder_0, 0), (self.isdbt_frequency_deinterleaver_0, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.SYNC_0, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.isdbt_ofdm_sym_acquisition_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Jordy_ggg_fullseg")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_mode(self):
        return self.mode

    def set_mode(self, mode):
        self.mode = mode
        self.set_total_carriers(2**(10+self.mode))
        self._mode_callback(self.mode)
        self.set_data_carriers(13*96*2**(self.mode-1))
        self.set_active_carriers(13*108*2**(self.mode-1)+1)
        self.SYNC_0.set_mode(self.mode)

    def get_total_carriers(self):
        return self.total_carriers

    def set_total_carriers(self, total_carriers):
        self.total_carriers = total_carriers

    def get_samp_usrp(self):
        return self.samp_usrp

    def set_samp_usrp(self, samp_usrp):
        self.samp_usrp = samp_usrp

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 6e6/2.0, 0.5e6, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_inter(self):
        return self.inter

    def set_inter(self, inter):
        self.inter = inter

    def get_guard(self):
        return self.guard

    def set_guard(self, guard):
        self.guard = guard
        self._guard_callback(self.guard)
        self.SYNC_0.set_guarda(self.guard)

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim

    def get_data_carriers(self):
        return self.data_carriers

    def set_data_carriers(self, data_carriers):
        self.data_carriers = data_carriers

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        Qt.QMetaObject.invokeMethod(self._center_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.center_freq)))
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)

    def get_active_carriers(self):
        return self.active_carriers

    def set_active_carriers(self, active_carriers):
        self.active_carriers = active_carriers

    def get_C(self):
        return self.C

    def set_C(self, C):
        self.C = C

    def get_B(self):
        return self.B

    def set_B(self, B):
        self.B = B

    def get_A(self):
        return self.A

    def set_A(self, A):
        self.A = A


def main(top_block_cls=Jordy_ggg_fullseg, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

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
