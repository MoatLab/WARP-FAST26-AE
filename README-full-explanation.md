
```
Dear FAST artifact evaluation committees,

I'm one of the authors of 'Characterizing and Emulating FDP SSDs with WARP' and this is the doc for the artifact reproduction document.
We hope this document helps to reproduce the results of WARP, given that this is also an open-source contribution for the community.

The results of this paper convey both real SSDs and WARP write amplification results.
These require making a workload size 5 to 10 times the device capacity for a thorough investigation.
This leads to 4 to 5 hours for each line in a single figure in this paper.
Artifact evaluation for this paper, therefore, will consume more than 100hours, approximately 1 week to reproduce all experiments result and plot them.
Plus, in the paper, there are real FDP SSD experiments.
Some experiments take at least 4 hours to run.
At most, 1 week of one experiment to collect the write amplification result from a real SSD(e.g., CacheLib).
Given that one experiment corresponds to one line in the figure, the actual amount of time to reproduce all the results will take more than a month.
These numbers assume that the experiment successfully finished without any human mistakes (e.g., incorrect parameter setting or script) and unexpected system failure.

Since this amount of time is a burden for artifact evaluation, we collect and select core experiments that represent this paper the most.
Given that the contributions of this paper are explaining the write amplification phenomenon with WARP and the reliability of WARP itself,
We select and organize the following experiments for FAST artifact evaluation.

This document will help you to initiate experiments, generate results, make and check figures in the paper.
Due to the amount of time, we first recommend generating and evaluating a subset of each figure, instead of reproducing all exps for a single figure (e.g., Fig. 13a, FDP line).
Although we are providing instructions for selected experiments, we prepare all experiment scripts for the entire experiment in the paper.

Thank you.
```
# Experiment scripts for WARP
These are the scripts that I used for both FDP SSD and WARP(the old name Cylon-FDP) testing.

* FDP SSD setup (real FDP SSD nvme-cli setup)
```
sudo ./fdp_setup_nvme-cli.sh /dev/nvmeX
```

# Phase 0. Prerequisite(Inside the VM)
**Note. If you are using the provided VM image, skip this step.**
## meson

## libnvme
I'm using `nvme fdp ` command to get the write amplification results
to use, libnvme should be v1.5

```
wget https://github.com/linux-nvme/libnvme/archive/refs/tags/v1.5.tar.gz
```
```
tar -xvf v1.5.tar.gz; cd libnvme-1.5/;
```
```
meson setup .build; meson compile -C .build; sudo meson install -C .build;
```
```
sudo cp /usr/local/lib/x86_64-linux-gnu/libnvme.so.1.5.0 /usr/lib/.
sudo cp /usr/local/lib/x86_64-linux-gnu/libnvme-mi.so.1.5.0 /usr/lib/.
sudo ln -sf /usr/lib/libnvme-mi.so.1.5.0 /usr/lib/libnvme-mi.so.1
sudo ln -sf /usr/lib/libnvme.so.1.5.0 /usr/lib/libnvme.so.1
sudo ln -sf /usr/lib/libnvme.so.1 /usr/lib/libnvme.so
sudo ln -sf /usr/lib/libnvme-mi.so.1 /usr/lib/libnvme-mi.s
sudo ln -sf /usr/lib/libnvme-mi.so.1 /usr/lib/libnvme-mi.so
```
## nvme-cli
```
wget https://github.com/linux-nvme/nvme-cli/archive/refs/tags/v2.5.tar.gz
```
```
tar -xvf v2.5.tar.gz ; cd nvme-cli-2.5/;
```
```
meson setup .build; meson compile -C .build; sudo meson install -C .build 
```
```
sudo cp .build/nvme /usr/sbin/nvme
```
check nvme-cli version
```
nvme --version
```
result should be
```
femu@fvm:~/libs/nvme-cli-2.5/.build$ nvme --version
nvme version 2.5 (git 2.5)
libnvme version 1.5 (git 1.5)
```

## liburing 
version 2.3 >= works fine. Scripts for liburing install.
```bash
wget https://github.com/axboe/liburing/archive/refs/tags/liburing-2.3.tar.gz
```
```
tar -xvf liburing-2.3.tar.gz; cd liburing-liburing-2.3/
```
```
./configure --cc=gcc --cxx=g++;
make -j$(nproc);
sudo make install;
```

Also works fine with
v2.3
v2.6
v2.7
v2.9
v2.10


## FIO
version 3.36
```bash
wget https://github.com/axboe/fio/archive/refs/tags/fio-3.36.tar.gz
```
```
tar -xvf fio-3.36.tar.gz ; cd fio-fio-3.36/
```
```
./configure ;
make;
sudo make install;
```

## Kernel
Using 6.2.14

Also tested with
v6.5.6
v6.10.x (especially F2FS, 6.10.x)

## Kernel-FDP patch
TBD

# 1. WARP evaluation procedure and requirements

## Phase 1: infrastructure setup

