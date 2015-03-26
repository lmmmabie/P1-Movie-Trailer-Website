import webbrowser

class Movie():
    """ This clss provides a way to store movie related information"""

    # These are Valid Ratings for the movies
    VALID_RATINGS = ("G", "PG", "PG-13", "R")

    # This is the movie detail class
    def __init__(self, movie_title, movie_storyline, poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # This function will call the browser to open and play the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
