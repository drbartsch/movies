import webbrowser

class Movie():
    
    #This class provides a way to store movie related information.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, rotten_tomatoes, year_released, imdb_page):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rotten_tomatoes_url = rotten_tomatoes
        self.year_released = year_released
        self.imdb_page_url = imdb_page

    #This instance method opens the movie's trailer on YouTube's website.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
