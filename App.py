!pip install tweepy
!pip install flair
bearer = "AAAAAAAAAAAAAAAAAAAAAPyV2wEAAAAAAZpKcIg0%2BdMsKqKtU0yMAouORHs%3DPPQRtMfZTZoBbAKjVZOKSybzh5W0Zcifsfdwmdd7uV60GsDgKk"
consumer_key = "v7VX576awE5PVLOtQv5P9WMbi"
consumer_secret = "4VSXwTXmIbvS8HodwrwdX9ajnhtPvkEPZ1czQUmP9AYCXkSqyV"
access_token = "1940851721909293060-3sqBFFpB1qr735YYJf13UFZLL18oI1"
access_token_secret = "RFFkEVRSFdZikpEkAScu6zzHKQY4edxzi2KMd1KSoEuWR"
## import modules
import tweepy
import re
import time
from flair.models import TextClassifier
from flair.data import Sentence
api = tweepy.Client(bearer,consumer_key,consumer_secret,access_token,access_token_secret)
api.get_me()
response = api.search_recent_tweets('#crypto')
tweets = response.data
for tweet in tweets:
  print(tweet.text)
  print('---------------------------------------------')
tweet .text
preprocess_text(tweet.text)
classifier = TextClassifier.load('en-sentiment')
def get_sentiment(tweet):
    sentence = Sentence(tweet)
    classifier.predict(sentence)
    return str(sentence.labels).split("\'")[3]
get_sentiment(tweet.text)
def preprocess_text(text):
  # convert to the lowercase
  text = text.lower()
  # remove user handle
  text = re.sub("@[\w]*","",text)
  ## remove http links
  text = re.sub("http\S+","",text)
  # remove digits and spl characters
  text = re.sub("[^a-zA-Z#]"," ",text)
  # remove rt characters
  text = re.sub("rt","",text)
  # remove additional spaces
  text = re.sub("\s+"," ",text)
  return text
### create sentiment analyzer function
classifier = TextClassifier.load('en-sentiment')
def get_sentiment(tweet):
    sentence = Sentence(tweet)
    classifier.predict(sentence)
    return str(sentence.labels).split("\'")[3]

import re
import time
import tweepy
from flair.models import TextClassifier
from flair.data import Sentence

# Import the exception
from tweepy.errors import TooManyRequests

# Preprocessing
def preprocess_text(text):
    text = text.lower()
    text = re.sub("@[\w]*", "", text)
    text = re.sub("http\S+", "", text)
    text = re.sub("[^a-zA-Z#]", " ", text)
    text = re.sub("rt", "", text)
    text = re.sub("\s+", " ", text)
    return text

# Sentiment model load
classifier = TextClassifier.load('en-sentiment')
def get_sentiment(tweet):
    sentence = Sentence(tweet)
    classifier.predict(sentence)
    return str(sentence.labels).split("'")[3]

# Use wait_on_rate_limit if using Api or Client init
# api = tweepy.Client(..., wait_on_rate_limit=True)  # for v2 client

while True:
    try:
        tweets = api.search_recent_tweets('#crypto', max_results=10).data or []
        for tweet in tweets:
            clean = preprocess_text(tweet.text)
            sentiment = get_sentiment(clean)
            print('- Tweet:', tweet.text)
            print('  Sentiment ➝', sentiment)

        time.sleep(10)  # gentle pacing between batches

    except TooManyRequests as e:
        # Use reset time from header to wait until reset
        reset_ts = int(e.response.headers.get("x-rate-limit-reset", time.time() + 60))
        wait = max(reset_ts - time.time(), 0) + 5
        print(f"➤ Rate limit hit. Sleeping for {int(wait)} seconds…")
        time.sleep(wait)
        continue
