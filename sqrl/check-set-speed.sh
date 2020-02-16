#!/bin/bash
echo "Terminating running miner0 session"
screen -S miner0 -p 0 -X stuff "q"
echo "Wating for miner0 - Sleeping for 2 minutes"
date
sleep 30
echo "90 seconds left"
sleep 30
echo "60 seconds left"
sleep 30
echo "30 seconds left"
sleep 30
while true
do
  if ! screen -list | grep -q $screen_pid_name 2>/dev/null;
  then
      screen_pid_name=`screen -ls | grep miner0 | awk {'print $1}'`
      echo "Set screen_pid_name to: $screen_pid_name"
      echo "Making sure Miner is runnning - Sleeping for 1 minute"
      date
      sleep 30
      echo "30 seconds left"
      sleep 30
      echo 'Setting speed'
      # For the SQRL Miner commands:
      # a/#: select All or device # | +/-: Increase/decrease speed by 5 mhz | n/p: Select Next/Previous Device
      # You will need to manually figure out the correct speeds for your devices then set speeds. I have mine commands
      # increase all devices by 10 and then select my FK33's (1 and 2) and set them back to 800 by decreasing both by 10. 
      # I then set the speed of each indiviudal device by number then by using the n to choose nest for each device past 9
      screen -S miner0 -p 0 -X stuff "a++++++++++1----------2----------3+++++++4++++++5++++++++++"
      sleep 10
      screen -S miner0 -p 0 -X stuff "8+++9+n++++++n+++++++n+++++++n++++++++++n++++++++++n++++n++"

else
      echo "Same Screen:$screen_pid_name - Sleeping for 5 minutes"
      date
      sleep 300
  fi
done
