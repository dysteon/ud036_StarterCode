import webbrowser

class Movie():
    """ Class to contain all relevant information regarding Movies
    
    Attributes:
        title: String storing the title of the movie
        poster_image_url: String storing the online location of the film's poster
        trailer_youtube_url: String stroing the online location of the film's trailer
    """
    def __init__(self, movie_title, poster_image, trailer_youtube):
        """ Initiate an instance of Movie with provided values """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Open the online trailer of the provided Movie instance """
        webbrowser.open(self.trailer_youtube_url)
