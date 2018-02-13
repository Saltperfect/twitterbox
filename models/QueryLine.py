class QueryLine:
	def __init__(self, id = -1, tweet = '', date = '', user='', retweet=0, likes=0):
		self.tweet = str(tweet)
		self.date = str(date)
		self.id = str(id)
		self.user = str(user)
		self.retweets = int(retweet)
		self.likes = int(likes)
	def __repr__(self):
		return '[' + self.id + ' | ' + self.tweet + ' | ' + self.date + ' | ' + self.user + ' | ' + str(self.retweets)  + ' | ' + str(self.likes)  + ']'

	def __lt__(self, other):
		return self.date < other.date

	def list(self):
		l = [self.id, self.tweet, self.date, self.user]
		return l