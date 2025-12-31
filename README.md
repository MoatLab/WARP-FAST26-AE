# WARP evaluation procedure and requirements
```
Dear FAST artifact evaluation committees,

This repository is for artifact reproduction of 'Characterizing and Emulating FDP SSDs with WARP' (AE #51).
We hope this document helps to reproduce the results of WARP, given that this is also an open-source contribution for the community.

We select a couple of experiments for the artifact evaluation of this paper. 
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
## Phase 1: infrastructure setup

- Hardware and environment: a KVM-enabled x86_64 server with Linux 6.2.14 or 6.5.6.
- DRAM requirement: 500GB+ DRAM (Over 500GB enabled to run 2VMs at the same time(224G*2))
- VM preparation
   * pull the image with `wget https://people.cs.vt.edu/inhoinno/image/u20s.qcow2.xz`. Run `xz -dv -T0 u20s.qcow2.xz` after download.
   * `mkdir image` and `mv u20s.qcow2 image/.`
   * Clone the WARP repo with `git clone https://github.com/MoatLab/WARP-earlyaccess.git` (or `git clone https://github.com/inhoinno/WARP-earlyaccess.git`), `cd WARP-earlyaccess`, and follow the FEMU README instructions.
       * 1. Make sure you have installed the necessary libraries for building QEMU. The dependencies can be installed by following the instructions below:
      ```
      mkdir build-femu
      # Switch to the FEMU building directory
      cd build-femu
      # Copy femu script
      cp ../femu-scripts/femu-copy-scripts.sh .
      ./femu-copy-scripts.sh .
      # only Debian/Ubuntu based distributions supported
      sudo ./pkgdep.sh
      ```
      * 2. Compile & Install FEMU:
      ```
      ./femu-compile.sh
      ```

   * After copying scripts and compiling(FEMU README), go `build-femu` dir and run `./run-fdp-WARP4.sh` to start the qemu VM.
   * WARP run-scripts like `./run-fdp-WARP4.sh` assumes the `u20s.qcow2` image is located `~/image/u20s.qcow2`. If you are using a different directory, change the path in `./run-fdp-WARP4.sh`
     ```bash
     # image directory
     IMGDIR=$HOME/image
     # Virtual machine disk image
     OSIMGF=$IMGDIR/u20s.qcow2
     ```
- Open another terminal and connect to VM using this ssh <ssh -P 18080 femu@localhost>. pw is femu.
- This process will consume about 1 hour, and most of the time will be spent pulling the image.
- **Tip** Open `~/.ssh/config` and add this entry for vm.
  ```
  Host vm
    HostName localhost
    User femu
    Port 18080
    ServerAliveInterval 20
    ServerAliveCountMax 2147483
  ```
  Now just type `ssh vm` to access the VM.
- Setup for experiment run
   * Access to the VM image `ssh vm`
   * `git clone https://github.com/MoatLab/WARP-FAST26-AE.git`, then you have this repository.
     Check `nvme fdp stats /dev/ng0n1 -e 1` command works after installation.
     ```
      femu@fvm:~/libs/nvme-cli-2.5$ sudo nvme fdp stats /dev/ng0n1 -e 1
      Host Bytes with Metadata Written (HBMW): 0
      Media Bytes with Metadata Written (MBMW): 0
      Media Bytes Erased (MBE): 0
     ```
     Now ready to begin.
     
     <details>
      <summary> Click if `nvme fdp` does not work </summary>
      
     ### nvme-cli 
     To use `nvme fdp` subcommand, `nvme-cli` needs to be recompiled after libjson-c installation.
     ```
     sudo apt install libjson-c-dev
     cd ~/libs/nvme-cli-2.5
     meson setup .build
     meson compile -C .build
     mesonn install -C .build # (This ask sudo privilege)
     ```
## Phase 2: experiment run 

#### One stream write experiment (Fig 11)
**NOTE: Check whether FDP SSD emul works as a FDP mode (WARP-earlyaccess/hw/femu/bbssd/ftl.h:11)**
```
#define SSD_STREAM_WRITE 
//#define FORCE_NOFDP <- disabled is correct
```
- Host (Skip this part if Phase 1 VM is alive)
   * In `build-femu` dir, run `./run-fdp-WARP4.sh`
   * ssh to VM `ssh vm` (See **Tip** in Phase 1.) or `ssh -P 18080 femu@localhost`

- VM
   * `cd WARP-FAST26-AE; pushd .; cd FIO-scripts/`
   * `sudo nohup ./run-fig11.sh &` or `sudo ./run-fig11.sh` (Ctrl^C if it goes wrong)
   * Experiment will take ~2hours.
   * `popd` and run `python3 Fig11.py` and check `val-1stream-AE.jpeg` file for Fig11. (Check Fig11.ipynb if you prefer this. If the script and results locate the exact path, `[Check!]` mark will appear for all `.txt` file.)
 
