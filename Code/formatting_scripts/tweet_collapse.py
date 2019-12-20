from os import listdir
from os.path import isfile, join
import csv
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

#Set path for where all data be
all_files_path = "C:/Users/chris/Desktop/NS-FinalProject/ML_Part/whole_data_tweet"

#Get all files names in that directory
data_files_pre = [f for f in listdir(all_files_path) if isfile(join(all_files_path, f))]

data_files = []
for i in data_files_pre:
	if i[-10:] == "tweets.csv":
		data_files.append(i)
	
for file_name in data_files:
	print(file_name)
	data = pd.read_csv(all_files_path + "/" + file_name)
	# Keeping only the neccessary columns
	data = data[['text']]
	data.to_csv("C:/Users/chris/Desktop/NS-FinalProject/ML_Part/filtered_whole/" + file_name[:-11] + ".csv", sep=',')
	
	