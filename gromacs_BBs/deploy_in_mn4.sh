#!/usr/bin/env bash

main_folder=/apps/COMPSs/PerMedCoE

function install {
    version=$(python -c "import sys; version = sys.version_info; print('%d.%d' % (version[0], version[1]))")
    path="${main_folder}/python${version}/site-packages/"
    bin_path="${main_folder}/python${version}/bin/"
    ORIGINAL_PYTHONPATH=$PYTHONPATH
    export PYTHONPATH=${path}:$PYTHONPATH

    mkdir -p ${path}
    mkdir -p ${bin_path}

    for building_block in */ ; do
        [ -L "${d%/}" ] && continue
        if [[ "${building_block}" == "image/" ]];then
            # Ignore image folder
            continue
        fi
        cd ${building_block}

        echo "Installing ${building_block::-1}"
        ./install_sc.sh ${path}
        ./clean.sh

        mv ${path}/bin/* ${bin_path}/.
        rm -rf  ${path}/bin

        cd ..
    done
    export PYTHONPATH=${ORIGINAL_PYTHONPATH}
}


echo "Installing Building Blocks into MareNostrum 4..."

# For python 3.7
module purge
module load intel mkl python/3.7.4
module use /apps/modules/modulefiles/tools/COMPSs/libraries
module load permedcoe

install

# # For python 3.6
# module purge
# module load intel mkl python/3.8.2
# module use /apps/modules/modulefiles/tools/COMPSs/libraries
# module load permedcoe
#
# install

# # For python 3.10
# module purge
# module load intel mkl python/3.10.2
# module use /apps/modules/modulefiles/tools/COMPSs/libraries
# module load permedcoe
#
# install

