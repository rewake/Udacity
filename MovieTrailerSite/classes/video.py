class Video:
    """ Class Video defines general variables and methods related to a video object.
    """

    # Instantiate class and declare variables
    def __init__(self, title, url, duration):
        self.title = title
        self.url = url
        self.duration = duration

    # Shows all declared variables in this class
    def info(self):
        print vars(self)
