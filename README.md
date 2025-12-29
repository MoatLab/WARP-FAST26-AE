# WARP evaluation procedure and requirements

## Phase 1: infrastructure setup

- Hardware and environment: a KVM-enabled x86_64 server with Linux 6.2.14 or 6.5.6.
- DRAM requirement: 500GB+ DRAM (Over 500GB enabled to run 2VMs at the same time(224G*2))
- VM preparation: clone the WARP repo with `git https://github.com/inhoinno/WARP-earlyaccess.git` and pull the image with <command>. Then, move into <director> and run <./run_fdp_RU256.sh> to start the qemu VM
- Then connect to VM using this ssh <ssh -P 18080 warp@localhost>
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

## Phase 2: experiment run 

#### One stream write experiment (Fig 11)

- Host
   * In `build-femu` dir, run `./run-fdp-WARP4.sh`
   * ssh to VM `ssh vm` (See **Tip** in Phase 1.) or `ssh -P 18080 femu@localhost`

- VM
   * `git clone https://github.com/MoatLab/fdp-exp-scripts;` (skip if you have done this)
   * `cd fdp-exp-scripts; pushd .; cd FIO-scripts/`
   * `sudo nohup ./run-fig11.sh &` or `sudo ./run-fig11.sh` (Ctrl^C if goes wrong)
   * Experiment will take ~2hours.
   * `popd` and run `python3 Fig11.py` and check `val-1stream-AE.jpeg` file for Fig11. (Check Fig11.ipynb if you prefer this)
 
#### Three stream write experiment (Fig 13,15, and 16)
(shutdown previous VM if the previous one is alive.)
- Host
   * In `build-femu` dir, run `./run-fdp-RU256.sh`
   * ssh to VM `ssh vm` (See **Tip**) or `ssh -P 18080 femu@localhost`
 
- VM
   * `cd fdp-exp-scripts; pushd .; cd FIO-scripts/`
   * `sudo ./run-fig1316.sh`. (`sudo nohup ./run-fig1316.sh &` if you already have a root shell. Ctrl^C if it goes wrong)
   * Experiment will take ~3hours.
   * `popd`(or `cd ~/fdp-exp-scripts`) and run `python3 Fig13.py`.
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
  * `popd`(or `cd ~/fdp-exp-scripts`) and run `python3 Fig14.py`.
  *  Check `3Syn_CylonA2.jpeg` is generated in the current directory.


#### (Optional) II vs PI (Fig 17 and 18)
Proceed this step if the experiment results are insufficient for the AE 'Result reproduced' badges.
TBD 
- For Figure 17 and 18, run following four commands and each command will take 4 hours
- "./run_fdp_WARP256II10.sh"
- "./run_fdp_WARP256PI10.sh"
- "./run_fdp_WARP256II7.sh"
- "./run_fdp_WARP256P17.sh"


## Phase 3: Generate figures
TBD 
- Once you have run all the experiments, go into the WARP repo directory that you cloned in the beginning and run <python3 -m notebook> and click on the jupyter notebook WARP-AE-FAST26-1.ipynb
- Start running all cells one by one
