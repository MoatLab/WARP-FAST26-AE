#!/bin/bash
for dir in */; do
  cp "5.get_waf.sh" "$dir"
  cp "6.get_bw.sh" "$dir"
  cp "trim.sh" "$dir"
done

