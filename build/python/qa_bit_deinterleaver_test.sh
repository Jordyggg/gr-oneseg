#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/jordy/gr-oneseg/python
export PATH=/home/jordy/gr-oneseg/build/python:$PATH
export LD_LIBRARY_PATH=/home/jordy/gr-oneseg/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/jordy/gr-oneseg/build/swig:$PYTHONPATH
/usr/bin/python2 /home/jordy/gr-oneseg/python/qa_bit_deinterleaver.py 
