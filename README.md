
# Experiment scripts for WARP
These are the scripts that I used for both FDP SSD and WARP(proj old name Cylon-FDP) testing.

Experiments are three-fold. FIO. CacheLib. and F2FS.

## FDP SSD setup (nvme cli)
```
sudo ./fdp_setup_nvme-cli.sh /dev/nvmeX
```

# 0.Dependency 
## libnvme
I'm using `nvme fdp ` command to get the write amplification results
to use, libnvme should be v1.5

```
wget https://github.com/linux-nvme/libnvme/archive/refs/tags/v1.5.tar.gz
```
tar -xvf v1.5.tar.gz, then

```
meson setup .build
```


## liburing 
version 2.3 >= works fine

Also works fine with
v2.3
v2.6
v2.7
v2.9
v2.10


## FIO
version 3.36


## Kernel
Using 6.2.14

Also tested with
v6.5.6
v6.10.x (especially F2FS, 6.10.x)

# 1. WARP evaluation procedure and requirements

## Phase 1: infrastructure setup

- Hardware and environment: x86_64 server with Linux 6.2.14 or 6.5.6 with KVM enabled.
- DRAM requirement: 500 GB DRAM
- VM preparation: clone the WARP repo with <command> and pull the image with <command>. Then, move into <director> and run <./run_fdp_RU256.sh> to start the qemu VM
- Then connect to VM using this ssh <ssh -P 180880 warp@localhost>
- This process will consume about 1 hour, and most of the time will be spent pulling the image.
 
## Phase 2: experiment run 
- Overview
   * Two steps for setup the env.This is the basic experiment setup for WARP.
       1. Launch the VM(script in `build-femu` dir)
       2. Launch the exp script(this repo) to run the experiments. 
   * Two file will be needed for figure plotting.
       1. `nvmeX_waf_1sec.txt` (or `samsung_waf_1sec.txt` by `5.get_waf.sh` script)
       2. `log` file. This located in outside of the VM, in `build-femu` directory.
    
In here, `sudo ./run_fdp_RU256.sh` (or `sudo nohup ./run_fdp_RU256.sh &`) to launch the VM. This is equivalent to WARP-A. Make sure your VM is using libnvme 1.5 and fio 3.36(`pkg-config --modversion libnvme` and `fio --version`). GC policy is greedy.
<img width="949" height="309" alt="image" src="https://github.com/user-attachments/assets/048e4edf-cca7-498d-bb84-961938b396a5" />

- Instruction map for the fio experiments. Each line approximately takes 2-5 hours for the single experiment run. For every run, two file will be collected. `nvmeX_waf_1sec.txt`(VM inside) and `log`(VM outside, `build-femu`).
- **VM** specifies which femu script should be launched.
- **1stream/2stream/3stream** is the experiment name corresponding to the paper.
- **log/nvme0_waf_1sec.txt** is needed for plotting. Recommend using `rsync` to get *nvme0_waf_1sec.txt*. Explain in later section.
<img width="1920" height="1080" alt="image (3)" src="https://github.com/user-attachments/assets/6ced7a0f-92da-4361-bee9-e98e857778dd" />
<img width="1920" height="1080" alt="image (4)" src="https://github.com/user-attachments/assets/524dfa89-b898-4850-893b-146556f34a58" />

- To generat
e Figure 11, run "./run_fdp_WARP4.sh". experiment will take 36 hours
- To generate Figure 13 and 16, run "./run_fdp_WARP_A.sh" in VM A. experiment will take 10 hours
- To generate Figure 15, run "./run_fdp_WARP_B.sh" in VM B. experiment will take (???) hours
- To generate Figure 14, run "./run_fdp_WARP_A2.sh". experiment will take 12 hours
- For Figure 17 and 18, run following four commands and each command will take 4 hours
- "./run_fdp_WARP256II10.sh"
- "./run_fdp_WARP256PI10.sh"
- "./run_fdp_WARP256II7.sh"
- "./run_fdp_WARP256P17.sh"


### Fig 11

### Fig 13

### Fig 




## Phase 3: Generate figures

- Once you have run all the experiments, go into the WARP repo directory that you cloned in the beginning and run <python3 -m notebook> and click on the jupyter notebook WARP-AE-FAST26-1.ipynb
- Start running all cells one by one
