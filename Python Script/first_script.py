favorite_movies = [
    {"name": "Inception", "release_year": 2010},
    {"name": "The Godfather", "release_year": 1972},
    {"name": "Interstellar", "release_year": 2014}
]

def check_movie(movie):
    if movie["release_year"] < 2000:
        print("This movie was released before 2000")
    else:
        print("This movie was released after 2000")
        return movie["name"]

recent_movies = []

for movie in favorite_movies:
    result = check_movie(movie)
    if result is not None:
        recent_movies.append(result)

print(recent_movies)