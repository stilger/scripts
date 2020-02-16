# Misc Scripts

#### check-set-speed.sh - Used to set the speed of Acorns and FK33's for SQRL miner. 
   * I run this on [mmpOS](https://app.mmpos.eu) from the /etc/rc.local with this command:
         
         screen -mDSL 'ssc' /home/miner/check-set-speed.sh &
   * You will need to modify the check_set_speed.sh script with your own settings:
      * For the SQRL Miner commands:
      * a/#: select All or device # | +/-: Increase/decrease speed by 5 mhz | n/p: Select Next/Previous Device
      * You will need to manually figure out the correct speeds for your devices then set speeds. I have mine commands
      * increase all devices by 10 and then select my FK33's (1 and 2) and set them back to 800 by decreasing both by 10. 
      * I then set the speed of each indiviudal device by number then by using the n to choose nest for each device past 9
      
      screen -S miner0 -p 0 -X stuff "a++++++++++1----------2----------3+++++++4++++++5++++++++++"
      sleep 10
      screen -S miner0 -p 0 -X stuff "8+++9+n++++++n+++++++n+++++++n++++++++++n++++++++++n++++n++"
