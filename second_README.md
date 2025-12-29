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

- VM
   * In `build-femu` dir, run `./run-fdp-WARP4.sh`
   * ssh to VM `ssh vm` (See **tip**) or `ssh -P 18080 femu@localhost`
   * `git clone https://github.com/MoatLab/fdp-exp-scripts;` (skip if you have done this)
   * `cd fdp-exp-scripts; pushd .; cd FIO-scripts/`
   * `sudo nohup ./run-fig11.sh &` or `sudo ./run-fig11.sh` (Ctrl^C if goes wrong)
   * Experiment will take ~2hours.
   * `popd` and run `python3 Fig11.py` and check `val-1stream-AE.jpeg` file for Fig11. (Check Fig11.ipynb if you prefer this)
 
#### Three stream write experiment (Fig 13,15, and 16)

- VM
   * In `build-femu` dir, run `./run-fdp-RU256.sh`
   * ssh to VM ssh vm` (See **tip**) or `ssh -P 18080 femu@localhost`
   * `cd fdp-exp-scripts; pushd .; cd FIO-scripts/`
   * `sudo ./run-fig1316.sh`. (`sudo nohup ./run-fig1316.sh &` if you already have a root shell. Ctrl^C if it goes wrong)
   * Experiment will take ~3hours.
   * `popd`(or `cd ~/fdp-exp-scripts`) and run `python3 Fig13.py`.
   * check `val-3stream-AE.jpeg` file for Fig13. (Check Fig13.ipynb if you prefer this)



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
