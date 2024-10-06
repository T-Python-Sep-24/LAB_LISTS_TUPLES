#sum of all the items
def sum_list(l):
    return sum (l)
    
my_list=[2, 3, 4, 5, 15, 1, 43, 20]


print(sum_list(my_list))

#largest number from a list 
def max_list(n):
    return max(n)
max__list=[2, 3, 4, 5, 15, 1, 43, 20]
print(max_list(max__list))


#odd numbers

odd_numbers=[num for num in range(1200,2000,125)if num%2!=0]
print(odd_numbers)

#list slicing
new_list = odd_numbers[:5]

print(new_list)


#Bouns
def movie_ratings(movies):
   
    filtered_movies = [
        (title, year, sum(ratings) / len(ratings))
        for title, year, ratings in movies
        if sum(ratings) / len(ratings) >= 6.0
    ]


    print("movies=")
    for title, year, avg_rating in filtered_movies:
        print(f"{title} ({year}) - Average Rating: {avg_rating:.2f}")

movies =[  ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])]
movie_ratings(movies)

