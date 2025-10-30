#!/bin/bash
target_file="nvme3_bw_1min.txt"
output_dir="./"
#output_dir="/home/inho/git/CacheLib/inho-run-cachelib"
#mv_dir="/home/inho/git/CacheLib/inho-run-cachelib/samsung-full-noFDP"

date>>${output_dir}/${target_file}
iostat -d nvme3n1 -m 60 -h  >> ${output_dir}/${target_file}
