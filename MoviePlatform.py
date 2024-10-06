def get_avrg(movie_list:list)->list:
    """
    This function calculates the average of the ratings and returns it 
    Args:
        a list of movies that the platform provides
    Returns:
        a list with the results and with avrg_rating for each movie in the list
    """
    result=[]
    
    for movie in movie_list:
        movie_name,movie_year,ratings=movie
        if ratings:
            avrg_rating=round(sum(ratings)/len(ratings),2)
        else:
            avrg_rating=0
        
        result.append((movie_name,movie_year,avrg_rating)) 
    return result

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
    
]
result=get_avrg(movies)
wanted_result=list(filter(lambda movie:movie[2]>=6.0,result))
wanted_result.sort(key=lambda x:x[2],reverse=True)
index=1
for movie in wanted_result:
    print(f"{index}. {movie[0]} ({movie[1]}) - Average rating: {movie[2]} ★")
    index +=1
