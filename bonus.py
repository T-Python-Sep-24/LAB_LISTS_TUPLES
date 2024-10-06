'''
# Bonus
## Movie Ratings Analysis
'''

def filtring_movies(movies:list):
    '''
    data analyst at a movie streaming platform

    Args:
        movies: (list): list of movies
    Returns:
        None
    '''
    best_movies=[]
    for i in range(len(movies)):
        if len(movies[i]) != 3 or not (isinstance(movies[i][0], str) and isinstance(movies[i][1], int) and isinstance(movies[i][2], list)):
            print("The input list should include the movie title, release year, and user ratings.")
            return
        sum_rating=0
        for j in range(len(movies[i][2])):
            sum_rating +=movies[i][2][j]
        avg_rating=sum_rating/6
        if avg_rating>=6:
            best_movies.append(list(movies[i]))
            best_movies[i].insert(0,round(avg_rating,2))
            best_movies.sort(reverse=True)
  
    for m, n in enumerate(best_movies, start=1):
     print(f"{m}. {n[1]} ({n[2]}) - Average rating: {n[0]} ★")     

# calling the function
filtring_movies(movies = [
    ( "The Shawshank Redemption",1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
])        