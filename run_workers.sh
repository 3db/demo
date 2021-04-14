#!/bin/sh

export PYTHONPATH="$(realpath ./threedb/):$PYTHONPATH"
export PATH="$(realpath ./blender):$PATH"

NUM=$1
BLENDER_DATA=$2
PORT=$3

for i in $(seq $NUM); do
    blender --python-use-system-env -b -P ./threedb/threedb/client.py \
        -- $BLENDER_DATA --master-address "localhost:$PORT" &

done;
wait
