import pandas
import psycopg2
import os
import numpy as np

from psycopg2.extensions import register_adapter, AsIs
from naive_bayes import NaiveBayes
from naive_bayes import Sentiments

psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

# Read csv file
tweet_data = pandas.read_csv('../testdata.csv', encoding='ISO-8859-1')

nb = NaiveBayes()
nb.load_tweets(tweet_data)
tweets = nb.tweets
nb.train()

institutions_data = pandas.read_csv('../institution_repository/institutions_twitter.csv')
ranks = institutions_data['National Rank'].values.astype(int)
institutions = institutions_data['Institution']
counter = 0
id = 1

directory = r'/mnt/c/Users/itspu/Documents/GitHub/tweetversity-backend/tweet_repository'
for entry in os.scandir(directory):
    test_data = pandas.read_csv(entry.path)

    for i, row in test_data.iterrows():
        tweet = row['full_text']
        sentiment = nb.predict(tweet)

        connection = psycopg2.connect(user="ggqqmgjisgeidz",
                                      password="0c1237da000717ebf0fae08a266eb311f44ea8d5e9de8c20360a146178affc4f",
                                      host="ec2-54-156-85-145.compute-1.amazonaws.com",
                                      port="5432",
                                      database="da71hnbr874rn5")
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO sentiments (ID, INSTITUTION, TWEET, SENTIMENT, NATIONAL_RANK) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (id, institutions[counter], tweet, sentiment, ranks[counter])
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()

        id = id + 1
    counter = counter + 1



