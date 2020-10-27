import pandas

from src.naive_bayes import NaiveBayes
from src.naive_bayes import Sentiments

tweet_data = pandas.read_csv('../testdata.csv', encoding='ISO-8859-1')

nb = NaiveBayes()
nb.load_tweets(tweet_data)
tweets = nb.tweets
nb.train()

# Possible university datasets may be found in tweet_repository folder
test_data = pandas.read_csv('../tweet_repository/texas_a&m_university,_college_station.csv')
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
