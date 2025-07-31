# voltronic
python lib protocol com for voltronic inverter 

Inverter.py :
State of Voltronic type of inverter

wksSendCommand.py :
contain wksProtocol class, this class allow to comunicate from rs232 line with a voltronic inverter (can be updated for all mode / inverter)

wksGetStatus.py :
use the 2 precedent files to get the state of the inverter

main.py :
CRON task use to periodiquely read inverter state and send data to BDD thrue local web services 
CRON mask :
*/1 * * * * python /path/to/your/python/files/main.py /dev/ttyUSB0 
setXXX.py  :

shortcut to basic command
