#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Receptor ISDBTb ONESEG
# Description: demodula la señal de IDSBT de un segmento
# Generated: Fri Apr  6 13:45:43 2018
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

from MER_OneSeg import MER_OneSeg  # grc-generated hier_block
from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from SYNC_DEM_OFDM_1SEG import SYNC_DEM_OFDM_1SEG  # grc-generated hier_block
from decoder_1seg import decoder_1seg  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import oneseg
import sip
import time


class Receptor_OneSeg(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Receptor ISDBTb ONESEG")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Receptor ISDBTb ONESEG")
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

        self.settings = Qt.QSettings("GNU Radio", "Receptor_OneSeg")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.mode = mode = 3
        self.total_carriers = total_carriers = 2**(10+mode)/8
        self.time = time = 1*2**(mode-1)
        self.samp_rate = samp_rate = 6.4e6*80/63/8
        self.rate = rate = 1
        self.guard = guard = 1/16.0
        self.data_carriers = data_carriers = 96*2**(mode-1)
        self.center_freq = center_freq = 575.143e6
        self.active_carriers = active_carriers = 108*2**(mode-1)
        self.DB = DB = 30

        ##################################################
        # Blocks
        ##################################################
        self.Tabber1 = Qt.QTabWidget()
        self.Tabber1_widget_0 = Qt.QWidget()
        self.Tabber1_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Tabber1_widget_0)
        self.Tabber1_grid_layout_0 = Qt.QGridLayout()
        self.Tabber1_layout_0.addLayout(self.Tabber1_grid_layout_0)
        self.Tabber1.addTab(self.Tabber1_widget_0, 'Parametres')
        self.top_grid_layout.addWidget(self.Tabber1, 0,0,1,2)
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
        self.Tabber1_grid_layout_0.addWidget(self._mode_tool_bar, 1,0,1,0)
        self._time_options = (0*2**(mode-1), 1*2**(mode-1), 2*2**(mode-1), 3*2**(mode-1), )
        self._time_labels = ('op1', 'op2', 'op3', 'op4', )
        self._time_tool_bar = Qt.QToolBar(self)
        self._time_tool_bar.addWidget(Qt.QLabel('Length time'+": "))
        self._time_combo_box = Qt.QComboBox()
        self._time_tool_bar.addWidget(self._time_combo_box)
        for label in self._time_labels: self._time_combo_box.addItem(label)
        self._time_callback = lambda i: Qt.QMetaObject.invokeMethod(self._time_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._time_options.index(i)))
        self._time_callback(self.time)
        self._time_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_time(self._time_options[i]))
        self.Tabber1_grid_layout_0.addWidget(self._time_tool_bar, 3,0,1,0)
        self._rate_options = (0, 1, 2, 3, )
        self._rate_labels = ('1/2', '2/3', '3/4', '5/6', )
        self._rate_group_box = Qt.QGroupBox('Viterbi Rate')
        self._rate_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._rate_button_group = variable_chooser_button_group()
        self._rate_group_box.setLayout(self._rate_box)
        for i, label in enumerate(self._rate_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._rate_box.addWidget(radio_button)
        	self._rate_button_group.addButton(radio_button, i)
        self._rate_callback = lambda i: Qt.QMetaObject.invokeMethod(self._rate_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._rate_options.index(i)))
        self._rate_callback(self.rate)
        self._rate_button_group.buttonClicked[int].connect(
        	lambda i: self.set_rate(self._rate_options[i]))
        self.Tabber1_grid_layout_0.addWidget(self._rate_group_box, 4,0,1,0)
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
        self.Tabber1_grid_layout_0.addWidget(self._guard_tool_bar, 2,0,1,0)
        self._center_freq_tool_bar = Qt.QToolBar(self)
        self._center_freq_tool_bar.addWidget(Qt.QLabel('Frecuency'+": "))
        self._center_freq_line_edit = Qt.QLineEdit(str(self.center_freq))
        self._center_freq_tool_bar.addWidget(self._center_freq_line_edit)
        self._center_freq_line_edit.returnPressed.connect(
        	lambda: self.set_center_freq(eng_notation.str_to_num(str(self._center_freq_line_edit.text().toAscii()))))
        self.Tabber1_grid_layout_0.addWidget(self._center_freq_tool_bar, 0,0,1,0)
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
        self.top_grid_layout.addWidget(self.Tabber, 0,2,1,2)
        self._DB_tool_bar = Qt.QToolBar(self)
        self._DB_tool_bar.addWidget(Qt.QLabel('Ganancia USRP (dB)'+": "))
        self._DB_line_edit = Qt.QLineEdit(str(self.DB))
        self._DB_tool_bar.addWidget(self._DB_line_edit)
        self._DB_line_edit.returnPressed.connect(
        	lambda: self.set_DB(eng_notation.str_to_num(str(self._DB_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._DB_tool_bar)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(('addr=192.168.10.2', "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(100e6/99)
        self.uhd_usrp_source_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_source_0.set_gain(DB, 0)
        self.uhd_usrp_source_0.set_antenna('TX/RX', 0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=176,
                decimation=175,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	2*(int(total_carriers*(1+guard))), #size
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
        self.qtgui_number_sink_0_1.set_update_time(0.1)
        self.qtgui_number_sink_0_1.set_title("SNR")
        
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
            self.qtgui_number_sink_0_1.set_max(i, 40)
            self.qtgui_number_sink_0_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_1.set_label(i, labels[i])
            self.qtgui_number_sink_0_1.set_unit(i, units[i])
            self.qtgui_number_sink_0_1.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_1.enable_autoscale(False)
        self._qtgui_number_sink_0_1_win = sip.wrapinstance(self.qtgui_number_sink_0_1.pyqwidget(), Qt.QWidget)
        self.Tabber_grid_layout_3.addWidget(self._qtgui_number_sink_0_1_win, 0,2,1,1)
        self.qtgui_number_sink_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_VERT,
            1
        )
        self.qtgui_number_sink_0_0_0.set_update_time(0.1)
        self.qtgui_number_sink_0_0_0.set_title("BER Reed Solomon")
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_0.set_min(i, -10)
            self.qtgui_number_sink_0_0_0.set_max(i, 0)
            self.qtgui_number_sink_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0.pyqwidget(), Qt.QWidget)
        self.Tabber_grid_layout_3.addWidget(self._qtgui_number_sink_0_0_0_win, 0,4,1,1)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_VERT,
            1
        )
        self.qtgui_number_sink_0_0.set_update_time(0.1)
        self.qtgui_number_sink_0_0.set_title("BER Viterbi")
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0.set_min(i, -20)
            self.qtgui_number_sink_0_0.set_max(i, 0)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.pyqwidget(), Qt.QWidget)
        self.Tabber_grid_layout_3.addWidget(self._qtgui_number_sink_0_0_win, 0,3,1,1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_VERT,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.1)
        self.qtgui_number_sink_0.set_title("Modulation Error Rate")
        
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
            self.qtgui_number_sink_0.set_max(i, 30)
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
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	samp_rate, #bw
        	'Spectrum', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['spectrum', '', '', '', '',
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
        self.Tabber_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0,0,0)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	96*2**(mode-1), #size
        	'Constellation', #name
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
        self.Tabber_grid_layout_1.addWidget(self._qtgui_const_sink_x_0_win, 0,0,0,0)
        self.oneseg_tmcc_decoder_1seg_0 = oneseg.tmcc_decoder_1seg(mode, True)
        self.oneseg_time_deinterleaver_1seg_0 = oneseg.time_deinterleaver_1seg(mode, time)
        self.oneseg_symbol_demapper_1seg_0 = oneseg.symbol_demapper_1seg(mode, 4)
        self.oneseg_ofdm_synchronization_1seg_0 = oneseg.ofdm_synchronization_1seg(mode, guard)
        self.oneseg_frequency_deinterleaver_1seg_0 = oneseg.frequency_deinterleaver_1seg(mode)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 500e3/2.0, 5e3, firdes.WIN_HAMMING, 6.76))
        self.decoder_1seg_0 = decoder_1seg(
            mod=4,
            mode=mode,
            rate=rate,
        )
        self.blocks_vector_to_stream_0_2 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 96*2**(mode-1))
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_char*1, 188)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/jordy/ones.ts', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.SYNC_DEM_OFDM_1SEG_1 = SYNC_DEM_OFDM_1SEG(
            carriers=total_carriers,
            guarda=guard,
        )
        self.MER_OneSeg_1 = MER_OneSeg(
            Portadoras_OneSeg=96*2**(mode-1),
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.MER_OneSeg_1, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.SYNC_DEM_OFDM_1SEG_1, 0), (self.oneseg_ofdm_synchronization_1seg_0, 0))    
        self.connect((self.SYNC_DEM_OFDM_1SEG_1, 1), (self.qtgui_number_sink_0_1, 0))    
        self.connect((self.SYNC_DEM_OFDM_1SEG_1, 2), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_vector_to_stream_0_2, 0), (self.qtgui_const_sink_x_0, 0))    
        self.connect((self.decoder_1seg_0, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.decoder_1seg_0, 2), (self.qtgui_number_sink_0_0, 0))    
        self.connect((self.decoder_1seg_0, 1), (self.qtgui_number_sink_0_0_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.SYNC_DEM_OFDM_1SEG_1, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.oneseg_frequency_deinterleaver_1seg_0, 0), (self.oneseg_time_deinterleaver_1seg_0, 0))    
        self.connect((self.oneseg_ofdm_synchronization_1seg_0, 0), (self.oneseg_tmcc_decoder_1seg_0, 0))    
        self.connect((self.oneseg_symbol_demapper_1seg_0, 0), (self.decoder_1seg_0, 0))    
        self.connect((self.oneseg_time_deinterleaver_1seg_0, 0), (self.MER_OneSeg_1, 0))    
        self.connect((self.oneseg_time_deinterleaver_1seg_0, 0), (self.blocks_vector_to_stream_0_2, 0))    
        self.connect((self.oneseg_time_deinterleaver_1seg_0, 0), (self.oneseg_symbol_demapper_1seg_0, 0))    
        self.connect((self.oneseg_tmcc_decoder_1seg_0, 0), (self.oneseg_frequency_deinterleaver_1seg_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.rational_resampler_xxx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Receptor_OneSeg")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_mode(self):
        return self.mode

    def set_mode(self, mode):
        self.mode = mode
        self._mode_callback(self.mode)
        self.set_total_carriers(2**(10+self.mode)/8)
        self.set_time(1*2**(self.mode-1))
        self.decoder_1seg_0.set_mode(self.mode)
        self.set_data_carriers(96*2**(self.mode-1))
        self.set_active_carriers(108*2**(self.mode-1))
        self.MER_OneSeg_1.set_Portadoras_OneSeg(96*2**(self.mode-1))

    def get_total_carriers(self):
        return self.total_carriers

    def set_total_carriers(self, total_carriers):
        self.total_carriers = total_carriers
        self.SYNC_DEM_OFDM_1SEG_1.set_carriers(self.total_carriers)

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time
        self._time_callback(self.time)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 500e3/2.0, 5e3, firdes.WIN_HAMMING, 6.76))

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate
        self._rate_callback(self.rate)
        self.decoder_1seg_0.set_rate(self.rate)

    def get_guard(self):
        return self.guard

    def set_guard(self, guard):
        self.guard = guard
        self._guard_callback(self.guard)
        self.SYNC_DEM_OFDM_1SEG_1.set_guarda(self.guard)

    def get_data_carriers(self):
        return self.data_carriers

    def set_data_carriers(self, data_carriers):
        self.data_carriers = data_carriers

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        Qt.QMetaObject.invokeMethod(self._center_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.center_freq)))
        self.uhd_usrp_source_0.set_center_freq(self.center_freq, 0)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)

    def get_active_carriers(self):
        return self.active_carriers

    def set_active_carriers(self, active_carriers):
        self.active_carriers = active_carriers

    def get_DB(self):
        return self.DB

    def set_DB(self, DB):
        self.DB = DB
        Qt.QMetaObject.invokeMethod(self._DB_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.DB)))
        self.uhd_usrp_source_0.set_gain(self.DB, 0)
        	


def main(top_block_cls=Receptor_OneSeg, options=None):
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
