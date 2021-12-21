import requests
import json
import sys
import csv
import sqlite3

def func1():
    _writeToDB(True, -1)

def func2():
    _writeToDB(False, 5)

def func3(path):
    _import_basic_movie_info_from_csv(path)

# import the intermediate csv file on basic info on top 250 movies and put the imdb id into a list
def _get_imdb_id_list():
    fileread = open('data/top-250-movies-basic-info.csv').read().splitlines()

    # put all imdb_id into a list
    imdb_id_list = []
    for line in fileread[1:]:
        imdb_id_list.append(line.split(',')[1])
    return imdb_id_list

# # write a new file with movie information using API
# def output_more_movies_info_to_csv():
#     imdb_id_list = _get_imdb_id_list()
    
#     filewrite = open('more-movies-info.csv', 'w')
#     header_list = ['imdb_id','movie name','year','release time','runtime','genre','language','country','awards','box office']
#     for header in header_list:
#         filewrite.write(header + ',')
#     filewrite.write('\n')

#     for imdb in imdb_id_list:
#         url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

#         querystring = {"r":"json","i":imdb}

#         headers = {
#             'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
#             'x-rapidapi-key': "2528740c4dmsh7e3200af218df77p15441ajsna362d5da378e"
#             }

#         response = requests.request("GET", url, headers=headers, params=querystring)
#         result = json.loads(response.text)

#         filewrite.write(imdb + ',')
#         filewrite.write('"{}"'.format(result['Title']) + ',')
#         filewrite.write('"{}"'.format(result['Year']) + ',')
#         filewrite.write('"{}"'.format(result['Released']) + ',')
#         filewrite.write('"{}"'.format(result['Runtime']) + ',')
#         filewrite.write('"{}"'.format(result['Genre']) + ',')
#         filewrite.write('"{}"'.format(result['Language']) + ',')
#         filewrite.write('"{}"'.format(result['Country']) + ',')
#         filewrite.write('"{}"'.format(result['Awards']) + ',')
#         filewrite.write('"{}"'.format(result['BoxOffice']) + ',')
#         filewrite.write('\n')
#     filewrite.close()
#     return filewrite

def _import_basic_movie_info_from_csv(path):
    table_name = 'more_movies_info'
    conn = sqlite3.connect('top_250_movies.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()
    # create the table
    cur.execute('DROP TABLE IF EXISTS ' + table_name)
    cur.execute('CREATE TABLE ' + table_name + ' (imdb_id TEXT, movie_name TEXT, year INTEGER, release_time TEXT, runtime INTEGER, genre TEXT, language TEXT, country TEXT, awards TEXT, box_office REAL)')

    file = open(path)

    csvreader = csv.reader(file)

    index = 0
    for row in csvreader:
        if index == 0:
            index += 1
            continue
        imdb_id = row[0]
        movie_name = row[1]
        year = row[2]
        release_time = row[3]
        runtime = row[4].split()[0]
        genre = row[5]
        language = row[6]
        country = row[7]
        awards = row[8]
        box_office = row[9].replace(',', '').replace('$', '')
        cur.execute('INSERT INTO ' + table_name +' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (imdb_id, movie_name, year, 
            release_time, runtime, genre, language, country, awards, box_office))
    
    conn.commit()
    conn.close()

# output basic movie information above into a csv
def _writeToDB(storeAll, numRows):
    table_name = 'more_movies_info'
    conn = sqlite3.connect('top_250_movies.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()

    # create the table
    cur.execute('DROP TABLE IF EXISTS ' + table_name)
    cur.execute('CREATE TABLE ' + table_name + ' (imdb_id TEXT, movie_name TEXT, year INTEGER, release_time TEXT, runtime INTEGER, genre TEXT, language TEXT, country TEXT, awards TEXT, box_office REAL)')

    # define the dataset
    imdb_id_list = _get_imdb_id_list()

    index = 0
    for imdb_id in imdb_id_list:
        if index == numRows and not storeAll:
            break
        url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

        querystring = {"r":"json","i":imdb_id}

        headers = {
            'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
            'x-rapidapi-key': "2528740c4dmsh7e3200af218df77p15441ajsna362d5da378e"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        result = json.loads(response.text)

        movie_name = result['Title']
        year = result['Year']
        release_time = result['Released']
        runtime = result['Runtime'].split()[0]
        genre = result['Genre']
        language = result['Language']
        country = result['Country']
        awards = result['Awards']
        box_office = result['BoxOffice'].replace(',', '').replace('$', '')
        cur.execute('INSERT INTO ' + table_name +' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (imdb_id, movie_name, year, 
            release_time, runtime, genre, language, country, awards, box_office))
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