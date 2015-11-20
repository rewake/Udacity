import webbrowser
from classes.movie_data import MovieData
from classes.template import Template
from classes.movie import Movie

'''
Procedure Outline / Algorithm

1. Load movie data
2. Create new movie objects from data
3. Generate HTML file using movie objects
3. Display generated movie trailers HTML page
'''

# Load movie data from Data Source. In this case, movie data is stored within a class (movie_data.py)
movie_data = MovieData().get_data()

# Create a list of movie objects from data provided above
movies = []
for k, v in movie_data.items():
    movies.append(Movie(v['title'], v['url'], v['duration'], v['poster_image']))

# Generate HTML file from templates
movie_file_url = Template('templates').generate_movies_page(sorted(movies))

# Open the output file in the browser (in a new tab, if possible)
webbrowser.open('file://' + movie_file_url, new=2)
