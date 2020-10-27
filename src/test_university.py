from naive_bayes import NaiveBayes
import pandas
from naive_bayes import *

def main():
    nb = NaiveBayes()
    tweet_data = pandas.read_csv('../testdata.csv')
    nb.load_tweets(tweet_data)
    tweets = naive_bayes.tweets
    nb.train(tweets)

    test_data = pandas.read_csv('../tweet_repository/texas_a&m_university,_college_station.csv')
    positive = 0
    negative = 0
    total = 0
    for i, row in test_data.iterrows():
        tweet = row['full_text']
        total += 1
        sentiment = nb.predict(tweet)
        if sentiment == "positive":
            positive += 1
        elif sentiment == "negative":
            negative += 1
    print ("people find this university ", positive/total, "% happy")

