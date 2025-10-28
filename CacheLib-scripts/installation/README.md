/data/inho/fdp-exp-scripts/CacheLib-scripts/installation



# liburing
Recommend installing liburing first 
CacheLib FDP requires liburing 2.3 >=


Prefer specific version
```
wget https://github.com/axboe/liburing/archive/refs/tags/liburing-2.7.tar.gz
```
Then
```
./configure --cc=gcc --cxx=g++;
make -j$(nproc);
make liburing.pc;
sudo make install;
```



or

```
git clone https://github.com/axboe/liburing
```
and proceed the same 


# CacheLib

Commit Release Stable 20240621

1. Redo CacheLib git
```
git clone https://github.com/facebook/CacheLib.git CacheLib
```

2. Set to c5c0d9b0 (v20240621 stable commit)
```
cd CacheLib
git reset --hard c5c0d9b08d7914343760d11cabd58fffa5775484
```


Then
```
./contrib/build.sh -j -T
```

See CacheLib_installation_problemshooting.pdf if you meet installation errors.



