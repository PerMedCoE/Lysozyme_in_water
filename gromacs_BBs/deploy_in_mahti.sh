#!/usr/bin/env bash

main_folder=/projappl/project_2007898/PerMedCoE

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


echo "Installing Building Blocks into Mahti..."

module load COMPSs/3.0
module use /projappl/project_2007898/PerMedCoE/modulefiles
module load permedcoe

install
