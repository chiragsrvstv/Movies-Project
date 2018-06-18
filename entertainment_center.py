import media
import fresh_tomatoes

inception = media.Movie("Inception", "Dreams can be true",
                        "https://2.bp.blogspot.com/-uZUMCsz_H4M/TWaqInlGSmI/AAAAAAAABbc/2Xbu9kylMrQ/s1600/Inception-Widescreen-Wallpaper-1920x1200-2.jpg" ,
                        "https://www.youtube.com/watch?v=M7O44CUIRYU")

#print(inception.story)



jurassicworld = media.Movie("Jurassic World", "Dinos are coming",
                     "https://static0.srcdn.com/wp-content/uploads/2017/12/Jurassic-World-Fallen-Kingdom-Dinosaur-Fire.jpg",
                     "https://www.youtube.com/watch?v=1FJD7jZqZEk")


#print(jurassicworld.title)

movelst = [jurassicworld, inception]

#fresh_tomatoes.open_movies_page(movelst)

#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
