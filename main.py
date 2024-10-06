#Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.
list=[2, 3, 4, 5, 15, 1, 43, 20]
def f_sum(list):
    return sum(list)
#Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
def largest_number(list):
    return max(list)
print(f_sum(list))
print(largest_number(list))
#Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
odd_numbers=[number for number in range (1200 , 2000 , 125)]
print(odd_numbers)
#use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.
slice_odd_num=odd_numbers[0:5]
print(slice_odd_num)

#Bonus
print("-"*15)
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
#Calculates the average rating for each movie.
average_ratings=[]
for movie in movies:
    title=movie[0]
    year=movie[1]
    rating=movie[2]
    average_rat= sum (rating)/len(rating)
    average_ratings.append((title,year,average_rat))
#Filters out movies with an average rating lower than 6.0.   
Filters_movies=[]
for movie in average_ratings:
    if movie[2]> 6.0:
        Filters_movies.append(movie)
#Displays the movies, along with their title, release year, and average rating.    
for i , movie in enumerate(Filters_movies):
    print(f"{i+1}.{movie[0]} ({movie[1]}) - Avergae rating:{movie[2]:.2f}★")
