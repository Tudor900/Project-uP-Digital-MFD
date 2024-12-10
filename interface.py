from flask import Flask, render_template, jsonify
from threading import Thread
import time
import random


app = Flask(__name__)
label_text = "Original Label"

  



# Background task to update the label
def modify_speed():
    while True:      
          # Simulate a long-running task
        label_text = "test"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_speed')
def get_speed():
    return jsonify({"speed": label_text})


    

if __name__ == '__main__':

    Thread(target=modify_speed, daemon=True).start()  # Run the background task
    app.run(debug=True)


