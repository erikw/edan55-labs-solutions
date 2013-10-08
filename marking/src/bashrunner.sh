#!/usr/bin/env bash
rm aus;for i in {1..1000};do ./marking.py -r3 -H 3 >> aus;done
awk 'BEGIN{sum=0;cnt=0}{sum+=$4;cnt++}END{print sum/cnt}' aus
#awk '{print $4}' aus | sort -n | uniq -c | sort -n
