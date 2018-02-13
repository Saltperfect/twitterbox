import csv

class QueryBox:
	def __init__(self, QueryLineList = []):
		self.box = QueryLineList
	
	def append(self, QueryLine):
		self.box.append(QueryLine)
	
	def __repr__(self):
		return '<QueryBox Object>\n' + self.box.__repr__()

	def reset(self):
		self.box = []
	
	def search_by_text(self, query):
		results = QueryBox()
		results.reset()
		for i in self.box:
			print(type(i))
			if i.tweet.find(query) != -1:
				results.append(i)
		return results

	def search_by_date(self, date):
		results = QueryBox()
		results.reset()
		for i in self.box:
			if i.date.find(date) != -1:
				results.append(i)
		return results

	def sort(self):
		results = QueryBox()
		results.reset()
		results.box = self.box
		results.box.sort()
		return results
	
	def export_to_csv(self, path):
		try:
			with open(path, 'w') as csvfile:
				spamwriter = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
				for i in self.box:
					i.tweet = ' '.join(i.tweet.split('\t'))
					spamwriter.writerow(i.list())
			return 1
		except Error as e:
			print(e)
			return 0
	def __getitem__(self, index):
		return self.box[index]

