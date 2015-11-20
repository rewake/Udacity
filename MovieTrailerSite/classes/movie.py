from video import Video


class Movie(Video):
    """ Class Movie extends the Video object and defines variables and methods related to movies.
    """

    # Instantiate class and declare variables
    def __init__(self, title, url, duration, poster_image):
        Video.__init__(self, title, url, duration)
        self.poster_image = poster_image
