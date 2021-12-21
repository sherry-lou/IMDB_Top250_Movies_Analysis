# IMDB_Top250_Movies_Analysis

# NECESSARY LIBRARIES:

Besides BeautifulSoup, all libraries I used are standard Python built-in libraries. No need for installation of other libraries. Just in case, I also included a 'requirements.txt' so that the users can install any packages they don't have in order to run my code.


# SAMPLE INPUT TO RUN MY CODE:

1) first cd to my final project folder (below is my own path, but you should enter yours depending on where you stored the folder)
cd 'Google Drive'/'My Drive'/Classes/'DSCI 510'/HW5/'Lou-Lan(Sherry)-DSCI510-project'

2) run the analysis .py file (3 scrapers are imported as modules in the analysis .py file, so no need to run the three scrapers separately like in HW4)
-- static mode command line

python scraper_and_complete_analysis.py —static

-- real-time scraping mode command line

python scraper_and_complete_analysis.py

3) (optional) in case you want to check and run the three scrapers .py files, you can follow the below instructions (however no need to do so since all three scrapers are imported as modules into 'scraper_and_complete_analysis.py', so the information below is only for your reference)
	a) three ways to run the 'top_250_movies_web_scraper.py'
	# only getting five entries and store in database
	python top_250_movies_web_scraper.py —scrape

	# use the static csv I already scraped beforehand and store in database
	python top_250_movies_web_scraper.py —static 'data/top-250-movies-basic-info.csv'

	# scrape the entire website and store in database
	python top_250_movies_web_scraper.py


	b) three ways to run the 'more_movies_info_API.py'
	# only getting five entries and store in database
	python more_movies_info_API.py —scrape

	# use the static csv I already scraped beforehand and store in database
	python more_movies_info_API.py —static 'data/more-movies-info.csv'

	# scrape the entire website and store in database
	python more_movies_info_API.py


	c) three ways to run the 'movie_aliases_API.py'
	# only getting five entries and store in database
	python movie_aliases_API.py —scrape

	# use the static csv I already scraped beforehand and store in database
	python movie_aliases_API.py —static 'data/movie-aliases.csv'

	# scrape the entire website and store in database
	python movie_aliases_API.py


# SAMPLE OUTPUT OF MY CODE:

The output consists of two parts. 

Firstly, there is the text analysis output, like below:
	The top 5 rated movies by IMDB and their rating are: 
	Top 1: The Shawshank Redemption with rating of 9.220649578673955 and box office of $28699976.0
	Top 2: The Godfather with rating of 9.14744669786617 and box office of $134966411.0
	Top 3: The Godfather: Part II with rating of 8.980915536629867 and box office of $47834595.0
	Top 4: The Dark Knight with rating of 8.97405415507201 and box office of $534858444.0
	Top 5: 12 Angry Men with rating of 8.940342076396444 and box office of $N/A
	=========================================
	The average rating of the top 250 movies is 8.260663574127554
	The minimum rating of the top 250 movies is 8.019925624066646
	The maximum rating of the top 250 movies is 9.220649578673955
	=========================================
	The average runtime of the top 250 movies is 129.684 mins.
	The minimum runtime of the top 250 movies is 45 mins.
	The maximum runtime of the top 250 movies is 321 mins.
	=========================================
	The top five directors who have the most movies on the list are respectively: 
	Top 1: Akira Kurosawa (dir.) with 7 movies.
	Top 2: Christopher Nolan (dir.) with 7 movies.
	Top 3: Martin Scorsese (dir.) with 7 movies.
	Top 4: Stanley Kubrick (dir.) with 7 movies.
	Top 5: Alfred Hitchcock (dir.) with 6 movies.
	=========================================
	The top five actors who have the most movies on the list are respectively: 
	Top 1: Robert De Niro with 6 movies.
	Top 2: Tom Hanks with 5 movies.
	Top 3: Leonardo DiCaprio with 5 movies.
	Top 4: Charles Chaplin with 5 movies.
	Top 5: Toshirô Mifune with 4 movies.
	=========================================
	The top 5 worldwide popular movies and the number of countries distributed are: 
	Top 1: Star Wars : distributed to 176 countries.
	Top 2: Star Wars: Episode VI - Return of the Jedi : distributed to 125 countries.
	Top 3: Star Wars: Episode V - The Empire Strikes Back : distributed to 123 countries.
	Top 4: The Lord of the Rings: The Fellowship of the Ring : distributed to 102 countries.
	Top 5: Harry Potter and the Deathly Hallows: Part 2 : distributed to 101 countries.
	=========================================
	Sorted genres and their frequencies on the top 250 IMDB movie list are: 
	('Drama', 184)
	('Adventure', 56)
	('Crime', 53)
	('Action', 45)
	('Comedy', 43)
	('Thriller', 34)
	('Mystery', 31)
	('Biography', 28)
	('Romance', 24)
	('Animation', 22)
	('Sci-Fi', 20)
	('War', 20)
	('History', 15)
	('Fantasy', 13)
	('Family', 12)
	('Western', 6)
	('Music', 6)
	('Sport', 6)
	('Horror', 4)
	('Film-Noir', 3)
	('Musical', 1)

	Top 3 frequent genres are: 
	Top 1: Drama with a frequency of 184
	Top 2: Adventure with a frequency of 56
	Top 3: Crime with a frequency of 56
	=========================================
	Sorted countries and their frequencies on the top 250 IMDB movie list are: 
	('United States', 170)
	('United Kingdom', 49)
	('France', 26)
	('Japan', 18)
	('Germany', 14)
	('Italy', 13)
	('Canada', 8)
	('India', 8)
	('Spain', 7)
	('West Germany', 6)
	('Australia', 6)
	('Sweden', 6)
	('South Korea', 4)
	('Mexico', 4)
	('Soviet Union', 4)
	('New Zealand', 3)
	('Hong Kong', 3)
	('China', 3)
	('Poland', 2)
	('Iran', 2)
	('Austria', 2)
	('Argentina', 2)
	('Turkey', 2)
	('Algeria', 2)
	('Switzerland', 2)
	('Ireland', 2)
	('South Africa', 2)
	('Brazil', 1)
	('Malta', 1)
	('Morocco', 1)
	('Lebanon', 1)
	('Cyprus', 1)
	('Qatar', 1)
	('Czechoslovakia', 1)
	('Denmark', 1)
	('Kenya', 1)
	('Namibia', 1)
	('Bulgaria', 1)
	('Estonia', 1)
	('Georgia', 1)

	Top 3 frequent countries are: 
	Top 1: United States with a frequency of 170
	Top 2: United Kingdom with a frequency of 49
	Top 3: France with a frequency of 49
	=========================================
	Correlation formula between runtime and rating is: y=0.001473744924136164x+8.069542437385877
	R-square: 0.04679693147877373
	There is no/low correlation between runtime and rating.
	=========================================
	Correlation formula between box office and rating is: y=4.184909168070268e-10x+8.237928442858056
	R-square: 0.05713182858605123
	There is no/low correlation between box office and rating.
	=========================================
	Correlation formula between number of aliases and rating is: y=0.003941997840749098x+8.16356428331422
	R-square: 0.1351988549573893
	There is no/low correlation between number of aliases and rating.

