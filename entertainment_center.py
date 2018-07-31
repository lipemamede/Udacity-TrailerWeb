# encoding: utf-8

import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his Toys that come to life",
                        "https://goo.gl/dURc8K",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on alien planet",
                     "https://goo.gl/NBC4Yp",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie("School of Rock",
                             "Storyliner",
                             "https://goo.gl/d4xLK9",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "Storyline",
                            "https://goo.gl/JRNkko",
                            "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Storyline",
                                "https://goo.gl/DZwbqk",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie("Hunger Games",
                            "Storyline",
                            "https://goo.gl/xRBgVi",
                            "https://www.youtube.com/watch?v=PbA63a7H0bo")
movies = [toy_story, avatar,
          school_of_rock, ratatouille,
          midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)


