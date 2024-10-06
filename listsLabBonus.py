movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

def analyzeMovies(moviesList):

    analyzed_movies = []
    for name, year, rates in moviesList:

        averageRate = sum(rates) / len(rates)

        if averageRate >= 6:
            analyzed_movies.append((name, year, averageRate))
    # print(analyzed_movies)
    analyzed_movies.sort()
    count = 1
    for name, year, avgRate in reversed(analyzed_movies):
        stars = ""
        if avgRate >= 9:
            stars = "★★★"
        elif 8 < avgRate < 9:
            stars = "★★"
        elif 7 < avgRate < 8:
            stars = "★"

        print(f"{count}. {name} ({year}) - Average rating: {avgRate:.2f} {stars}")
        count += 1


analyzeMovies(movies)

