from os import listdir
from os.path import isfile, join

import csv

data_path = 'C:/Users/chris/Desktop/NS-FinalProject/data'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

with open('half_data_b.csv', 'w', newline='') as csvfile:
	spamwriter = csv.writer(csvfile)
	for i in onlyfiles:
		spamwriter.writerow((i[:-4], i))
	
#print(onlyfiles)