import csv
import twitterbox.db_c as db


class TwitterBoxSearchResult:
	def __init__(self, TweepySearchResult):
		self.box = TweepySearchResult
        
	def savebox(self):
		ret = db.save(self.box)
		return ret
    
	def export_to_csv(self, path):
		try:
			with open(path, 'w') as csvfile:
				spamwriter = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
				cnt = 1
				for i in self.box:
					i.text = ' '.join(i.text.split('\t'))
					spamwriter.writerow([cnt, i.text, i.created_at, i.user.name])
					cnt += 1
			return 1
		except Error as e:
			print(e)
			return 0
