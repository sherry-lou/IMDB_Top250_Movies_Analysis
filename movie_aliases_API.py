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

def _import_basic_movie_info_from_csv(path):
    table_name = 'movie_aliases'
    conn = sqlite3.connect('top_250_movies.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()
    # create the table
    cur.execute('DROP TABLE IF EXISTS ' + table_name)
    cur.execute('CREATE TABLE ' + table_name + ' (imdb_id TEXT, alias TEXT)')

    file = open(path)

    csvreader = csv.reader(file)

    index = 0
    for row in csvreader:
        if index == 0:
            index += 1
            continue
        imdb_id = row[0]
        alias = row[1]
        cur.execute('INSERT INTO ' + table_name +' VALUES (?, ?)', (imdb_id, alias))

    conn.commit()
    conn.close()

# output basic movie information above into a csv
def _writeToDB(storeAll, numRows):
    table_name = 'movie_aliases'
    conn = sqlite3.connect('top_250_movies.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()

    # create the table
    cur.execute('DROP TABLE IF EXISTS ' + table_name)
    cur.execute('CREATE TABLE ' + table_name + ' (imdb_id TEXT, alias TEXT)')

    # define the dataset
    imdb_id_list = _get_imdb_id_list()

    index = 0
    for imdb_id in imdb_id_list:
        if index == numRows and not storeAll:
            break
        url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"

        querystring = {"type":"get-movies-aliases-by-imdb","imdb":imdb_id}

        headers = {
            'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com",
            'x-rapidapi-key': "2528740c4dmsh7e3200af218df77p15441ajsna362d5da378e"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        result = json.loads(response.text)['aliases']
        
        for alias in result:
            cur.execute('INSERT INTO ' + table_name +' VALUES (?, ?)', (imdb_id, alias))
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


# # write a new file with movie aliases information using API
# def output_movie_aliases_to_csv():
#     imdb_id_list = get_imdb_id_list()
    
#     filewrite = open('movie-aliases.csv', 'w')
#     header_list = ['imdb_id','alias']
#     for header in header_list:
#         filewrite.write(header + ',')    
#     filewrite.write('\n')
    
#     for imdb in imdb_id_list:
#         url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"

#         querystring = {"type":"get-movies-aliases-by-imdb","imdb":imdb}

#         headers = {
#             'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com",
#             'x-rapidapi-key': "2528740c4dmsh7e3200af218df77p15441ajsna362d5da378e"
#             }

#         response = requests.request("GET", url, headers=headers, params=querystring)
#         result = json.loads(response.text)['aliases']
        
#         for alias in result:
#             filewrite.write(imdb + ',')
#             filewrite.write('"{}"'.format(alias) + ',')
#             filewrite.write('\n')
    
#     filewrite.close()
#     return filewrite