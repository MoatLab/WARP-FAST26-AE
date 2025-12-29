#!/bin/bash
echo "Fig11 One-stream write (~2hrs)"
echo "Exp launched at :"
date

pushd . 
cd 1stream/; ./run_one.sh
popd


echo " Finished(Fig11) grab nvme0_waf_1sec.txt with rsync command for plotting."

