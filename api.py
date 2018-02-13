import operator
import tweepy as tp
import importlib
import csv

import twitterbox.db_c as db
from twitterbox.models import QueryLine
from twitterbox.models import QueryBox
from twitterbox.models.SearchBox import TwitterBoxSearchResult

from twitterbox.tools.twitter_authentication import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


class TwitterBoxQuery:
	def __init__(self):
		self.pointer = 1
        
	def get_next(self, line=1):
		res = db.get_tweets(self.pointer, self.pointer+line)
		self.pointer = self.pointer+line
		print(self.pointer)
		return res
    
	def reset_pointer(self, position=1):
		self.pointer = position
        
class TwitterBoxSearch:
	def __init__(self):
		self.auth = tp.OAuthHandler(API_KEY, API_SECRET)
		self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		self.api = tp.API(self.auth)
    
	def search(self, query, max_count = 10):
		results = TwitterBoxSearchResult(self.api.search(query, count=max_count))
		return results
    
	def trending(self, trends_count = 1):
		out = self.api.trends_place(trends_count)
		data = out[0]
		trends = data['trends']
		names = [trend['name'] for trend in trends]
		return names

    