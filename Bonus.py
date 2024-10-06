#Function to filter through a list of movies
def movieFiltering(movies: list) -> list :
    '''
    This function takes a list of movies, each element in the list is a tuple.
    Then it removes the movies with an average rating that is less than 6
    '''
    #Storing the modified movie list in modifiedMovies variable 
    modifiedMovies = list()

    #Making the varibale global to edit it in and out of the function
    global formattedOutput

    #The current iteration(index of current movie)
    i: int = 0

    for movie in movies:
        #Unpacking movie details into separate variables
        name, releaseYear, rating = movie
        
        #Calculate average rating of a movie 
        sum: int = 0
        averageRating: float = 0.0
        for n in rating:
            sum += n 
        averageRating = round(sum / (len(rating)), 2)
        #If the rating is less than 6, skip the iteration 
        if averageRating < 6.0:
            continue
        modifiedMovies = [name, releaseYear, averageRating]
        formattedOutput += f"{i + 1}. {name} ({releaseYear}) - Average rating: {averageRating} ★\n"
        i += 1
    
    #Return the movie list after filtering 
    return modifiedMovies

#Creating the list of movies
moviesList  = [ 
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

#Store the final output in this variable
formattedOutput: str = ""

#Call the method with the created list of movies
modMoviesList: list = movieFiltering(moviesList)
print(formattedOutput)
