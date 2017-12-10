#!/usr/bin/env python
import os
import tweepy
from datetime import datetime

# Create variables for each key, secret, token
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_SECRET']

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
f = open(os.environ['HTML_REPORT'],'w')
f.write('<html><head><style>table, th, td {border: 1px solid black;}</style><table width="100%"></style></head><body>\n')

for tweet in public_tweets:
  f.write('<tr><td><br>{}<hr></td></tr>\n'.format(tweet.text.encode('utf-8')))

f.write('</table></body></html>')
f.close()
    
# Write a tweet to push to our Twitter account
tweet = 'Hello, world! The time now is {}'.format(datetime.now().time())
api.update_status(status=tweet)
