import csv
import json

CSVFILE = 'data-file.csv'
JSONFILE = 'sense-hat-data.json'

jsonfile = open(JSONFILE, 'w')

with open(CSVFILE) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		json.dump(row, jsonfile)
		jsonfile.write('\n')

