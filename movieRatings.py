movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

avgRates = []
for i in range(len(movies)):
    ratingList = movies[i][2]
    avgRates.append(sum(ratingList) / len(ratingList))
  
print()  
for i in range(len(avgRates)):
    if avgRates[i] > 6:
        print(f'{movies[i][0]} - Avergae rating: {round(avgRates[i], 2)} ★')

print()  