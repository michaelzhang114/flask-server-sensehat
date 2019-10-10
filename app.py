from sense_hat import SenseHat
from flask import Flask, jsonify, request
from datetime import datetime
import csv
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
	sense_data.append(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
	
	# Environmental sensors
	sense_data.append(sense.get_temperature())
	sense_data.append(sense.get_pressure())
	sense_data.append(sense.get_humidity())
	
	# Orientation
	sense_data.append(orientation["yaw"])
	sense_data.append(orientation["pitch"])
	sense_data.append(orientation["roll"])
	
	# Raw compass readings
	sense_data.append(mag["x"])
	sense_data.append(mag["y"])
	sense_data.append(mag["z"])
	
	# Accelerometer readings
	sense_data.append(acc["x"])
	sense_data.append(acc["y"])
	sense_data.append(acc["z"])
	
	# Raw gyroscope readings
	sense_data.append(gyro["x"])
	sense_data.append(gyro["y"])
	sense_data.append(gyro["z"])
	
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


