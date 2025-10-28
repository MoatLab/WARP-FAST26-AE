
# Trace Path
Note: path for 'traceFileNames' should be located in this directory(configs dir) 
for example, 
```
lrwxrwxrwx  1 inho inho       53 Sep 13 05:03 kvcache_traces_1.csv -> /data/inho/traces/kvcache/202206/kvcache_traces_1.csv
```

   "traceFileNames": [
            "kvcache_traces_1.csv",
            "kvcache_traces_2.csv",
            "kvcache_traces_3.csv",
            "kvcache_traces_4.csv",
            "kvcache_traces_5.csv"
    ]
  }


# Write only
We can populate only 'SET' in trace to see write amplification only.
To do this, use 'grep SET' to extract.

Do not forget to add the header of extracted write only trace
Add this line at the very beggining of the file.
```
key,op,size,op_count,key_size
```

```
inho@hds03:~/.../kvcache202206$ cat kvcache_traces_2.csv | head -20
key,op,size,op_count,key_size
1665500856,GET,93,1,44
1666349206,GET,256,1,72
1665497229,GET,1670,1,102
1665447489,GET,111,2,71
1665556232,GET,0,5,40
1669839030,SET,168,1,128
1669839030,GET,168,4,128
1669839030,SET,168,1,128
1669839030,GET,168,2,128
1668685228,GET,111,5,61
1669839030,SET,168,1,128
1669839030,GET,0,1,128
1669839030,SET,168,2,128
1669839030,GET,0,2,128
1669839030,SET,168,1,128
1669839030,GET,0,1,128
1665447811,GET,65,1,23
1669839114,GET,132,1,91
1669839030,SET,168,1,128
```

After extracting write(SET) only 

```
inho@hds03:.../202206$ cat kvcache_traces_1_SET.csv | head -20
key,op,size,op_count,key_size
1668757755,SET,82,1,40
1668757805,SET,208,1,63
1665702915,SET,109,1,40
1666365241,SET,162,1,88
1668757754,SET,263,1,32
1665502693,SET,570,1,96
1668758073,SET,110,1,70
1668757781,SET,94,1,54
1668758007,SET,173,4,67
1668757763,SET,932,1,77
1666654178,SET,99,1,59
1668761799,SET,157,1,63
1668761739,SET,110,1,38
1668762462,SET,148,1,32
1665578833,SET,121,1,80
1668762822,SET,65,1,23
1668763274,SET,184,1,34
1668765143,SET,165,1,71
1668761768,SET,100,1,60
1668763274,SET,110,1,34
```
