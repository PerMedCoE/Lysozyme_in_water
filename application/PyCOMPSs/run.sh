#!/usr/bin/env bash

CURRENT_DIR=$(pwd)

export PERMEDCOE_IMAGES="${CURRENT_DIR}/../../gromacs_BBs/image/"

DATASET_PATH=${CURRENT_DIR}/../dataset_small
OUTPUT_PATH=${CURRENT_DIR}/../output
CONFIG_PATH=${CURRENT_DIR}/../config

# Explicit call with PyCOMPSs runcompss command:
runcompss -g --python_interpreter=python3 \
     app_complete.py \
     ${DATASET_PATH} \
     ${OUTPUT_PATH} \
     ${CONFIG_PATH}

