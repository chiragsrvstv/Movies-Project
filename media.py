class Movie():
    # This is documentation about the class movie
    """ Gives information about movies.

    Argument:
    title -- The title of the movie (string)
    story -- The storyline of the movie (string)
    poster_image_url -- Movie's poster image URL (string)
    trailer_youtube_url -- Movie's tailer youtube URL (string)

    It shows information like title, storyline,
    poster image url and trailer's youtube URL
    of the movie."""

    def __init__(self, title, story, poster_image_url, trailer_youtube_url):
        # Defining class movie that takes arguments
        self.title = title
        self.story = story
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
