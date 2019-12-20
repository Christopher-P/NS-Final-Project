#https://github.com/nagypeterjob/Sentiment-Analysis-NLTK-ML-LSTM

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from keras.models import load_model
import re
import copy

model = load_model('trained.h5')

names = ["obama.csv", "bernie.csv", "clinton.csv", "spencer.csv", "trump.csv", "tucker.csv", "waters.csv"]

for j in names:

	data = pd.read_csv(j)
	# Keeping only the neccessary columns
	data = data[['text']]

	data['text'] = data['text'].apply(lambda x: x.lower())
	data['text'] = data['text'].apply((lambda x: re.sub('[^a-zA-z0-9\s]','',x)))

	for idx,row in data.iterrows():
		row[0] = row[0].replace('rt',' ')
		
	max_fatures = 5000
	tokenizer = Tokenizer(nb_words=max_fatures, split=' ')
	tokenizer.fit_on_texts(data['text'].values)
	X = tokenizer.texts_to_sequences(data['text'].values)
	X = pad_sequences(X)

	X = np.resize(X, (len(X), 57))


	results = model.predict(X)

	total = len(results)
	count = 0


	for i in results:
		if(i[0] > i[1]):
			count = count - 1
		else:
			count = count + 1
			
	print(j)
	print(count/total)
