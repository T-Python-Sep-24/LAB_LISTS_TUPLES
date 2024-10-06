''' Scenario:
You have just been hired as a data analyst at a movie streaming platform. 
Your manager has given you a list of movies, each with a tuple containing the movie title,
 release year, and user ratings. The platform allows users to rate movies on a scale of 1 to 10.
   Your manager wants you to create a Python program that:

1. Accepts a list of movies, with each movie represented as a tuple containing the movie title, release year,
 and a list of user ratings.
2. Calculates the average rating for each movie.
3. Filters out movies with an average rating lower than 6.0.
5. Displays the  movies, along with their title, release year, and average rating.
'''


#List of movies with title, release year, and user ratings
movies = [
    ("Toy Story", 1995, [10, 9, 10, 10, 10, 9]),
    ("Finding Nemo", 2003, [9, 10, 8, 9, 9, 10]),
    ("The Lion King", 1994, [10, 10, 9, 10, 8, 9]),
    ("Frozen", 2013, [9, 8, 10, 9, 9, 10]),
    ("Moana", 2016, [9, 9, 10, 8, 9, 10]),
    ("Despicable Me", 2010, [8, 9, 8, 9, 7, 9]),
    ("Shrek", 2001, [9, 8, 9, 9, 10, 8])
]

#Calculate the average rating of a movie
def average_rating(ratings):
    return sum(ratings) / len(ratings)

#List to hold movies with average ratings
filtered_movies = []

#Calculate average ratings and filter movies
for title, year, ratings in movies:
    avg_rating = average_rating(ratings)
    if avg_rating >= 6.0:
        filtered_movies.append((title, year, avg_rating))

#Results
for index, (title, year, avg_rating) in enumerate(filtered_movies, start=1):
    print(f"{index}. {title} ({year}) - Average rating: {avg_rating:.2f} ★")