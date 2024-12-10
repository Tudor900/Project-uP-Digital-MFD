import obd
import time
from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int
obd.logger.setLevel(obd.logging.DEBUG)
# OBD connection parameters
fuel_used = 0
fuel_price = 7.11  # Price per liter in RON
total_cost = 0
connection = obd.Async(portstr="/dev/rfcomm0", protocol="6", baudrate=115200, fast=False, timeout=30)

print("Connection Status:", connection.is_connected())

afr = 1/14.7
MAF = 0
SPEED = 0
def printMAF(r):
    global MAF
    MAF = r.value.magnitude
    print(r.value)
    #time.sleep(1)
    
def printSPEED(r):
    global MAF
    global SPEED
    SPEED = r.value.magnitude
    fuel = (3600000*MAF)/(SPEED * 14.7 * 832)
    print(fuel)
    print(r.value)
    #time.sleep(1)

    
connection.watch(obd.commands.MAF, callback=printMAF)
connection.watch(obd.commands.SPEED, callback=printSPEED)

connection.start()

# The callback will now be fired upon receipt of new values
try:
    while True:
        time.sleep(1)  # Keep the script running
except KeyboardInterrupt:
    print("Stopping the connection...")
    connection.stop()
