import webbrowser
class Movie():
    """Gives info about movies"""
    VALID_RATINGS = ["U", "U/G", "A"]
    
    def __init__(self, title, story, poster_image_url, trailer_youtube_url):
        self.title = title
        self.story = story
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def showtrailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
