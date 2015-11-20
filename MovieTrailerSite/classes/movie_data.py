class MovieData:
    """ This class contains and returns movie trailer data
    """

    # This dictionary stores all data related to my movie trailers
    movie_data = {
        'Dancer in the Dark': {
            'title': 'Dancer in the Dark',
            'url': 'https://www.youtube.com/watch?v=53vr9EiOH7g',
            'duration': '140 min',
            'poster_image': 'http://ia.media-imdb.com/images/M/MV5BMTIxNDMwNTQ3NV5BMl5BanBnXkFtZTYwMDU4MzQ5._V1_SX640_SY720_.jpg'
        },
        'Eternal Sunshine of the Spotless Mind': {
            'title': 'Eternal Sunshine of the Spotless Mind ',
            'url': 'https://www.youtube.com/watch?v=quuMv7cGUn0',
            'duration': '108 min',
            'poster_image': 'http://ia.media-imdb.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1__SX915_SY694_.jpg'
        },
        'The Fountain': {
            'title': 'The Fountain',
            'url': 'https://www.youtube.com/watch?v=dAuxryJ6pv8',
            'duration': '96 min',
            'poster_image': 'http://ia.media-imdb.com/images/M/MV5BMTU5OTczMTcxMV5BMl5BanBnXkFtZTcwNDg3MTEzMw@@._V1__SX1473_SY711_.jpg'
        },
        '9': {
            'title': '9',
            'url': 'https://www.youtube.com/watch?v=UY7Tge7ftxM',
            'duration': '79 min',
            'poster_image': 'http://ia.media-imdb.com/images/M/MV5BMTY2ODE1MTgxMV5BMl5BanBnXkFtZTcwNTM1NTM2Mg@@._V1__SX1473_SY711_.jpg'
        },
        'The Fifth Element': {
            'title': 'The Fifth Element',
            'url': 'https://www.youtube.com/watch?v=VkX7dHjL-aY',
            'duration': '126 min',
            'poster_image': 'http://ia.media-imdb.com/images/M/MV5BMTkzOTkwNTI4N15BMl5BanBnXkFtZTYwMDIzNzI5._V1__SX1473_SY711_.jpg'
        },
        'Snatch': {
            'title': 'Snatch',
            'url': 'https://www.youtube.com/watch?v=ni4tEtuTccc',
            'duration': '102 min',
            'poster_image': 'http://ia.media-imdb.com/images/M/MV5BMTk5NzE0MDQyNl5BMl5BanBnXkFtZTcwNzk4Mjk3OA@@._V1__SX1473_SY711_.jpg'
        },
        'Star Wars: The Force Awakens': {
            'title': 'Star Wars: The Force Awakens',
            'url': 'https://www.youtube.com/watch?v=sGbxmsDFVnE',
            'duration': 'Length Unknown',
            'poster_image': 'http://ia.media-imdb.com/images/M/MV5BMTkwNzAwNDA4N15BMl5BanBnXkFtZTgwMTA2MDcwNzE@._V1__SX1473_SY711_.jpg'
        },
        'Up': {
            'title': 'Up',
            'url': 'https://www.youtube.com/watch?v=pkqzFUhGPJg',
            'duration': '96 min',
            'poster_image': 'http://ia.media-imdb.com/images/M/MV5BMTk3NDE2NzI4NF5BMl5BanBnXkFtZTgwNzE1MzEyMTE@._V1__SX1473_SY711_.jpg'
        }
    }

    # Get movie data
    def get_data(self):
        return self.movie_data
