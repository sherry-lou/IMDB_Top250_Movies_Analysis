import sys
import top_250_movies_web_scraper
import more_movies_info_API
import movie_aliases_API
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def data_analysis():
	conn = sqlite3.connect('top_250_movies.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
	cur = conn.cursor()
	
	# fetch top five rated movies by IMDB users
	cur.execute('''
				SELECT more_movies_info.movie_name, top_250_movies_basic_info.rating, more_movies_info.box_office
				FROM top_250_movies_basic_info
				JOIN more_movies_info
				ON top_250_movies_basic_info.imdb_id = more_movies_info.imdb_id
				JOIN movie_aliases
				ON top_250_movies_basic_info.imdb_id = movie_aliases.imdb_id
				GROUP BY 1
				ORDER BY top_250_movies_basic_info.ranking
				LIMIT 5''')	
	top_five_movies = cur.fetchall()
	print('The top 5 rated movies by IMDB and their rating are: ')
	print('Top 1: ' + top_five_movies[0][0] + ' with rating of ' + str(top_five_movies[0][1]) + ' and box office of ' + '$' + str(top_five_movies[0][2]))
	print('Top 2: ' + top_five_movies[1][0] + ' with rating of ' + str(top_five_movies[1][1]) + ' and box office of ' + '$' + str(top_five_movies[1][2]))
	print('Top 3: ' + top_five_movies[2][0] + ' with rating of ' + str(top_five_movies[2][1]) + ' and box office of ' + '$' + str(top_five_movies[2][2]))
	print('Top 4: ' + top_five_movies[3][0] + ' with rating of ' + str(top_five_movies[3][1]) + ' and box office of ' + '$' + str(top_five_movies[3][2]))
	print('Top 5: ' + top_five_movies[4][0] + ' with rating of ' + str(top_five_movies[4][1]) + ' and box office of ' + '$' + str(top_five_movies[4][2]))

	print('=========================================')

	# rating description of the top 250 movies
	cur.execute('''
				SELECT AVG(rating) as average_rating, MIN(rating) as min_rating, MAX(rating) as max_rating
				FROM top_250_movies_basic_info
				''')	
	rating_des = cur.fetchall()
	print('The average rating of the top 250 movies is ' + str(rating_des[0][0]))
	print('The minimum rating of the top 250 movies is ' + str(rating_des[0][1]))
	print('The maximum rating of the top 250 movies is ' + str(rating_des[0][2]))

	print('=========================================')

	# runtime description of the top 250 movies
	cur.execute('''
				SELECT AVG(runtime) as average_runtime, MIN(runtime) as min_runtime, MAX(runtime) as max_runtime
				FROM more_movies_info
				''')	
	runtime_des = cur.fetchall()
	print('The average runtime of the top 250 movies is ' + str(runtime_des[0][0]) + ' mins.')
	print('The minimum runtime of the top 250 movies is ' + str(runtime_des[0][1]) + ' mins.')
	print('The maximum runtime of the top 250 movies is ' + str(runtime_des[0][2]) + ' mins.')

	print('=========================================')

	# top five directors who have the most movies on the list
	cur.execute('''
				SELECT director, COUNT(*)
				FROM top_250_movies_basic_info
				GROUP BY 1
				ORDER BY 2 DESC, 1 ASC
				LIMIT 5
				''')	
	best_directors = cur.fetchall()
	print('The top five directors who have the most movies on the list are respectively: ')
	print('Top 1: ' + best_directors[0][0] + ' with ' + str(best_directors[0][1]) + ' movies.')
	print('Top 2: ' + best_directors[1][0] + ' with ' + str(best_directors[1][1]) + ' movies.')
	print('Top 3: ' + best_directors[2][0] + ' with ' + str(best_directors[2][1]) + ' movies.')
	print('Top 4: ' + best_directors[3][0] + ' with ' + str(best_directors[3][1]) + ' movies.')
	print('Top 5: ' + best_directors[4][0] + ' with ' + str(best_directors[4][1]) + ' movies.')

	print('=========================================')

	# top five actors who have the most movies on the list
	cur.execute('''
				SELECT actors, SUM(CNT)
				FROM
					(SELECT actor1 AS actors, COUNT(actor1) AS CNT
					FROM top_250_movies_basic_info
					GROUP BY 1
					UNION ALL
					SELECT actor2 AS actors, COUNT(actor2) AS CNT
					FROM top_250_movies_basic_info
					GROUP BY 1)
				GROUP BY 1
				ORDER BY 2 DESC
				LIMIT 5
				''')	
	best_actors = cur.fetchall()
	print('The top five actors who have the most movies on the list are respectively: ')
	print('Top 1: ' + best_actors[0][0] + ' with ' + str(best_actors[0][1]) + ' movies.')
	print('Top 2: ' + best_actors[1][0] + ' with ' + str(best_actors[1][1]) + ' movies.')
	print('Top 3: ' + best_actors[2][0] + ' with ' + str(best_actors[2][1]) + ' movies.')
	print('Top 4: ' + best_actors[3][0] + ' with ' + str(best_actors[3][1]) + ' movies.')
	print('Top 5: ' + best_actors[4][0] + ' with ' + str(best_actors[4][1]) + ' movies.')

	print('=========================================')

	# most popular movies around the world -> most number of aliases
	cur.execute('''
				SELECT more_movies_info.movie_name, COUNT(alias)
				FROM more_movies_info
				JOIN movie_aliases
				ON more_movies_info.imdb_id = movie_aliases.imdb_id
				GROUP BY 1
				ORDER BY 2 DESC, 1 ASC
				LIMIT 5''')	
	most_popular = cur.fetchall()
	print('The top 5 worldwide popular movies and the number of countries distributed are: ')
	print('Top 1: ' + most_popular[0][0] + ' : distributed to ' + str(most_popular[0][1]) + ' countries.')
	print('Top 2: ' + most_popular[1][0] + ' : distributed to ' + str(most_popular[1][1]) + ' countries.')
	print('Top 3: ' + most_popular[2][0] + ' : distributed to ' + str(most_popular[2][1]) + ' countries.')
	print('Top 4: ' + most_popular[3][0] + ' : distributed to ' + str(most_popular[3][1]) + ' countries.')
	print('Top 5: ' + most_popular[4][0] + ' : distributed to ' + str(most_popular[4][1]) + ' countries.')

	print('=========================================')

	cur.execute('''
				SELECT top_250_movies_basic_info.ranking,
					   more_movies_info.movie_name, 
				       top_250_movies_basic_info.rating,
					   more_movies_info.year, 
					   more_movies_info.runtime,
					   more_movies_info.genre,
					   more_movies_info.country,
					   more_movies_info.box_office,
					   COUNT(alias) as alias_num
				FROM top_250_movies_basic_info
				JOIN more_movies_info
				ON top_250_movies_basic_info.imdb_id = more_movies_info.imdb_id
				JOIN movie_aliases
				ON top_250_movies_basic_info.imdb_id = movie_aliases.imdb_id
				GROUP BY 1
				ORDER BY top_250_movies_basic_info.ranking''')	
	analysis_tb = cur.fetchall()
	analysis_df = pd.DataFrame(analysis_tb)
	analysis_df.columns = ['ranking','movie_name','rating','year','runtime','genre','country','box_office','alias_number']

	# what's the most popular genre for the movies to be on the top 250 list
	genre_df = analysis_df[['genre']]
	genre_list = list()
	genre_list.extend(genre_df['genre'].tolist())
	clean_genre_list = list()
	for item in genre_list:
		item_list = item.split(',')
		for i in item_list:
			i = i.strip()
			clean_genre_list.append(i)
	genre_dict = dict()
	for item in clean_genre_list:
		if item not in genre_dict:
			genre_dict[item] = 1
		else:
			genre_dict[item] += 1
	sorted_genre = sorted(genre_dict.items(), key=lambda x: x[1], reverse=True)
	print('Sorted genres and their frequencies on the top 250 IMDB movie list are: ')
	for item in sorted_genre:
		print(item)
	print()
	print('Top 3 frequent genres are: ')
	print('Top 1: ' + sorted_genre[0][0] + ' with a frequency of ' + str(sorted_genre[0][1]))
	print('Top 2: ' + sorted_genre[1][0] + ' with a frequency of ' + str(sorted_genre[1][1]))
	print('Top 3: ' + sorted_genre[2][0] + ' with a frequency of ' + str(sorted_genre[1][1]))

	print('=========================================')

	# which country has the most movies on the top 250 list
	country_df = analysis_df[['country']]
	country_list = list()
	country_list.extend(country_df['country'].tolist())
	clean_country_list = list()
	for item in country_list:
		item_list = item.split(',')
		for i in item_list:
			i = i.strip()
			clean_country_list.append(i)
	country_dict = dict()
	for item in clean_country_list:
		if item not in country_dict:
			country_dict[item] = 1
		else:
			country_dict[item] += 1
	sorted_country = sorted(country_dict.items(), key=lambda x: x[1], reverse=True)
	print('Sorted countries and their frequencies on the top 250 IMDB movie list are: ')
	for item in sorted_country:
		print(item)
	print()
	print('Top 3 frequent countries are: ')
	print('Top 1: ' + sorted_country[0][0] + ' with a frequency of ' + str(sorted_country[0][1]))
	print('Top 2: ' + sorted_country[1][0] + ' with a frequency of ' + str(sorted_country[1][1]))
	print('Top 3: ' + sorted_country[2][0] + ' with a frequency of ' + str(sorted_country[1][1]))

	print('=========================================')
	
	# year distribution
	year_df = analysis_df[['year']]
	year_df.year.plot.hist(bins=10,color='green')
	plt.xticks(range(min(year_df.year),max(year_df.year),5),fontsize=8,rotation=90)
	plt.xlabel('Year')
	plt.ylabel('Number of Movies')
	plt.title('Top 250 IMDB Movies Year Distribution',fontsize=16,fontweight='bold')
	plt.grid(True)
	plt.show()

	# runtime distribution
	runtime_df = analysis_df[['runtime']]
	runtime_df.runtime.plot.hist(bins=5,color='blue')
	plt.xticks(fontsize=8,rotation=90)
	plt.xlabel('Runtime')
	plt.ylabel('Number of Movies')
	plt.title('Top 250 IMDB Movies Runtime Distribution',fontsize=16,fontweight='bold')
	plt.grid(True)
	plt.show()

	# correlation between rating and runtime
	rating_runtime_df = analysis_df[['runtime','rating']]
	rating_runtime_df.plot.scatter(x='runtime',y='rating')
	plt.xlabel('Runtime')
	plt.ylabel('Rating')
	plt.title('Top 250 IMDB Movies - Runtime vs. Rating',fontsize=16,fontweight='bold')
	plt.show()

	slope,intercept,r,p,std_err = linregress(rating_runtime_df.runtime,rating_runtime_df.rating)
	print('Correlation formula between runtime and rating is: ' + 'y=' + str(slope) + 'x+' + str(intercept))
	print('R-square: ' + str(r**2))
	if abs(r)<=0.4:
		print('There is no/low correlation between runtime and rating.')
	elif 0.4<abs(r)<=0.7:
		print('There is a moderate correlation between runtime and rating.')
	elif abs(r)>0.7:
		print('There is a strong correlation between runtime and rating.')

	print('=========================================')

	# correlation between rating and box office
	rating_boxoffice_df = analysis_df[['box_office','rating']]
	for i in rating_boxoffice_df.index:
		if rating_boxoffice_df.box_office[i] == 'N/A' or rating_boxoffice_df.rating[i] == 'N/A':
			rating_boxoffice_df = rating_boxoffice_df.drop(i)
	bo_data_type_dict = {'box_office': float}
	rating_boxoffice_df = rating_boxoffice_df.astype(bo_data_type_dict)

	rating_boxoffice_df.plot.scatter(x='box_office',y='rating')
	plt.xlabel('Box Office')
	plt.ylabel('Rating')
	plt.title('Top 250 IMDB Movies - Box Office vs. Rating',fontsize=16,fontweight='bold')
	plt.show()

	slope2,intercept2,r2,p2,std_err2 = linregress(rating_boxoffice_df.box_office,rating_boxoffice_df.rating)
	print('Correlation formula between box office and rating is: ' + 'y=' + str(slope2) + 'x+' + str(intercept2))
	print('R-square: ' + str(r2**2))
	if abs(r2)<=0.4:
		print('There is no/low correlation between box office and rating.')
	elif 0.4<abs(r2)<=0.7:
		print('There is a moderate correlation between box office and rating.')
	elif abs(r2)>0.7:
		print('There is a strong correlation between box office and rating.')

	print('=========================================')

	# correlation between rating and number of aliases
	rating_alias_df = analysis_df[['alias_number','rating']]
	rating_alias_df.plot.scatter(x='alias_number',y='rating')
	plt.xlabel('Number of Aliases')
	plt.ylabel('Rating')
	plt.title('Top 250 IMDB Movies - Number of Aliases vs. Rating',fontsize=13,fontweight='bold')
	plt.show()

	slope3,intercept3,r3,p3,std_err3 = linregress(rating_alias_df.alias_number,rating_alias_df.rating)
	print('Correlation formula between number of aliases and rating is: ' + 'y=' + str(slope3) + 'x+' + str(intercept3))
	print('R-square: ' + str(r3**2))
	if abs(r3)<=0.4:
		print('There is no/low correlation between number of aliases and rating.')
	elif 0.4<abs(r3)<=0.7:
		print('There is a moderate correlation between number of aliases and rating.')
	elif abs(r3)>0.7:
		print('There is a strong correlation between number of aliases and rating.')


if __name__ == '__main__':
	if len(sys.argv) == 1:
		print('The scraping process might take several minutes. Please wait patiently. Thanks!')
		top_250_movies_web_scraper.func1()
		more_movies_info_API.func1()
		movie_aliases_API.func1()
		data_analysis()
	elif len(sys.argv) == 2: 
		top_250_movies_web_scraper.func3('data/top-250-movies-basic-info.csv')
		more_movies_info_API.func3('data/more-movies-info.csv')
		movie_aliases_API.func3('data/movie-aliases.csv')
		data_analysis()