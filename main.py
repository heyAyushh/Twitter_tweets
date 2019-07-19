from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import re
import panda as pd
import numpy as np
import twitter_credentials
from tweepy import API
from tweepy import Cursor

# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = TwitterListener(fetched_tweets_filename)
        auth = OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
        auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)
        stream = Stream(auth, listener)
        # This line filter Twitter Streams to capture data by the keywords:
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class TwitterListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            # Returning False on_data method in case rate limit occurs.
            return False
        print(status)

    def on_error(self, status):
        print(status)

class TweetAnalyzer():
    'To Analize the tweets'
    pass
if __name__ == '__main__':

    # Authenticate using config.py and connect to Twitter Streaming API.
    # hash_tag_list = ['Python','AWS','Azure','Java','Sql']
    # fetched_tweets_filename = "tweets.txt"
    #
    # twitter_streamer = TwitterStreamer()
    # twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
    twitter_data = TwitterListener()
    tweets = twitter_data.on_data()