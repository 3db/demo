# Demo threedb

This demo assumes linux operating system and bash shell. Adapt commands if you have something different.

## Setup

- Follow the installation instructions for your operating system: https://github.com/3db/installers
- Activate your conda environment: `conda activate threedb` (if you use the default environment name, otherwise change accordingly)
- Clone this repository: `git clone https://github.com/3db/demo.git`
- `cd demo`
- Download the resources required to run this demo `sh ./download_resources.sh`

## Running

To run an experiment you have to:

1. Start the master process: `./run_master.sh $RESOURCE_FOLDER $CONFIG_FILE $RESULT_FOLDER $PORT`
1. Start the worker process: `./run_workers.sh $NUM_WORKERS ./experiments/simple_envs 5555 `
2. Explore the results on the dashboard: `python -m threedb.dashboard $RESULT_FOLDER`

## Experiments

In this repository we demonstrate `threedb` features through multiple experiments

### Render with HDRI background

In this experiment, we show how to render the same object in various environment modeled by 360deg HDRI backgrounds. We demonstrate a single control: the position of the camera relative to the object.

- `./run_master.sh experiments/simple_hdris/ experiments/simple_hdris/config.yaml /tmp/simple_hdris 5555`
- `./run_workers.sh 1 ./experiments/simple_hdris 5555`

### Render with arbitrary Blender scene

In this experiment we show how to render objects in arbitrary scenes (described by a `.blend` file).

- `./run_master.sh experiments/simple_envs/ experiments/simple_envs/config.yaml /tmp/simple_envs 5555`
- `./run_workers.sh 1 ./experiments/simple_envs 5555`

### Write a custom Pre-render Control

Being able to control the camera is nice but for most applications, users are intrested in domain specific parameters. In this experiment we show how to add a new control `SunControl` that is able to change the angle of the sun (i.e. the time of the day).

- `./run_master.sh experiments/demo_sun/ experiments/demo_sun/config.yaml /tmp/demo_sun 5555`
- `./run_workers.sh 1 ./experiments/demo_sun 5555`


### Write a custon Post-Render Control

In this experiment we demonstrate how to add a custom post processing step to the pipeline. We add a corruption control and render with it

- `./run_master.sh experiments/demo_corruptions/ experiments/demo_corruptions/config.yaml /tmp/demo_corruptions 5555`
- `./run_workers.sh 1 ./experiments/demo_corruptions/ 5555`
