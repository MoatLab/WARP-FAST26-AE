#!/bin/bash
dir=$(ls)
for d in dir
    do
        pushd .
        cd $d
        mkdir fdp fdp_share nofdp
        popd
        done

