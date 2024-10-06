def avg_rate(movies):
    rating_list = []
    for title, year, ratings in movies:
        avg_rating = sum(ratings) / len(ratings)
        if avg_rating >= 6:
            rating_list.append((title, year, avg_rating))
    return rating_list

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

rating_list = avg_rate(movies)

for title, year, avg in rating_list:
    print(f"Title: {title}, Year: {year}, Average Rating: {avg:.2f}")
