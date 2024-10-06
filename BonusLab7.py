#Bonus Lab 7

# List of movies, each movie is represented as a tuple (title, release year, ratings list)
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

def calculate_average(ratings):
    return sum(ratings) / len(ratings)

def display_movies(movies):
    filtered_movies = []
    
    for movie in movies:
        title, year, ratings = movie
        avg_rating = calculate_average(ratings)
        if avg_rating >= 6.0:
            filtered_movies.append((title, year, avg_rating))
    
    filtered_movies.sort(key=lambda x: x[2], reverse=True)
    
    for i, movie in enumerate(filtered_movies, 1):
        title, year, avg_rating = movie
        print(f"{i}. {title} ({year}) - Average rating: {avg_rating:.2f} ★")

display_movies(movies)

        