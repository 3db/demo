#!/bin/sh

export PYTHONPATH="$(realpath ./threedb/):$(realpath .):$PYTHONPATH"
echo $PYTHONPATH

python ./threedb/threedb/main.py $@
