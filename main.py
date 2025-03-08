def load_movies():
    """Load movies from the movies.txt file."""
    movies = []
    with open('movies.txt', 'r') as file:
        for line in file:
            title, genres_str = line.strip().split(';')
            genres = genres_str.split(',')
            movies.append({"title": title, "genres": genres})
    return movies

def has_preferred_genre(movie_genres, preferred_genres):
    """Check if a movie's genres contain any of the preferred genres."""
    return any(genre.lower() in preferred_genres for genre in movie_genres)

def recommend_movies_by_genre(movies, preferred_genres):
    """Filter and return movies that match any of the preferred genres."""
    return [movie for movie in movies if has_preferred_genre(movie["genres"], preferred_genres)]

if __name__ == "__main__":
    # Load movies from file
    movies = load_movies()
    
    # Ask the user for their preferred genres
    user_input = input("Enter the genres you like (comma separated): ")
    preferred_genres = [genre.strip().lower() for genre in user_input.split(',') if genre.strip()]

    # Get recommendations
    recommendations = recommend_movies_by_genre(movies, preferred_genres)

    if not recommendations:
        print("No movies found for the given genres.")
    else:
        print("\nRecommended Movies:")
        for movie in recommendations:
            genres_str = ", ".join(movie['genres'])
            print(f"- {movie['title']} (Genres: {genres_str})")
