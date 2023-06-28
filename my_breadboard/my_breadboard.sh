#!/bin/sh
cd `dirname $0`
export PYTHONPATH `/home/felixreichenbach/my_breadboard`
echo $PYTHONPATH

# Be sure to use `exec` so that termination signals reach the python process,
# or handle forwarding termination signals manually
exec python3 -m my_breadboard.main $@