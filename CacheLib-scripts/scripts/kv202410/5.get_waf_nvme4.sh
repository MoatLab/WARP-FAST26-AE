#!/bin/bash
target_file="nvme4_waf_1min.txt"
output_dir="./"
#output_dir="/home/inho/git/CacheLib/inho-run-cachelib"
#mv_dir="/home/inho/git/CacheLib/inho-run-cachelib/fadu-full-noFDP"

while true
do
    date>>${output_dir}/${target_file}
    sudo nvme fdp stats -e 1 /dev/ng4n1 >> ${output_dir}/${target_file}
    sleep 60
done
