#!/bin/bash
for dir in */; do
    mkdir $dir/fdp $dir/nofdp
    echo " mkdir $dir/fdp $dir/nofdp ->done"
done
