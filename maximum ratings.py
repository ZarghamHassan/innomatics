import pandas as pd
# Load the ratings data
ratings_df = pd.read_csv('ratings.csv')

# Load the movies data
movies_df = pd.read_csv('movies.csv')
# Count the number of ratings for each movieId
movie_rating_counts = ratings_df['movieId'].value_counts()

# Get the movieId with the maximum number of ratings
max_rated_movie_id = movie_rating_counts.idxmax()
# Get the movie title associated with the max_rated_movie_id
max_rated_movie = movies_df[movies_df['movieId'] == max_rated_movie_id]['title'].values[0]

print(f"The movie with the maximum number of ratings is: {max_rated_movie}")
