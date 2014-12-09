#!/bin/bash

# monitor GPIO pin 7 (wiringPi pin 26) for shutdown signal

# export GPIO pin 7 and set to input with pull-up
#echo "7" > /sys/class/gpio/unexport

echo "7" > /sys/class/gpio/export
echo "in" > /sys/class/gpio/gpio7/direction
echo "high" > /sys/class/gpio/gpio7/direction

# wait for pin to go low
while [ true ]
do
if [ "$(cat /sys/class/gpio/gpio7/value)" == '0' ]
then
 echo "Raspberry Pi Shutting Down!"
 halt &
 exit 0
fi
sleep 0.1
done
