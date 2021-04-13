#!/bin/sh

export PYTHONPATH="$(realpath ./threedb/):$PYTHONPATH"

python ./threedb/threedb/main.py $BLENDER_DATA $YAML_CONFIG $OUTPUT_FOLDER $@
