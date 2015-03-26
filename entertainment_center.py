import fresh_tomatoes
import media

# Movie Content for Mabie Family Movie Trailers.  These movies were chosen either as favorite movies or had favorite subjects like "Coca-Cola" or "Mickey Mouse"
gods_not_dead = media.Movie("God's Not Dead", "A student's faith is challenged by a college professor.", "http://upload.wikimedia.org/wikipedia/en/c/cf/God%27s_Not_Dead.jpg","https://www.youtube.com/watch?v=90PWFEeRApA")

batman = media.Movie("Batman","Batman battles the Joker to save Gotham City.", "http://upload.wikimedia.org/wikipedia/en/3/3c/Batman_ver2.jpg","https://www.youtube.com/watch?v=EyozzozRsCk")

fletch = media.Movie("Fletch","An investigative news resporter uses multiple identities.", "http://upload.wikimedia.org/wikipedia/en/3/3e/Fletchmovieposter.jpg","https://www.youtube.com/watch?v=4sMMt2M3RiU")

the_edge = media.Movie("The Edge","Two men trapped in the wild fight for survival.", "http://upload.wikimedia.org/wikipedia/en/b/b2/TheEdgeposter.jpg","https://www.youtube.com/watch?v=GQZDxh5Im6E")

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy","An unlikely group of heroes save the galaxy.", "http://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg","https://www.youtube.com/watch?v=d96cjJhvlMA")

big_hero_six = media.Movie("Big Hero 6","A boy genius teams up with a robot to solve a mystery.", "http://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg","https://www.youtube.com/watch?v=z3biFxZIJOQ")

mickeys_christmas_carol = media.Movie("Mickey's Christmas Carol","A miserly man finds the true meaning of Christmas.", "http://cdnvideo.dolimg.com/cdn_assets/20f89c19e200dca37db63162fe8166cf6d373fa9.jpg","https://www.youtube.com/watch?v=ByAINYDyFXs")

the_cocoa_cola_kid = media.Movie("The Coca-Cola Kid","A businessman travels to Australia to sell Coca-Cola.", "http://ia.media-imdb.com/images/M/MV5BNDUxMjIyMTk3N15BMl5BanBnXkFtZTcwMjM5NzgxMQ@@._V1_SY317_CR3,0,214,317_AL_.jpg","https://www.youtube.com/watch?v=sd1DVlOl1eY")

movies = (gods_not_dead, batman,  fletch, the_edge, guardians_of_the_galaxy, big_hero_six, mickeys_christmas_carol, the_cocoa_cola_kid)
fresh_tomatoes.open_movies_page(movies)
