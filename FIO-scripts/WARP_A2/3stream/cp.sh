#!/bin/bash
for dir in */; do
  mkdir -p "$dir/fdp" "$dir/nofdp" "$dir/fdp_share" "$dir/fdp_share2"
  cp "./*.sh $dir/."
done

