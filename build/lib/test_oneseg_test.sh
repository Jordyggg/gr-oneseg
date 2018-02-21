#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/jordy/gr-oneseg/lib
export PATH=/home/jordy/gr-oneseg/build/lib:$PATH
export LD_LIBRARY_PATH=/home/jordy/gr-oneseg/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-oneseg 
