#!/usr/bin/env bash

#########
#  MN4  #
#########
# # Select Python 3.7.4
# export COMPSS_PYTHON_VERSION=3
# # Load COMPSs 3.2 (uses the COMPSS_PYTHON_VERSION)
# module load COMPSs/3.2
# # Load singularity to build your own containers
# module load singularity/3.5.2
# # Load permedcoe environment (provides "permedcoe" package)
# module use /apps/modules/modulefiles/tools/COMPSs/libraries

#########
# Mahti #
#########
module use /projappl/project_2007898/PerMedCoE/modulefiles
module load COMPSs/3.0
module load permedcoe

export PERMEDCOE_IMAGES=$(pwd)/../../gromacs_BBs/image/

rm -rf ../output
mkdir -p ../output

# Submit application
enqueue_compss \
    --job_name=Lysozyme_in_water \
    --project_name=project_2007898 \
    --num_nodes=1 \
    --exec_time=20 \
    --graph \
    --tracing \
    --master_working_dir=. \
    --worker_working_dir=$(pwd) \
    --keep_workingdir \
    --python_interpreter=python3 \
    app_complete.py \
        ../dataset_4x \
        ../output \
        ../config
