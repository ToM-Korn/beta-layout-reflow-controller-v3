# Command Line Tools and maybe more for the BETA Layout Reflow Controller v3 #
More Infos at: http://www.beta-estore.com/rkuk/order_product_details.html?wg=1&p=613
BETA Layout Item Number: RK-10579


## Purpose ##
This is the first step of command line tools | controlling software for the Reflow
Controller by Beta Layout.
For me it was neccessary to keep the ofen at a certain temperature for a defined time.
For example to dry a photo positiv paint or a photo positiv solder mask
Further i dried cleaned electronic component for example at 60º C for 30 minutes with
the script.

## installation instructions ##
1. clone or copy this repository to your computer
2. go to the folder where you copied it
3. start your Reflow Controller and Connect it to your Computer
4. you may have to change the Serial Port in the Script (TODO-Implement in Command Line)
3. start it from command line with: python rf_keep_warm.py [temp(in C)] [time(in min)]
	replace temp with the temperature you like to heat the ofen to 
	replace time with the time you like to keep the ofen on that themperatur
	example: python rf_keep_warm.py 80 15
	> keep the ofen at 80 degrees for 15 minutes
4. the current temperature and downcounting time in sec are displayed at the terminal

## Configuration instructions ##
Feel free to improve or change the script
please fork the repo and let me know about improvments 

## Files ##
- rf_keep_warm.py the main script

## copyright and licensing information ##
#### Author of rf_keep_warm.py ####
ToM Krickl

#### License ####
CC0 1.0 Universal
please see the LICENSE file for further information.

## contact information for the distributor or programmer ##
- email: git@krickl.eu
- phone: please ask me in email 
- web: www.krickl.eu

## known bugs ##
sometimes it can not send the rf controller into manual mode
restarting the script again helped
will see to solve that in the next release...

## troubleshooting ##
don't panic... write me a mail or solve the problem and commit it :)

## credits and acknowledgements ##
Thanks to Beta Layout - their awesome Service, Products and Support :) 

## changelog ##
please see the github repository commits