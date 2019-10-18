from sense_hat import SenseHat
from flask import Flask, jsonify, request
from datetime import datetime
import csv
import math
import json

JSONFILE = 'sense-hat-data.json'
MY_IP = '10.197.119.190'
app = Flask(__name__)
sense = SenseHat()
sense.clear()

def get_sense_data():
	sense_data = []
	orientation = sense.get_orientation()
	mag = sense.get_compass_raw()
	acc = sense.get_accelerometer_raw()
	gyro = sense.get_gyroscope_raw()
	
	# DateTime
	sense_data.append(datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
	
	# Environmental sensors
	sense_data.append(round(sense.get_temperature(), 4))
	sense_data.append(round(sense.get_pressure(), 4))
	sense_data.append(round(sense.get_humidity(), 4))
	
	# Orientation
	sense_data.append(round(orientation["yaw"], 4))
	sense_data.append(round(orientation["pitch"], 4))
	sense_data.append(round(orientation["roll"], 4))
	
	# Raw compass readings
	sense_data.append(round(mag["x"], 4))
	sense_data.append(round(mag["y"], 4))
	sense_data.append(round(mag["z"], 4))
	
	# Accelerometer readings
	sense_data.append(round(acc["x"], 4))
	sense_data.append(round(acc["y"], 4))
	sense_data.append(round(acc["z"], 4))
	
	# Raw gyroscope readings
	sense_data.append(round(gyro["x"], 4))
	sense_data.append(round(gyro["y"], 4))
	sense_data.append(round(gyro["z"], 4))
	
	return sense_data

@app.route('/', methods=['GET'])
def index():
	if request.method== 'GET':
		current_data = get_sense_data()
		return json.dumps(current_data)

@app.route('/header', methods=['GET'])
def header():
	if request.method== 'GET':
		sensehat_header = ['datetime', 'temperature', 'pressure',
							'humidity', 'yaw', 'pitch', 'roll',
							'mag_x', 'mag_y', 'mag_z',
							'acc_x', 'acc_y', 'acc_z', 
							'gyro_x', 'gyro_y', 'gyro_z']
		return json.dumps(sensehat_header)

if __name__ == '__main__':
	app.run(debug=True, host=MY_IP)


