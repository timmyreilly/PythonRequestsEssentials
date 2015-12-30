from tokens import *

import requests
from requests_oauthlib import OAuth1

auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

favorite_tweet = requests.get('https://api.twitter.com/1.1/favorites/list.json?count=1', auth=auth)


print favorite_tweet.json()

# Searching twitter

search_results = requests.get('https://api.twitter.com/1.1/search/tweets.json?q=%python', auth=auth) 

search_results.json().keys()

search_results.json()["search_metadata"]

# getting followers

followers = requests.get('https://api.twitter.com/1.1/followers/list.json', auth=auth)

followers.json().keys()

followers.json()["users"]

# retweets

retweets = requests.get('https://api.twitter.com/1.1/statuses/retweets_of_me.json', auth=auth)

len(retweets.json())

retweets.json()[0]

# trends

available_trends = requests.get('https://api.twitter.com/1.1/trends/available.json', auth=auth)

len(available_trends.json())

available_trends.json()[10]


# posting a tweet!

# requests.post('https://api.twitter.com/1.1/statuses/update.json?status=Happy%to%help', auth=auth)


# FACEBOOK = Struggle with OAuth

# on to reddit

search = requests.get('http://reddit.com/search.json', params={'q': 'python'}) 

subreddit_search = requests.get('http://www.reddit.com/subreddits/search.json', params={'q': 'python'})



'''
types of data in the web
Structured Data
Unstructured data
Semistructured Data
'''

R