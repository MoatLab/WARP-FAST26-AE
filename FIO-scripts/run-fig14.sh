#!/bin/bash
echo "Fig14 Three-stream write WARP_A2 (~4*3hrs)"
echo "Exp launched at :"
date

pushd .
cd WARP_A2/3stream/; ./run_metascript_all.sh 
popd


echo " Finished(Fig14) grab nvme0_waf_1sec.txt with rsync command for plotting."


