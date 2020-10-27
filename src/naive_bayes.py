import copy
import pandas
import math
from enum import IntEnum

tweets = []


class Sentiments(IntEnum):
    positive = 0
    negative = 1


class NaiveBayes:
    def __init__(self):
        self.total_tweets = 0
        self.tweets_per_sentiment = {label: 0 for label in Sentiments}
        self.word_frequency_per_sentiment = {label: {} for label in Sentiments}
        self.total_unique_words = set()
        self.saved_word_frequency_per_sentiment = {label: {} for label in Sentiments}

    def train(self, tweets):
        self.total_tweets = len(tweets)
        for document in tweets:
            document_content = document[0]
            document_label = document[1]

            self.tweets_per_sentiment[document_label] += 1

            document_content_list = document_content

            vocab_label_dictionary = self.word_frequency_per_sentiment[document_label]

            for word in document_content_list:
                self.total_unique_words.add(word)

                if word in vocab_label_dictionary:
                    vocab_label_dictionary[word] += 1
                else:
                    vocab_label_dictionary[word] = 1

                self.word_frequency_per_sentiment[document_label] = vocab_label_dictionary

        self.saved_word_frequency_per_sentiment = copy.deepcopy(self.word_frequency_per_sentiment)

        for label in self.word_frequency_per_sentiment:
            word_frequency_by_label = sum(self.word_frequency_per_sentiment[label].values())
            for word in self.word_frequency_per_sentiment[label]:
                top = self.word_frequency_per_sentiment[label][word] + 1
                bottom = word_frequency_by_label + (len(self.total_unique_words) + 1)
                self.word_frequency_per_sentiment[label][word] = top / bottom

    def predict(self, x):
        words = x.lower().split()

        estimations = []
        for label in Sentiments:
            word_frequency_by_label = sum(self.saved_word_frequency_per_sentiment[label].values())
            left = math.log10(self.tweets_per_sentiment[label] / self.total_tweets)
            right = 0
            for word in words:
                if word in self.word_frequency_per_sentiment[label]:
                    probability = self.word_frequency_per_sentiment[label][word]
                    right += math.log10(probability)
                else:
                    top = 1
                    bottom = word_frequency_by_label + (len(self.total_unique_words) + 1)
                    right += math.log10(top / bottom)

            max_posteriori_estimate = left + right
            estimations.append(max_posteriori_estimate)

        highest_score_index = estimations.index(max(estimations))

        print(Sentiments(highest_score_index))

        return Sentiments(highest_score_index)

    def load_tweets(self, tweet_data):
        for i, row in tweet_data.iterrows():
            tweet = row['Tweet']
            label = row['Sentiment']

            parsed_tweet = tweet.lower().split()

            if label == 0:
                label = Sentiments(int(1))
            else:
                label = Sentiments(int(0))

            tweets.append((parsed_tweet, label))


nb = NaiveBayes()
tweet_data = pandas.read_csv('../testdata.csv')
nb.load_tweets(tweet_data)
nb.train(tweets)
nb.predict("Hate sick!")
