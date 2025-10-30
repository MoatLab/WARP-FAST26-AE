# 2stream write
This is the workload for 2 synthetic write, divided by two RUH.
One thread writes sequentially and the other writes random.
Two threads should be work with the same QD and bs.
10p 50p 90p explaines how much the capacity is being taken by random write thread(RUH1)


## mkdir

mkdir.sh will make nofdp/ and fdp/ subdirs under 10p/ 50p/ and 90p/ 
```
./mkdir.sh
```
for example, 
fdp_share/ can be ignored in this workload


BEFORE ./mkdir.sh
```
inho@hds03:.../seq_rand$ tree -d
.
├── 10p
│   └── archive
│       ├── fdp
│       └── nofdp
├── 50p
│   └── archive
│       ├── fdp
│       └── nofdp
└── 90p
    └── archive
        ├── fdp
        └── nofdp
```

AFTER ./mkdir.sh
```
inho@hds03:.../seq_rand$ tree -d
.
├── 10p
│   ├── archive
│   │   ├── fdp
│   │   ├── fdp_share
│   │   └── nofdp
│   ├── fdp
│   └── nofdp
├── 50p
│   ├── archive
│   │   ├── fdp
│   │   ├── fdp_share
│   │   └── nofdp
│   ├── fdp
│   └── nofdp
└── 90p
    ├── archive
    │   ├── fdp
    │   ├── fdp_share
    │   └── nofdp
    ├── fdp
    └── nofdp
```