#### Three stream write experiment (Fig 13,15, and 16)
(shutdown previous VM if the previous one is alive.)
- Host
   * In `build-femu` dir, run `./run-fdp-RU256.sh`
   * ssh to VM `ssh vm` (See **Tip**) or `ssh -P 18080 femu@localhost`
 
- VM
   * `cd fdp-exp-scripts; pushd .; cd FIO-scripts/`
   * `sudo ./run-fig1316.sh`. (`sudo nohup ./run-fig1316.sh &` if you already have a root shell. Ctrl^C if it goes wrong)
   * Experiment will take ~3hours.
   * `popd`(or `cd ~/WARP-FAST26-AE`) and run `python3 Fig13.py`.
   * check `3stream_WARP_AE.jpeg` file for Fig13. (Check Fig13.ipynb if you prefer this)

- Host: move `log` file in Host to VM (Fig15&16)
   * In the host machine(outside VM), locate to `build-femu` directory. 
   * `rsync log vm:~/fdp-exp-scripts/archive/ops-log/log-gc-zoned-fdp-AE` (See **Tip** in Phase 1.)
   * Then ssh to VM `ssh vm` (See **Tip**) or `ssh -P 18080 femu@localhost`
 
- VM
   * `cd ~/fdp-exp-scripts` and run `python3 Fig1516.py`
   * Check `fdp_3syn_investigation-HBMWDLWA-AE.jpeg` and `Noisy.jpeg`. (Check Fig131516.ipynb if you prefer this)
 
#### Three stream write experiment (Fig 14)
(shutdown previous VM if the previous one is alive.)
- Host
  * In `build-femu` dir, run `./run-fdp-RU128-WARPA2.sh`
  * ssh to VM `ssh vm` (See **Tip**) or `ssh -P 18080 femu@localhost`
- VM
  * `cd fdp-exp-scripts; pushd .; cd FIO-scripts/`
  * `sudo ./run-fig14.sh`. (`sudo nohup ./run-fig14.sh &` if you already have a root shell. Ctrl^C if it goes wrong)
  * Experiment will take ~12 hours(4exp*3hr).
  * `popd`(or `cd ~/WARP-FAST26-AE`) and run `python3 Fig14.py`.
  *  Check `3Syn_CylonA2.jpeg` is generated in the current directory.


#### (Optional) II vs PI (Fig 17)
Proceed with these steps if the experiment results are insufficient for the AE 'Result reproduced' badges.
Before proceeding, make sure all figures are generated. 
Run `cd ~/WARP-FAST26-AE/FIO-scripts/3stream/zoned/fdp/; mv samsung_waf_1sec.txt samsung_waf_1sec_Fig11.txt` to avoid overwritting.

- For Figure 17 and 18, run the following four commands, and each experiment will take 4 hours
- Host:locate to `build-femu` directory and run `./run_fdp_WARP256II10.sh` -> `ssh vm` -> VM `cd ~/WARP-FAST26-AE/FIO-scripts/3stream` -> `sudo ./run_metascript_one.sh` -> (~4hr Fin) -> Host:locate to `build-femu` directory -> `cat log | grep "is_force" > temp`-> `rsync temp vm:~/WARP-FAST26-AE/archive/ops-log/log-ii-zoned-RU256OP10-AE` -> shutdown vm(Use `kill` or `ssh vm` then `shutdown -h 0`)
- Host:locate to `build-femu` directory and run  `./run_fdp_WARP256PI10.sh` -> `ssh vm` -> VM `cd ~/WARP-FAST26-AE/FIO-scripts/3stream` ->`sudo ./run_metascript_one.sh` -> (~4hr Fin) -> Host:locate to `build-femu` directory -> `cat log | grep "is_force" > temp`-> `rsync temp vm:~/WARP-FAST26-AE/archive/ops-log/log-pi-zoned-RU256OP10-AE`
- Host:locate to `build-femu` directory and run  `./run_fdp_WARP256II14.sh` -> `ssh vm` -> VM `cd ~/WARP-FAST26-AE/FIO-scripts/3stream` -> `sudo ./run_metascript_one.sh` -> (~4hr Fin) -> Host:locate to `build-femu` directory -> `cat log | grep "is_force" > temp` -> `rsync temp vm:~/WARP-FAST26-AE/archive/ops-log/log-ii-zoned-RU256OP14-AE`
- Host:locate to `build-femu` directory and run  `./run_fdp_WARP256PI14.sh` -> `ssh vm` -> VM `cd ~/WARP-FAST26-AE/FIO-scripts/3stream` -> `sudo ./run_metascript_one.sh` -> (~4hr Fin) -> Host:locate to `build-femu` directory -> `cat log | grep "is_force" > temp` -> `rsync temp vm:~/WARP-FAST26-AE/archive/ops-log/log-pi-zoned-RU256OP14-AE`
- VM:Run `python3 Fig17.py` and check `fdp_8020_IIvsPI-OPSplot2.jpeg`(/.pdf/.png) that has black line for AE.

## Phase 3: Gather figures
- Host
  * Run `rsync vm:~/WARPWARP-FAST26-AE/*.jpeg . ` if `ssh vm` is available(See **Tip**)
