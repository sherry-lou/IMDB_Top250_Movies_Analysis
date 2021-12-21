import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import sqlite3
import csv

def func1():
	_writeToDB(True, -1)

def func2():
	_writeToDB(False, 5)

def func3(path):
	_import_basic_movie_info_from_csv(path)

# access the top 250 ranked movies by IMDB's rating using BeautifulSoup
def get_page_url():
	page = urlopen("http://www.imdb.com/chart/top")
	soup = BeautifulSoup(page, "html.parser")
	return soup

 # extract useful information into lists
def get_movie_links():
	soup = get_page_url()
	movie_links = []
	for movie in soup.select('td.titleColumn a'):
		movie_links.append(movie.attrs.get('href'))
	return movie_links

def get_imdb_id():
	movie_links = get_movie_links()
	imdb_id = []
	for id in movie_links:
		imdb_id.append(id.split('/')[2])
	return imdb_id

def get_entire_cast():
	soup = get_page_url()
	entire_cast = []
	for cast in soup.select('td.titleColumn a'):
		entire_cast.append(''.join(cast.attrs.get('title')))
	return entire_cast

def get_directors():
	soup = get_page_url()
	directors = []
	for director in soup.select('td.titleColumn a'):
		directors.append(director.attrs.get('title').split(',')[0])
	return directors

def get_actors():
	entire_cast = get_entire_cast()
	actors = []
	for actor in entire_cast:
		actor = ','.join(actor.split(',')[1:]).strip()
		actors.append(actor)
	return actors

def get_ratings():
	soup = get_page_url()
	ratings = []
	for rating in soup.select('td.posterColumn span[name=ir]'):
		ratings.append(rating.get('data-value'))
	return ratings

# # output basic movie information above into a csv
# def output_basic_movie_info_to_csv():
# 	filewrite = open("top-250-movies-basic-info.csv", 'w')

# 	# write the header into an output csv
# 	header_list = ['ranking','imdb_id','director','actor 1','actior 2','rating']
# 	for header in header_list:
# 		filewrite.write(header + ',')
# 	filewrite.write('\n')
	
# 	imdb_id = get_imdb_id()
# 	directors = get_directors()
# 	actors = get_actors()
# 	ratings = get_ratings()
	
# 	index = 0
# 	for index in range(len(imdb_id)):
		
# 		index_list = []
# 		index_list.append(str(index+1))
# 		index_list.append(imdb_id[index])
# 		index_list.append(directors[index])
# 		index_list.append(actors[index])
# 		index_list.append(ratings[index])
		
# 		for i in index_list:
# 			filewrite.write(i + ',')
# 		filewrite.write('\n')
		
# 		index += 1
	
# 	filewrite.close()
# 	return filewrite

def _import_basic_movie_info_from_csv(path):
	table_name = 'top_250_movies_basic_info'
	conn = sqlite3.connect('top_250_movies.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
	cur = conn.cursor()
	# create the table
	cur.execute('DROP TABLE IF EXISTS ' + table_name)
	cur.execute('CREATE TABLE ' + table_name + ' (ranking INTEGER, imdb_id TEXT, director TEXT, actor1 TEXT, actor2 TEXT, rating REAL)')

	file = open(path)

	csvreader = csv.reader(file)

	index = 0
	for row in csvreader:
		if index == 0:
			index += 1
			continue
		ranking = row[0]
		imdb_id = row[1]
		director = row[2]
		actor1 = row[3]
		actor2 = row[4]
		rating = row[5]
		cur.execute('INSERT INTO ' + table_name +' VALUES (?, ?, ?, ?, ?, ?)', (ranking, imdb_id, director, actor1, actor2, rating))
	
	conn.commit()
	conn.close()

# output basic movie information above into a csv
def _writeToDB(storeAll, numRows):
	table_name = 'top_250_movies_basic_info'
	conn = sqlite3.connect('top_250_movies.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
	cur = conn.cursor()
	
	# create the table
	cur.execute('DROP TABLE IF EXISTS ' + table_name)
	cur.execute('CREATE TABLE ' + table_name + ' (ranking INTEGER, imdb_id TEXT, director TEXT, actor1 TEXT, actor2 TEXT, rating REAL)')

	# define the dataset
	imdb_id = get_imdb_id()
	directors = get_directors()
	actors = get_actors()
	ratings = get_ratings()
	
	index = 0
	for index in range(len(imdb_id)):
		if index == numRows and not storeAll:
			break
		_actors = actors[index].split(",")

		cur.execute('INSERT INTO ' + table_name +' VALUES (?, ?, ?, ?, ?, ?)', (str(index + 1), imdb_id[index], directors[index], _actors[0].strip(), _actors[1].strip(), ratings[index]))

		index += 1

	conn.commit()
	conn.close()

if __name__ == '__main__':
	if len(sys.argv) == 1:
		func1()
	elif len(sys.argv) == 2:
		func2()
	else:
		func3(sys.argv[2])