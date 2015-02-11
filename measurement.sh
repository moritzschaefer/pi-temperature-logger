#!/bin/bash

MEASURE_SCRIPT="/home/pi/Documents/DHT22/loldht"

output=$($MEASURE_SCRIPT | grep Humi)
humidity=$(echo $output  | awk '{print $3}')
temperature=$(echo $output  | awk '{print $7}')

/home/pi/Documents/DHT22/driveWriter.py --temperatur $temperature --humidity $humidity


