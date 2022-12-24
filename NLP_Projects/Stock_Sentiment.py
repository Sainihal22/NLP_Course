# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 19:40:31 2022

@author: saini

1. Remove all the punctuations
2. Lower the data
3. For BOW or TF-IDF we need to make it one paragraph
4. 
"""

import pandas as pd

df = pd.read_csv("C:\\Users\\saini\\Desktop\\Sentiment_Analysis\\NLP\\NLP_Projects\\Data.csv",encoding = "ISO-8859-1")

df.head()

train = df[df['Date'] < '20150101']
test = df[df['Date'] > '20141231']

# Remove Punctuations
data = train.iloc[:,2:27]
data.replace("[^a-zA-Z]", " ", regex = True, inplace = True)

# Renaming column names for ease of access
list1 = [i for i in range(25)]
newindex = [str(i) for i in list1]
data.columns = newindex
data.head(5)

# Converting Headlines in lower case      Always lower the text
for i in newindex:
    data[i] = data[i].str.lower()

data.head(5)

headlines = []
for i in range(0,len(data.index)):
    headlines.append(' '.join(str(x) for x in data.iloc[i,0:25]))     # i is row, 0:25 column

headlines[0]

from sklearn.feature_extraction.text import CountVectorizer      # Takes sentences and converts into a vector of features

# implement Bag Of Words
countvector = CountVectorizer()
traindataset = countvector.fit_transform(headlines)

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier()
rfc.fit(traindataset, train['Label'])

test_transform = []
for i in range(0,len(test.index)):
    test_transform.append(' '.join(str(x) for x in test.iloc[i,0:25]))

test_dataset = countvector.transform(test_transform)
predictions = rfc.predict(test_dataset)

from sklearn.metrics import *