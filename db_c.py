import os

import mysql.connector
from mysql.connector import Error
from configparser import ConfigParser

from twitterbox.models.QueryBox import QueryBox 
from twitterbox.models.QueryLine import QueryLine 

def read_con():
	section='mysql'
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

def connect():
	db_config = read_con()
	conn = mysql.connector.connect(**db_config)
	return conn

def save(box):
	try:
		conn = connect()		
		cursor = conn.cursor()
		for i in box:
			str_date = str(i.created_at)
			str_text = str(i.text)
			str_user = str(i.user.name)
			query = "INSERT INTO Tweets (tweet, date, user) VALUES(%s, %s, %s)"
			args = (str_text, str_date, str_user)
			cursor.execute(query, args)
		conn.commit()
		return 1
	except Error as e:
		return 0
	finally:
		cursor.close()
		conn.close()
	return 1

def get_tweets(start_index, end_index):
	result_box = QueryBox()
	result_box.reset()
	try:
		conn = connect()
		cursor = conn.cursor()
		# query = 
		args = (int(start_index), int(end_index))
		print(start_index, end_index)
		cursor.execute("SELECT * FROM Tweets WHERE id >= %s AND id < %s", (start_index, end_index))
		row = cursor.fetchone()
		while row is not None:
			result_box.append(QueryLine(row[0], row[1], row[2], row[3]))
			row = cursor.fetchone()
	except Error as e:
		print(e)
		return None
	finally:
		cursor.close()
		conn.close()
	return result_box

if '__init__' == '__main__':
	import models.QueryLine as QueryLine
	import models.QueryBox as QueryBox