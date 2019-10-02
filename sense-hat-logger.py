from sense_hat import SenseHat
from datetime import datetime
from csv import writer
import csv
import json

CSV_DATA_FILE = 'data-file.csv'

sense = SenseHat()
sense.clear()

timestamp = datetime.now()
delay = 1

def get_sense_data():
	sense_data = []
	orientation = sense.get_orientation()
	mag = sense.get_compass_raw()
	acc = sense.get_accelerometer_raw()
	gyro = sense.get_gyroscope_raw()
	
	# DateTime
	sense_data.append(datetime.now())
	
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



with open(CSV_DATA_FILE, 'w', newline='') as f:
	data_writer = writer(f)
	data_writer.writerow(['datetime', 'temperature', 'pressure',
							'humidity', 'yaw', 'pitch', 'roll',
							'mag_x', 'mag_y', 'mag_z',
							'acc_x', 'acc_y', 'acc_z', 
							'gyro_x', 'gyro_y', 'gyro_z'])
	while True:
		try:
			info = get_sense_data()
			dt = info[0] - timestamp
			if dt.seconds > delay:
				data_writer.writerow(info)
				timestamp = datetime.now()
		except KeyboardInterrupt:
			print('DONE')	
			break
	



	
