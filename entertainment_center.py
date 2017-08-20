import fresh_tomatoes
import media

""" Define multiple instances of the Movie class """
avatar = media.Movie("Avatar",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

shawshank_redemption = media.Movie("The Shawshank Redemption",
                                  "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SY1000_CR0,0,672,1000_AL_.jpg",
                                  "https://www.youtube.com/watch?v=6hB3S9bIaco")

stranger_than_fiction = media.Movie("Stranger than Fiction",
                                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY5MjA3MTY2Ml5BMl5BanBnXkFtZTcwNTMzNzYzMw@@._V1_SY1000_CR0,0,671,1000_AL_.jpg",
                                    "https://www.youtube.com/watch?v=PZpg8VII7es")   

""" Create single array of all created Movie class instances """
movies = [avatar, shawshank_redemption, stranger_than_fiction]

""" Open the website created with the movies array and fresh_tomatoes.py  """
fresh_tomatoes.open_movies_page(movies)
