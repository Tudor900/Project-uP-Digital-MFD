from flask import Flask, render_template, jsonify
from threading import Thread
import time
import random
import obdconnection
import obd
import time
from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int



app = Flask(__name__)
label_text = 69420

connection = obd.Async(portstr="/dev/rfcomm0", protocol="6", baudrate=115200, fast=False, timeout=30)

print("Connection Status:", connection.is_connected())

def printRPM(r):
    global RPM
    RPM = r.value.magnitude
    print(RPM)
    return RPM

def printSPEED(r):
    global SPEED
    SPEED = r.value
    print(SPEED)
    return SPEED
SPEED = 69420
connection.watch(obd.commands.RPM, callback=printRPM)
connection.watch(obd.commands.SPEED, callback=printSPEED)

connection.start()

# Background task to update the label
def modify_speed():
    while True:      
          # Simulate a long-running task
        global SPEED
        label_text = SPEED
        

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_speed')
def get_speed():
    return jsonify({"speed": label_text})


    

if __name__ == '__main__':
    Thread(target=modify_speed, daemon=True).start()  # Run the background task
    app.run(debug=True)


