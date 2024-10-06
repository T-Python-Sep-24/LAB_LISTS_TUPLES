
def CalculatesAverage(movies):
     resultMovies = []

     for title, year,ratings in movies:
          if ratings:
               averageRatings = round(sum(ratings)/len(ratings),2)
               if averageRatings >= 6.0:
                    print("/n {} ({}) -  Avergae rating : {}".format(title,year,averageRatings))
movies = [
("The Shawshank Redemption",1994, [9, 10, 10, 9, 8, 9]),
("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

CalculatesAverage(movies)
     
   