Secondly, there are 5 graph outputs. The graphs will show up one by one, which is detailed in 'Project Description.pdf' and the explanatory video. The five graphs are respectively:
	1) Top 250 IMDB Movies Year Distribution
	2) Top 250 IMDB Movies Runtime Distribution
	3) Top 250 IMDB Movies - Runtime vs. Rating
	4) Top 250 IMDB Movies - Box Office vs. Rating
	5) Top 250 IMDB Movies - Number of Aliases vs. Rating


# DATA FLOW LOGIC OF MY CODE:

For the static portion, I originally used the three scrapers (the codes in each of the three scrapers that are now commented out) to first scrape the three datasets into three csv (which are my three database files in the 'data' folder). 

Then, if I choose to use the static mode, my three scrapers will store the three static csv files as three tables into the 'top_250_movies.db'. If I choose to use the real-time scraping mode, my three scrapers will first scrape the three datasets in real time, and then store them as three tables into the 'top_250_movies.db'. Either way, my three datasets are stores as three separate tables in the 'top_250_movies.db'. In the analysis part, I used SQL language to connect the three datasets and performed relative analyses.



# FILE CLARIFICATION IN MY PROJECT FOLDER:

scraper_and_complete_analysis.py  -- the final analysis .py file (the only one you need to run)
top_250_movies_web_scraper.py -- the first web scraper
more_movies_info_API.py -- the second scraper using API
movie_aliases_API.py -- the third scraper using API
top_250_movies.db -- database where I store my data (no matter using static mode or real-time scraping mode, data will be stored in this database)
data_structure.png -- a picture of my data structure
requirements.txt
Project Description.pdf -- analysis report
'data' folder -- static data csv files
'graphs' folder -- the graphs generated when running the analysis (I saved them in this folder for your reference)
video -- explanatory video to help you understand how to execute my code and understand my analysis



# MAINTAINABILITY & EXTENSIBILITY:

Maintainability:
My code is considered maintainable because anyone can access the code with the running commands mentioned above, and all three code files can be run in the terminal with command line arguments specified above. Besides BeautifulSoup, all libraries I used are standard Python built-in libraries. The user should first install/check the installation of BeautifulSoup and then run the codes in sequence. I also included a 'requirements.txt' so that users can install any packages they don't have in order to run my code. And the Python packages I used have no version dependencies. In addition, there should not be any code deprecation risks because the website I scraped is an official website by IMDB and won't be taken down without any given notice, and the APIs I used is from a credible API website called RapidAPI. The API key is embedded in my python codes and the API key is always accessible given I have subscribed to the two APIs I used from RapidAPI service. Also, since the API key is embedded, there won't be any bad API requests or bad user inputs because no API key input is needed. The user can choose to run the analysis .py file with the static datasets, or with real-time scraping from the three scrapers.

Extensibility:
To maximize extensibility, I built a database of the three datasets I extracted. It is relatively easy to do so since the three datasets can be linked by the primary key of IMDB ID, which is a unique identifier of movies. Also, my code will work even if the top 250 movies changed on the IMDB ranking website because the structure of the HTML code doesn't change, and my web scraping/API data extraction pipeline won't be affected amid data changes. Therefore, further analyses can be conducted on every year's top 250 IMDB movies.
