class QueryLine:
	def __init__(self, id = -1, tweet = '', date = '', user=''):
		self.tweet = str(tweet)
		self.date = str(date)
		self.id = str(id)
		self.user = str(user)
	def __repr__(self):
		return '[' + self.id + ' | ' + self.tweet + ' | ' + self.date + ' | ' + self.user +']'

	def __lt__(self, other):
		return self.date < other.date

	def list(self):
		l = [self.id, self.tweet, self.date, self.user]
		return l