# Demo threedb

This demo assumes linux operating system and bash shell. Adapt commands if you have something different.

## Setup

- Make sure you clone this repo with the `--recursive` flag to clone the `threedb` library too
- Download the resources required to run this demo `sh ./download_resources.sh`
- Create a new conda environment: `conda create -n threedb python=3.7.7`. **Important** The version of python has to match the one of blender. If you follow this tutorial blender bundles python 3.7.7.
- Activate the newly created environment `conda activate threedb`
- Install the dependencies `pip install -r ./threedb/requirements.txt`
- Download and unpack blender: `sh ./setup_blender.sh`. **Important**: Make sure your environment is activated before running this script.

## Running

To run an experiment you have to:

1. Start the master process: `./run_master.sh $RESOURCE_FOLDER $CONFIG_FILE $RESULT_FOLDER $PORT`
1. Start the worker process: `./run_workers.sh $NUM_WORKERS ./experiments/simple_envs 5555 `

## Experiments

In this repository we demonstrate `threedb` features through multiple experiments

### Render with HDRI background

In this experiment, we show how to render the same object in various environment modeled by 360deg HDRI backgrounds. We demonstrate a single control: the position of the camera relative to the object.

- `./run_master.sh experiments/simple_hdris/ experiments/simple_hdris/config.yaml /tmp/simple_hdris 5555`
- `./run_workers.sh 1 ./experiments/simple_hdirs 5555`

### Render with arbitrary Blender scene

In this experiment we show how to render objects in arbitrary scenes (described by a `.blend` file).

- `./run_master.sh experiments/simple_hdris/ experiments/simple_envs/config.yaml /tmp/simple_envs 5555`
- `./run_workers.sh 1 ./experiments/simple_envs 5555`

