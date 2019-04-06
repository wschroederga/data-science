import tweepy
from textblob import TextBlob

consumer_key='2LmOKhyOSa7UZPvQ02NMquEpf'
consumer_secret='w6kSwdSbssUWeJdXtNeJnnHXGmy2h3GKMAEP6Gb8RG7fdU425j'

access_token='293000925-A3rWafxzq9md2SO0jG7qOYRKfWmYsVctbFEIeckh'
access_token_secret='N4fIRNb2INz3goKqVxHGUJBYViZudbbfyIT5APGYoh6qr'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
