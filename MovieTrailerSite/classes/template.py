import os
import re


class Template:
    """ Class Template contains methods to load template files, parse template data, and display parsed data
    """

    # Set template path on instantiation
    def __init__(self, path):
        self.path = path
        print(os.getcwd())

    # Load HTML file content
    def load(self, filename):
        with open(os.getcwd() + os.sep + self.path + os.sep + filename + '.html', 'r') as f:
            return f.read()

    # Create content for movie titles section of the page
    def _create_movie_tiles_content(self, movies):

        # The HTML content for this section of the page
        content = ''

        # Loop movies and generate move tile content
        for movie in movies:
            # Extract the youtube ID from the url
            youtube_id_match = re.search(
                r'(?<=v=)[^&#]+', movie.url)
            youtube_id_match = youtube_id_match or re.search(
                r'(?<=be/)[^&#]+', movie.url)
            trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                                  else None)

            # Append the tile for the movie with its content filled in
            content += self.load('movie_tile_content').format(
                movie_title = movie.title,
                poster_image_url = movie.poster_image,
                trailer_youtube_id = trailer_youtube_id,
                duration = movie.duration
            )
        return content

    # Generate the HTML output file
    def generate_movies_page(self, movies):

        # Create or overwrite the output file
        output_file = open('richards_movies.html', 'w')

        # Replace the movie tiles placeholder generated content
        rendered_content = self.load('page_content').format(
            movie_tiles = self._create_movie_tiles_content(movies))

        # Output the file
        output_file.write(self.load('page_head') + rendered_content)

        # Close the file
        output_file.close()

        # Return the filename of the file we created so it can be actioned upon
        return os.path.abspath(output_file.name)
