from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import re
import pandas as pd
import numpy as np
import twitter_credentials
from tweepy import API
from tweepy import Cursor
import json

# # # # TWITTER STREAMER # # # #


def verboseprint(*args, **kwargs): print(*args, **kwargs)


def findurls(d):

    urls = []

    text = str(d['text'])

    if text[0] == 'R' and text[1] == 'T' and text[2] == ' ':
        verboseprint("Retweet", end="\t")

        # finding urls in json twitter response

    if 'extended_tweet'in d:
        if 'entities' in d['extended_tweet']:
            if 'urls' in d['extended_tweet']['entities']:
                for url in d['extended_tweet']['entities']['urls']:
                    if 'expanded_url' in url:
                        urls.append(url['expanded_url'])
                        verboseprint(urls, end="\t")
            else:
                if 'entities' in d:
                    if 'urls' in d['entities']:
                        for url in d['entities']['urls']:
                            urls.append(url['expanded_url'])
                            verboseprint(url['expanded_url'], end="\t")

    pattern = "http\S+"
    '''rls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]),data)'''
    tweettexturls = re.findall(pattern, text)

    print(tweettexturls, end="\t")
    for url in tweettexturls:
        urls.append(url)
    verboseprint('\n')

    return urls


class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = TwitterListener(fetched_tweets_filename)
        auth = OAuthHandler(twitter_credentials.consumer_key,
                            twitter_credentials.consumer_secret)
        auth.set_access_token(twitter_credentials.access_token,
                              twitter_credentials.access_token_secret)
        stream = Stream(auth, listener)
        # This line filter Twitter Streams to capture data by the keywords:
        stream.filter(track=hash_tag_list,)


# # # # TWITTER STREAM LISTENER # # # #
class TwitterListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        # print(data)
        try:
            objects = data.splitlines()
            for line in objects:
                d = json.loads(line)
            

            # confirming pattern whether the tweet has a technical event info
            pattern = "(event|events|Register|RSVP|tickets|conference|conferences|tickets)"

            text = str(d['text'])
            if bool(re.search(pattern,text)):
                urls = findurls(d, urls)
                with open('./urls.txt', 'a') as tf:
                    if(urls):
                        for url in urls:
                            tf.write((url))
                            tf.write('\n')
        
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            

            return True
        except IndexError as e:
            print("No urls in Extended Tweets")
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            # Returning False on_data method in case rate limit occurs.
            return False
        print(status)


class TweetAnalyzer():
    'To Analize the tweets'
    pass


if __name__ == '__main__':

    # Authenticate using config.py and connect to Twitter Streaming API.
    """ hash_tag_list = ["Tech conference","tech conference","Pyconindia2019","pyconindia2019","#ServerlessDays"] """
    hash_tag_list = ["Python events", "hellorubyworld", "railsgirls",
                     "CodeFirstGirls", "WWCodeLondon", "tasomaniac", "ClaventEvents", "#Testcon2019", "POST/CON", "MSFTReactor", "RedHat", "rxjslive", "typescript", "TheDevConf", "Azure", "gophercon", "GOTOcph", "css","AndroidDev",'Python','AWS','Java','Sql',"#ServerlessDays","AWS_edu","droidcon"]
    fetched_tweets_filename = "tweets.txt"
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
    twitter_data = TwitterListener(fetched_tweets_filename)
    tweets = twitter_data.on_data()
