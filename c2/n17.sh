#!/bin/ash

cd `dirname $0`
LC_ALL=C sort -n hightemp.txt | uniq -w 4
