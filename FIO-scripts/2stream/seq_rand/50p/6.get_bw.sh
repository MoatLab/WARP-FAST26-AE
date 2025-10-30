#!/bin/bash
target_file="nvme0_bw_1sec.txt"
dev="/dev/nvme0n1"
#output_dir="/home/inho/git/CacheLib/inho-run-cachelib"
#mv_dir="/home/inho/git/CacheLib/inho-run-cachelib/samsung-full-noFDP"

#while true
#do
iostat -d ${dev} -m 1 >> ./${target_file}
#done
