import json
import tweepy
import time
import pandas

auth = tweepy.OAuthHandler("zjsCZArKGXIjdljnUKRCn0VJb",
                           "JdSahiGrK2bCvnBFIHnpetLS9DW4F1b6ehN2iIWP5PIIQomFx9")

auth.set_access_token("1315844267265454080-pV8Xm8ITDEpjjb1eqyFedgxMq20yj3",
                      "WmmDZILW1xPmNArqay88XhUgRdzidvhnkSt9scF3dZNeS")

api = tweepy.API(auth, wait_on_rate_limit=True)

output_directory = './tweet_repository'


def grab_tweets(institution, handle):
    response = []
    query_string = '(to:{handle} OR @{handle}) lang:en -filter:links'.format(handle=handle)

    for page in tweepy.Cursor(api.search, q=query_string, count=100, tweet_mode='extended').pages(5):
        response = response + page

    tweets = []
    for tweet in response:
        json_parsed = json.loads(json.dumps(tweet._json))
        tweets.append(json_parsed)

    export_tweets(institution, tweets)

    print('Finished grabbing tweets for %s...' % institution)

    time.sleep(3)


def export_tweets(institution, tweets):
    institution = institution.lower().replace(' ', '_')
    output_file_name = output_directory + '/' + '{institution}.csv'.format(institution=institution)

    dataframe = pandas.json_normalize(tweets)

    headers = ['created_at', 'full_text', 'id_str']
    dataframe.to_csv(output_file_name, columns=headers)


def handle_institution(institution_dataframe):
    for i, row in institution_dataframe.iterrows():
        institution = row['Institution']
        handle = row['Handle']
        grab_tweets(institution, handle)


institution_dataframe = pandas.read_csv('institutions_twitter.csv', usecols=[2, 3])
handle_institution(institution_dataframe)
