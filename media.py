class Movie():
    """ Gives information about movies.

    Argument:
    title -- The title of the movie
    story -- The storyline of the movie
    poster_image_url -- Movie's poster image url
    trailer_youtube_url -- Movie's tailer youtube url

    It shows the information like title, storyline,
    poster image url and trailer's youtube url
    of the movies."""
# This is documentation about the class movie

    def __init__(self, title, story, poster_image_url, trailer_youtube_url):
        # Defining class movie that takes arguments
        self.title = title
        self.story = story
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
