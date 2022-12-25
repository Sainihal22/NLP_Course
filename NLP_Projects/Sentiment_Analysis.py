# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 10:35:53 2022

@author: saini
"""

# import nltk
# nltk.downloader.download('vader_lexicon')

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import emoji
from nltk.stem import WordNetLemmatizer
# from nltk.corpus import stopwords
# import re

lemmatize = WordNetLemmatizer()

def process_data(sentence):
    
    word = nltk.word_tokenize(sentence)
    print(word)
    print(len(word))
    for i in range(len(word)):
        if(emoji.is_emoji(word[i])):
            word[i] = unicodedata.name(word[i])
            
    sentence = ' '.join(word)
    return sentence

# function to print sentiments of the sentence.
def sentiment_scores(sentence):
    print(sentence)
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
    print("sentence was rated as ", sentiment_dict['compound']*100, "% Compound")

    print("Sentence Overall Rated As", end = " ")

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")

    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negative")

    else :
        print("Neutral")

import unicodedata



# Driver code
if __name__ == "__main__" :

    print("\n1st statement :")
    sentence = "This product is 🙂."
    sentence = process_data(sentence)
    print(sentence)
    sentiment_scores(sentence)

    print("\n2nd Statement :")
    sentence = "This product is very bad."
    sentence = process_data(sentence)
    print(sentence)
    sentiment_scores(sentence)

    print("\n3rd Statement :")
    sentence = "study is going on as usual."
    sentence = process_data(sentence)
    print(sentence)
    sentiment_scores(sentence)