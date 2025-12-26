# WARP evaluation procedure and requirements

## Phase 1: infrastructure setup

- Hardware and environment: x86_64 server with Linux 6.2.14 or 6.5.6
- DRAM requirement: 500 GB DRAM
- Disk space: (??)

- VM preparation: clone the WARP repo with <command> and pull the image with <command>. Then, move into <director> and run <./run_fdp_RU256.sh> to start the qemu VM
- Then connect to VM using this ssh <ssh -P 180880 warp@localhost>
- This process will consume about 1 hour and most of the time will be spent pulling the image 
 
## Phase 2: experiment run 

- To generate Figure 11, run "./run_fdp_WARP4.sh". experiment will take 36 hours
- To generate Figure 13 and 16, run "./run_fdp_WARP_A.sh" in VM A. experiment will take 10 hours
- To generate Figure 15, run "./run_fdp_WARP_B.sh" in VM B. experiment will take (???) hours
- To generate Figure 14, run "./run_fdp_WARP_A2.sh". experiment will take 12 hours
- For Figure 17 and 18, run following four commands and each command will take 4 hours
- "./run_fdp_WARP256II10.sh"
- "./run_fdp_WARP256PI10.sh"
- "./run_fdp_WARP256II7.sh"
- "./run_fdp_WARP256P17.sh"






## Phase 3: Generate figures

- Once you have run all the experiments, go into the WARP repo directory that you cloned in the beginning and run <python3 -m notebook> and click on the jupyter notebook WARP-AE-FAST26-1.ipynb
- Start running all cells one by one
