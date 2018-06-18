class Movie():
    """Gives info about movies"""           #This is information about the class movie for predifened class variable
    
    
    def __init__(self, title, story, poster_image_url, trailer_youtube_url):  #Defining class movie with constructor
        self.title = title
        self.story = story
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    
