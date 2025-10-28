#!/bin/bash
target_file="nvme2_bw_1min.txt"
output_dir="./"
#output_dir="/home/inho/git/CacheLib/inho-run-cachelib"
#mv_dir="/home/inho/git/CacheLib/inho-run-cachelib/samsung-full-noFDP"

#while true
#do
date>>${output_dir}/${target_file}
iostat -m 60 -d /dev/nvme2n1 >> ${output_dir}/${target_file}
#done
