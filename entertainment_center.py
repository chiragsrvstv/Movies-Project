import media
import fresh_tomatoes #This module converts list of given movie instances to web page


#Creating instances from class Movie


inception = media.Movie("Inception", "Story of dreams and reality",
                        "https://2.bp.blogspot.com/-uZUMCsz_H4M/TWaqInlGSmI/AAAAAAAABbc/2Xbu9kylMrQ/s1600/Inception-Widescreen-Wallpaper-1920x1200-2.jpg" ,
                        "https://www.youtube.com/watch?v=M7O44CUIRYU")  

jurassic_world = media.Movie("Jurassic World Fallen Kingdom", "Story of experimentally created Dinosaurs and their survival",
                     "https://images.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpapersite.com%2Fimages%2Fwallpapers%2Fjurassic-world-fallen-kingdom-1366x768-hd-2018-8342.jpg&f=1",
                     "https://www.youtube.com/watch?v=1FJD7jZqZEk")

batman_vs_superman = media.Movie("Batman VS Superman", "Two DC superheroes stand face to face",
                               "http://www.designbolts.com/wp-content/uploads/2015/12/Superman-vs-batman_wallpaper_HD.jpg",
                               "https://www.youtube.com/watch?v=IwfUnkBfdZ4")

three_hundred = media.Movie("300", "Story of three hundred spartans and thier bravery",
                            "http://static.rogerebert.com/uploads/movie/movie_poster/300-2006/large_4AmPMxTs1zSdCK0eCacj0kBgOMV.jpg",
                            "https://www.youtube.com/watch?v=UrIbxk7idYA")

twenty_three = media.Movie("The Number 23", "A psychological thriller film about obsession and madness",
                           "https://fmgreviews.files.wordpress.com/2014/06/carey-movie-23jpg.jpg",
                           "https://www.youtube.com/watch?v=TUTlOC4mVQ8")

fight_club = media.Movie("Fight Club", "Story of a man and his miserable life taking a huge turn",
                         "https://3.bp.blogspot.com/_3N0VetpYvQE/S9jg0AGYwyI/AAAAAAAACz8/OP6C90Or-5s/s1600/Fight_Club_3.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")


movie_list = [three_hundred , inception, batman_vs_superman, twenty_three, fight_club, jurassic_world] 

fresh_tomatoes.open_movies_page(movie_list) #Giving list of instances (movies) to open_movie_page of fresh tomato 


