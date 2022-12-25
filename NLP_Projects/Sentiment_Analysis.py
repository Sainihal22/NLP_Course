# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 10:35:53 2022

@author: saini
"""

# import nltk
# nltk.downloader.download('vader_lexicon')

# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import emoji

text = 'I love Python ❤️, it is brilliant 👍'
emoji.demojize(text )

# function to print sentiments
# of the sentence.
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

    print("Sentence Overall Rated As", end = " ")

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")

    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negative")

    else :
        print("Neutral")

def demojize(text):
  text=emoji.demojize(text)
  return text



# Driver code
if __name__ == "__main__" :

    print("\n1st statement :")
    sentence = "This product is 😘."
    sentence = demojize(sentence)
    print(sentence)

    # # function calling
    sentiment_scores(sentence)

    # print("\n2nd Statement :")
    sentence = "This product is 🤬."
    sentence = demojize(sentence)
    print(sentence)

    # # function calling
    sentiment_scores(sentence)
    # sentiment_scores(sentence)

    # print("\n3rd Statement :")
    # sentence = "This product is 🙂."
    # sentiment_scores(sentence)
