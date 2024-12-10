import obd
import time
from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int

# OBD connection parameters
fuel_used = 0
fuel_price = 7.11  # Price per liter in RON
total_cost = 0
connection = obd.Async(portstr="/dev/rfcomm0", protocol="6", baudrate=115200, fast=False, timeout=30)

print("Connection Status:", connection.is_connected())

def test(msg):
    return msg

c = OBDCommand("RPM",         # name
               "Engine RPM",   # description
               b"2210C0",        # command
               2,              # number of return bytes to expect
               test,            # decoding function
               ECU.ENGINE,      # (optional) ECU filter
               True)             # (optional) allow a "01" to be added for speed
connection.supported_commands.add(c)
print(connection.query(c))
