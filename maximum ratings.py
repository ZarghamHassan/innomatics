import pandas as pd
ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')
movie_rating_counts = ratings_df['movieId'].value_counts()
max_rated_movie_id = movie_rating_counts.idxmax()
max_rated_movie = movies_df[movies_df['movieId'] == max_rated_movie_id]['title'].values[0]
print(f"The movie with the maximum number of ratings is: {max_rated_movie}")
