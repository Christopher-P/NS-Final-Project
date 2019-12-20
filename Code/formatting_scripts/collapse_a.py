from os import listdir
from os.path import isfile, join
import csv

#Set path for where all data be
all_files_path = "C:/Users/chris/Desktop/NS-FinalProject/half_data_a"

#Get all files names in that directory
data_files = [f for f in listdir(all_files_path) if isfile(join(all_files_path, f))]

#set of user_ids
user_ids = set()

for file_name in data_files:
	user_ids.add(file_name[:-4])
	with open(all_files_path + "/" + file_name, 'r') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', )
		for row in spamreader:
			user_ids.add(row[2])
			#print(row)
	

with open('user_ids.csv', 'w', newline='') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',')
	for i in user_ids:
		#filter out bad user_ids
		if (i == "user_id" or int(i) > 325000000):
			continue
			
		spamwriter.writerow([i])