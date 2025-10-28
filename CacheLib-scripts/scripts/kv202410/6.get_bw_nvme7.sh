#!/bin/bash
target_file="samsung_bw_1min.txt"
output_dir="./"
#output_dir="/home/inho/git/CacheLib/inho-run-cachelib"
#mv_dir="/home/inho/git/CacheLib/inho-run-cachelib/samsung-full-noFDP"

date>>${output_dir}/${target_file}
#iostat nvme7n1
iostat -d -m 1 /dev/nvme7n1 >> ${output_dir}/${target_file}
