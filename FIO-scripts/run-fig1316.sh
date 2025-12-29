#!/bin/bash


echo "Fig131516 Three-stream write(80/20 workload) (~3hrs)"
echo "Exp launched at :"
date


pushd .
cd 3stream/; sudo ./run_metascript_one.sh 
popd
