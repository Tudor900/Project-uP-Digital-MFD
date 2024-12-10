import obd
import time
from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int
#obd.logger.setLevel(obd.logging.DEBUG)
# OBD connection parameters
fuel_used = 0
fuel_price = 7.11  # Price per liter in RON
total_cost = 0
def test():
    return "Main is connected"
    exit(1)



connection = obd.Async(portstr="/dev/rfcomm0", protocol="6", baudrate=115200, fast=False, timeout=30)

print("Connection Status:", connection.is_connected())



def printRPM(r):
    global RPM
    RPM = r.value.magnitude
    print(RPM)
    return RPM
    #time.sleep(1)
    
def printSPEED(r):
    global SPEED
    SPEED = r.value.magnitude
    print(SPEED)
    return SPEED
    #time.sleep(1)

    
connection.watch(obd.commands.MAF, callback=printRPM)
connection.watch(obd.commands.SPEED, callback=printSPEED)

connection.start()

# The callback will now be fired upon receipt of new values
try:
    while True:
        time.sleep(1)  # Keep the script running
except KeyboardInterrupt:
    print("Stopping the connection...")
    connection.stop()
