import pandas as pd

movies_df = pd.read_csv('movies.csv')

ratings_df = pd.read_csv('ratings.csv')

movie_id = movies_df[movies_df['title'] == 'Terminator 2: Judgment Day (1991)']['movieId'].values[0]

movie_ratings = ratings_df[ratings_df['movieId'] == movie_id]

average_rating = movie_ratings['rating'].mean()

print(f"The average user rating for 'Terminator 2: Judgment Day (1991)' is {average_rating:.2f}")
