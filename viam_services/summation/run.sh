#!/bin/sh
cd `dirname $0`

export PYTHONPATH="/Users/felix.reichenbach/Documents/GitHub/viam-playground/viam_services"

# Be sure to use `exec` so that termination signals reach the python process,
# or handle forwarding termination signals manually
#exec poetry run python -m src.main $@

exec python3 -m my_service.main $@
