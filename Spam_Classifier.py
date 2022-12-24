import pandas as pd

messages = pd.read_csv("SMSSpamCollection",sep="\t",names=["label","message"])

messages

import re
import nltk
nltk.download("stopwords")


from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

lemmatize = WordNetLemmatizer()
# sentences = nltk.sent_tokenize(messages)
corpus = []

for i in range(0,len(messages)):
    review = re.sub('[^a-zA-Z]',' ',messages['message'][i])         # Remove unwanted expressions except a-z and A-Z
    review = review.lower()                               # Lower the sentences
    review = review.split()
    review = [lemmatize.lemmatize(word) for word in review if word not in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
#     print(review)

print(corpus)


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000)
# x = cv.fit_transform(corpus)
x = cv.fit_transform(corpus).toarray()
print(x)

y = pd.get_dummies(messages['label'])
y                                       # if 1 it means that it is that particular category


y = y.iloc[:,1].values

y

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.20,random_state=0)

from sklearn.naive_bayes import MultinomialNB
spam_detect_model = MultinomialNB().fit(X_train,Y_train)

Y_Pred = spam_detect_model.predict(X_test)

Y_Pred

from sklearn.metrics import confusion_matrix
confusion_m = confusion_matrix(Y_test,Y_Pred)

confusion_m

from sklearn.metrics import accuracy_score
acc = accuracy_score(Y_test,Y_Pred)

acc*100