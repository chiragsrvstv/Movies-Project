import media
import fresh_tomatoes
# This module converts list of given movie instances to web page

# Creating instances from class Movie by passing arguments to them
inception = media.Movie(
                        "Inception", "Story of dreams and reality",
                        '''https://www.warnerbros.com/sites/default/files/inception_keyart.jpg''',
                        "https://www.youtube.com/watch?v=M7O44CUIRYU"
                        )

jurassic_world = media.Movie(
                            "Jurassic World Fallen Kingdom", '''Story of
                            experimentally created Dinosaurs and their
                            survival''', '''https://i1.wp.com/bestoftheyear.in/wp-content/uploads/2018/02/Jurassic-World-Fallen-Kingdom.jpg?fit=400%2C634&ssl=1''',
                            "https://www.youtube.com/watch?v=1FJD7jZqZEk"
                            )

batman_vs_superman = media.Movie(
                                "Batman VS Superman",
                                "Two DC superheroes stand face to face",
                                '''http://www.movies.ie/wp-content/uploads/2016/03/BVS-MoviesPlus-HD-382x215.-72-pixels.jpg''',
                                "https://www.youtube.com/watch?v=IwfUnkBfdZ4"
                                )

three_hundred = media.Movie(
                            "300",
                            "Story of 300 hundred spartans and thier bravery",
                            '''https://crypticrock.com/wp-content/uploads/2014/01/300-slide.jpg''',
                            "https://www.youtube.com/watch?v=UrIbxk7idYA"
                            )

twenty_three = media.Movie(
                            "The Number 23",
                            '''A psychological thriller film about
                            obsession and madness''',
                            '''http://www.cinemagora.co.uk/images/films/12/48412-b-the-number-23.jpg''',
                            "https://www.youtube.com/watch?v=TUTlOC4mVQ8"
                           )

fight_club = media.Movie(
                        "Fight Club",
                        '''Story of a man and his miserable life taking
                        a huge turn''',
                        '''http://www.flore-maquin.com/wp-content/uploads/Fight_club_RVB_72.jpg''',
                        "https://www.youtube.com/watch?v=SUXWAEX2jlg"
                        )

movie_list = [
                three_hundred, inception, batman_vs_superman,
                twenty_three, fight_club, jurassic_world
             ]
fresh_tomatoes.open_movies_page(movie_list)
# Giving list of instances (movies) to open_movie_page of fresh tomato
