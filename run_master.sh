#!/bin/sh

export PYTHONPATH="$(realpath ./threedb/):$PYTHONPATH"

python ./threedb/threedb/main.py $@
