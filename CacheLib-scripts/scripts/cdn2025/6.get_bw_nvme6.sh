#!/bin/bash
target_file="nvme6_bw_1min.txt"
output_dir="./"
#output_dir="/home/inho/git/CacheLib/inho-run-cachelib"
#mv_dir="/home/inho/git/CacheLib/inho-run-cachelib/samsung-full-noFDP"

date>>${output_dir}/${target_file}
iostat nvme6n1
iostat -d nvme6n1 -m 60 -h >> ${output_dir}/${target_file}
