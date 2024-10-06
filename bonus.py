movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

# loop through list and modify it
loopCounter: int = 0
for movie in movies:
    # calculate average rating
    avgRating: float = 0
    for i in movie[2]:
        avgRating += i
    avgRating = avgRating / len(movie[2])
    
    # filter out the movie if avgRating lower than 6
    if avgRating >= 6:
        # add avgRating to current tuple
        movies[loopCounter] = movie + (avgRating, )
    else:
        movies.remove(movie)
        print()
    
    loopCounter += 1

    # sort list by avgRating on last loop using lambda 
    if loopCounter >= len(movies):
        movies.sort(key = lambda x: x[3], reverse = True)

# Displays the movies, along with their title, release year, and average rating.
movieNumber = 0
for movie in movies:
    movieNumber += 1
    print(f"{movieNumber}. {movie[0]} ({movie[1]}) Average Rating: {movie[3]:.2f}")