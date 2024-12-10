import obd
import time
from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int
# OBD connection parameters
fuel_used = 0
fuel_price = 7.11  # Price per liter in RON
total_cost = 0


def main():
    connection = obd.Async(portstr="/dev/rfcomm0", protocol="6", baudrate=115200, fast=False, timeout=30)

    print("Connection Status:", connection.is_connected())

    def printRPM(r):
        global RPM
        RPM = r.value.magnitude
        print(RPM)
        return RPM

    def printSPEED(r):
        global SPEED
        SPEED = r.value.magnitude
        print(SPEED)
        return SPEED
    SPEED = 69420
    connection.watch(obd.commands.RPM, callback=printRPM)
    connection.watch(obd.commands.SPEED, callback=printSPEED)

    connection.start()
    SPEED = 69420
    # The callback will now be fired upon receipt of new values
    try:
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        print("Stopping the connection...")
        connection.stop()

if __name__ == "__main__":
    SPEED = 69420
    main()
