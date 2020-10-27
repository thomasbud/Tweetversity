import pandas

from src.naive_bayes import NaiveBayes
from src.naive_bayes import Sentiments

tweet_data = pandas.read_csv('../testdata.csv')

nb = NaiveBayes()
nb.load_tweets(tweet_data)
tweets = nb.tweets
nb.train()

test_data = pandas.read_csv('../tweet_repository/albany_medical_college.csv')
positive = 0
negative = 0
total = 0

for i, row in test_data.iterrows():
    tweet = row['full_text']
    total += 1
    sentiment = nb.predict(tweet)
    if sentiment == Sentiments(0):
        positive += 1
    elif sentiment == Sentiments(1):
        negative += 1

print("people find this university ", (positive / total) * 100, "% happy")
