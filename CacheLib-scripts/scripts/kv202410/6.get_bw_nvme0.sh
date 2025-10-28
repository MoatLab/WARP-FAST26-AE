#!/bin/bash
target_file="nvme0_bw_1min.txt"
output_dir="./"
#output_dir="/home/inho/git/CacheLib/inho-run-cachelib"
#mv_dir="/home/inho/git/CacheLib/inho-run-cachelib/samsung-full-noFDP"

date>>${output_dir}/${target_file}
iostat -d nvme0n1 -h -m 60 >> ${output_dir}/${target_file}
