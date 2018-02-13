import operator
import tweepy as tp
import importlib
import csv
from configparser import ConfigParser
import twitterbox.db_c as db
import os
from twitterbox.models import QueryLine
from twitterbox.models import QueryBox
from twitterbox.models.SearchBox import TwitterBoxSearchResult



class TwitterBoxQuery:
	def __init__(self):
		self.pointer = 1
        
	def get_next(self, line=1):
		res = db.get_tweets(self.pointer, self.pointer+line)
		self.pointer = self.pointer+line
		return res
    
	def reset_pointer(self, position=1):
		self.pointer = position
        
class TwitterBoxSearch:
	def __init__(self, ret = {}):
		if ret == {}:
			ret = self._read_auth()
		self.auth = tp.OAuthHandler(ret['api_key'], ret['api_secret'])
		self.auth.set_access_token(ret['access_token'], ret['access_token_secret'])
		self.api = tp.API(self.auth)
    
	def _read_auth(self):
		section='auth'
		filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
		parser = ConfigParser()
		parser.read(filename)
		db = {}
		if parser.has_section(section):
			items = parser.items(section)
			for item in items:
				db[item[0]] = item[1]
		else:
			raise Exception('{0} not found in {1} file'.format(section, filename))
		return db

	def search(self, query, max_count = 10):
		results = TwitterBoxSearchResult(self.api.search(query, count=max_count))
		return results
    
	def trending(self, trends_count = 1):
		out = self.api.trends_place(trends_count)
		data = out[0]
		trends = data['trends']
		names = [trend['name'] for trend in trends]
		return names

def configure_database(host, database, user, password):
	config = ConfigParser()
	filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
	config.read(filename)
	config.set('mysql', 'host', str(host))
	config.set('mysql', 'database', str(database))
	config.set('mysql', 'user', str(user))
	config.set('mysql', 'password', str(password))
	with open(filename, 'w') as configfile:
		config.write(configfile)

def configure_twitter_authentication(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
	config = ConfigParser()
	filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
	config.read(filename)
	config.set('auth', 'api_key', str(API_KEY))
	config.set('auth', 'api_secret', str(API_SECRET))
	config.set('auth', 'access_token', str(ACCESS_TOKEN))
	config.set('auth', 'access_token_secret', str(ACCESS_TOKEN_SECRET))
	with open(filename, 'w') as configfile:
		config.write(configfile)

def initialise_database():
	return db.initialise_database()

def reinitialise_database():
	return db.reinitialise_database()