- Hardware and environment: a KVM-enabled x86_64 server with Linux 6.2.14 or 6.5.6.
- DRAM requirement: 500GB+ DRAM (Over 500GB enabled to run 2VMs at the same time(224G*2))
- VM preparation: clone the WARP repo with `git https://github.com/inhoinno/WARP-earlyaccess.git` and pull the image with <command>. Then, move into <director> and run <./run_fdp_RU256.sh> to start the qemu VM
- Then connect to VM using this ssh <ssh -P 18080 warp@localhost>
- This process will consume about 1 hour, and most of the time will be spent pulling the image.
 
## Phase 2: experiment run 
These figures help to comprehend how to use WARP and plot the figures in the paper from the experiment output. Detailed instructions are given next section.
### Overview
<img width="949" height="309" alt="image" src="https://github.com/user-attachments/assets/048e4edf-cca7-498d-bb84-961938b396a5" />

   * Two steps for setting up the env.This is the basic experiment setup for WARP.
       1. Launch the VM(script in `build-femu` dir)
       2. Launch the exp script(this repo) to run the experiments. 
   * Two files will be needed for figure plotting.
       1. `nvmeX_waf_1sec.txt` (or `samsung_waf_1sec.txt` by `5.get_waf.sh` script)
       2. `log` file. This is located outside of the VM, in `build-femu` directory.
   * In here, `sudo ./run_fdp_RU256.sh` (or `sudo nohup ./run_fdp_RU256.sh &`) to launch the VM. This is equivalent to WARP-A. Make sure your VM is using libnvme 1.5 and fio 3.36(`pkg-config --modversion libnvme` and `fio --version`). GC policy is greedy.

### Fig 11, 13, 14, 15, 16, 17, and 18 (FIO)
<img width="1920" height="1080" alt="image (3)" src="https://github.com/user-attachments/assets/6ced7a0f-92da-4361-bee9-e98e857778dd" />

- Instruction map for the fio experiments. Each line approximately takes 2-5 hours for a single experiment run. For every run, two files will be collected. `nvmeX_waf_1sec.txt`(VM inside) and `log`(VM outside, `build-femu`).
- **VM** specifies which femu script should be launched.
- **1stream/2stream/3stream** is the experiment name corresponding to the paper.
- **log/nvme0_waf_1sec.txt** is needed for plotting. Recommend using `rsync` to get *nvme0_waf_1sec.txt*. Explain in later section.

#### Fig 11

- VM
   * In `build-femu` dir, run `./run-fdp-WARP4.sh`
   * ssh to VM `ssh -P 18080 femu@localhost`
   * `git clone https://github.com/MoatLab/fdp-exp-scripts;` (skip if you have done this)
   * `cd fdp-exp-scripts; pushd .; cd FIO-scripts/1stream/`
   * `sudo nohup ./run-fig11.sh &` or `sudo ./run-fig11.sh` (Ctrl^C if goes wrong)
   * Experiment will take ~2hours.
   * After the experiment, `popd`
   * Go `python3 Fig11.py` and check `val-1stream-AE.jpeg` file for Fig11. (Check Fig11.ipynb if you prefer this)
 

------
TBD from here
#### Fig 13 and 16
- Figure 13 and 16, run `./run_fdp_WARP_A.sh`, ssh to VM, and `run-fig1316.sh`. `nvmeX_waf_1sec.txt` file is for fig13. `log` file in build-femu dir is for Fig16. Experiment will take 10 hours.

#### Fig 14
- Figure 14, run "./run_fdp_WARP_A2.sh". experiment will take 12 hours

#### Fig 15
- Figure 15, run "./run_fdp_WARP_B.sh", ssh to VM, and run `run-fig15.sh`. Experiment will take (???) hours


#### Fig 17 and 18
<img width="955" height="402" alt="image" src="https://github.com/user-attachments/assets/2cec25f9-3195-4a53-80b3-2504ba987dd6" />

- For Figures 17 and 18, run the following four commands. Each command will take 4 hours. For every exp, we advise shutting down and relaunching the VM.
  * `./run_fdp_WARP256II10.sh` -> `ssh -P 18080 warp@localhost` -> `command here` -> `mv log fixme_log` -> `mv fixme_log dir/fixme_log`
  * `./run_fdp_WARP256PI10.sh` -> `ssh -P 18080 warp@localhost` -> `command here` -> `mv log fixme_log` -> `mv fixme_log dir/fixme_log`
  * `./run_fdp_WARP256II7.sh` -> `ssh -P 18080 warp@localhost` -> `command here` -> `mv log fixme_log` -> `mv fixme_log dir/fixme_log`
  * `./run_fdp_WARP256P17.sh` -> `ssh -P 18080 warp@localhost` -> `command here` -> `mv log fixme_log` -> `mv fixme_log dir/fixme_log`
  * plot figure 17 and 18 with ipynb file.





## Phase 3: Generate figures

- Once you have run all the experiments, go into the WARP repo directory that you cloned in the beginning and run <python3 -m notebook> and click on the jupyter notebook WARP-AE-FAST26-1.ipynb
- Start running all cells one by one
