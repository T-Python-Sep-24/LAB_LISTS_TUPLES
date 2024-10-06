# List of movies with their titles, release years, and ratings
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

# Step 1: Calculate the average rating for each movie and store it in a new list
movies_with_avg_rating = []
for movie in movies:
    title, year, ratings = movie
    avg_rating = sum(ratings) / len(ratings)
    movies_with_avg_rating.append((title, year, avg_rating))

# Step 2: Filter movies with an average rating of 6.0 or higher
filtered_movies = []
for movie in movies_with_avg_rating:
    title, year, avg_rating = movie
    if avg_rating >= 6.0:
        filtered_movies.append((title, year, avg_rating))

# Step 3: Sort the filtered movies in descending order by the average ratin
filtered_movies.sort(reverse=True)
# Step 4: Print the movie details in the specified format
for title, year, avg_rating in filtered_movies:
    print(f"{title} ({year}) - Average rating: {round(avg_rating, 2)}")
