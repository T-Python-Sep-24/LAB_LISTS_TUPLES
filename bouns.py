movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

def filter_movies():
    filtered =[]
    for movies2 in movies:
        year, title, ratings = movies2
        avg = sum(ratings)/ len(ratings)
        if avg >= 6.0:
            filtered.append((title,year, avg))
    return filtered
for movie in filter_movies():
        year, title, avg = movie
        print(f"{title} ({year}) - Average Rating: {avg:.2f} ★")

