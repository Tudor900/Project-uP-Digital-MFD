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
import serial
import time


app = Flask(__name__) #flask app
speed_label = 0 # Global variable to store the speed
rpm_label = 0

def test_label1():
    global speed_label
    while True:
        for i in range(0,5):
            speed_label += 50
            if(speed_label == 200):
                time.sleep(0.5)
                speed_label = 0
            time.sleep(1)
        

def test_label2():
    global rpm_label
    while True:
        for i in range(0,7):
            rpm_label += 1000
            if(rpm_label == 6000):
                time.sleep(0.5)
                rpm_label = 0
            time.sleep(1)

#connection = obd.Async(portstr="/dev/tty.OBDII", protocol="6", baudrate=115200, fast=False, timeout=30) # OBD connection
#print("Connection Status:", connection.is_connected()) # Check if the connection is established


def printRPM(r):
    global rpm_label
    rpm_lable = r.value.magnitude
    
    print(RPM)
    return RPM

def printSPEED(r):
    global speed_label
    
    speed_lable = r.value.magnitude
    
    print(SPEED)
    return SPEED


#connection.watch(obd.commands.RPM, callback=printRPM) # Watch the RPM command
#connection.watch(obd.commands.SPEED, callback=printSPEED) # Watch the speed command

#connection.start() # Start the connection

# # Background task to update the label
# def modify_speed():
#     while True:      
#           # Simulate a long-running task
#         global RPM
#         label_text = printRPM()
#         print("RPM: ", label_text)
        

@app.route('/')
def index():
    return render_template('index.html') # render the HTML template

@app.route('/get_speed')
def get_speed():
    return jsonify({"speed": speed_label, "rpm": rpm_label}) # Return the speed


    

if __name__ == '__main__':
    Thread(target=test_label1, daemon=True).start()  # Run the background task
    Thread(target=test_label2, daemon=True).start()
    app.run(debug=True)


