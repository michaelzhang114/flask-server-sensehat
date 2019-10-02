from flask import Flask, jsonify, request
import csv
import json

JSONFILE = 'sense-hat-data.json'
MY_IP = '10.197.119.190'
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	if request.method== 'GET':
		f = open(JSONFILE, 'r')
		contents = f.read()
		return contents

if __name__ == '__main__':
	app.run(debug=True, host=MY_IP)
