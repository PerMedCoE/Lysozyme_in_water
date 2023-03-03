#!/usr/bin/env bash

# Select Python 3.7.4
export COMPSS_PYTHON_VERSION=3
# Load COMPSs 3.1 (uses the COMPSS_PYTHON_VERSION)
module load COMPSs/3.1
# Load singularity to build your own containers
module load singularity/3.5.2
# Load permedcoe environment (provides "permedcoe" package)
module use /apps/modules/modulefiles/tools/COMPSs/libraries
module load permedcoe

# Submit application
pycompss job submit \
    --job_name=Lysozyme_in_water \
    --num_nodes=3 \
    --exec_time=20 \
    -t \
    --python_interpreter=python3 \
    app.py ../dataset_small \
           ../output \
           ../config
