
FIO 3 synthetic workload.

RUH 0 : Rand write stream. Takes 10% LBA space and issues unform-random writes(4K QD=32)
RUH 1 : Seq. write stream. Takes 90% LBA space and writes sequentially(128K QD =1)
RUH 2 : overwrite stream. Takes 90% LBA space but overwrites RUH1's space with distribution(data hot/cold)(4K QD=32) 


Before run exps, make sure subdirs : "fdp" "fdp_share" "nofdp" are located under workload dirs.

Ex)
inho@hds03:~/.../3stream$ tree zoned
zoned
├── 5.get_waf.sh
├── 6.get_bw.sh
├── fdp
│   ├── samsung_bw_1sec.txt
│   └── samsung_waf_1sec.txt
├── fdp_share
├── nofdp
├── py_randwritefiles_bs4K_QD4_fdp
├── py_randwritefiles_bs4K_QD4_fdp_share
├── py_randwritefiles_bs4K_QD4_t0
└── trim.sh



To run all 
```
sudo nohup ./run_metascript_all.sh &
```
or 
```
./run_metascript_all.sh
```




