import fresh_tomatoes
import media

godzilla = media.Movie("Godzilla",
    "Giant lizard fights giant monsters.",
    "https://upload.wikimedia.org/wikipedia/en/1/10/Godzilla_%282014%29_poster.jpg",
    "https://www.youtube.com/watch?v=NwK1KurBS0o",
    "http://www.rottentomatoes.com/m/godzilla_2014/",
    "2014",
    "http://www.imdb.com/title/tt0831387/")

lotr_rotk = media.Movie("The Lord of the Rings: The Return of the King",
    "Frodo takes the One Ring to Mordor.",
    "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
    "https://www.youtube.com/watch?v=r5X-hFf6Bwo",
    "http://www.rottentomatoes.com/m/the_lord_of_the_rings_the_return_of_the_king/",
    "2003",
    "http://www.imdb.com/title/tt0167260/")

star_wars_tfa = media.Movie("Star Wars: The Force Awakens",
    "The Jedi are reborn and the First Order rises.",
    "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
    "https://www.youtube.com/watch?v=sGbxmsDFVnE",
    "http://www.rottentomatoes.com/m/star_wars_episode_vii_the_force_awakens/",
    "2015",
    "http://www.imdb.com/title/tt2488496/")

blade_runner = media.Movie("Blade Runner",
    "Replicants return to Earth and are hunted by Rick Deckard.",
    "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
    "https://www.youtube.com/watch?v=eogpIG53Cis",
    "http://www.rottentomatoes.com/m/blade_runner/",
    "1982",
    "http://www.imdb.com/title/tt0083658/")

spirited_away = media.Movie("Spirited Away",
    "Chihiro takes a job working in a bathhouse to find a way to free herself and her parents from the spirit world.",
    "https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG",
    "https://www.youtube.com/watch?v=ByXuk9QqQkk",
    "http://www.rottentomatoes.com/m/spirited_away/",
    "2001",
    "http://www.imdb.com/title/tt0245429/")

alien = media.Movie("Alien",
    "Highly aggressive extraterrestrial creature stalks and kills the crew of a spaceship.",
    "https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",
    "https://www.youtube.com/watch?v=LjLamj-b0I8",
    "http://www.rottentomatoes.com/m/alien/",
    "1979",
    "http://www.imdb.com/title/tt0078748/")
                            
movies = [godzilla, lotr_rotk, star_wars_tfa, blade_runner, spirited_away, alien]
fresh_tomatoes.open_movies_page(movies)
