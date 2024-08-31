import pandas as pd

# Load the movie details CSV file
movies_df = pd.read_csv('movies.csv')  # This file should contain movie titles and IDs

# Load the ratings CSV file
ratings_df = pd.read_csv('ratings.csv')  # This file should contain movie IDs and ratings

# Identify the movie ID for 'Terminator 2: Judgment Day'
movie_id = movies_df[movies_df['title'] == 'Terminator 2: Judgment Day (1991)']['movieId'].values[0]

# Filter the ratings for the identified movie ID
movie_ratings = ratings_df[ratings_df['movieId'] == movie_id]

# Calculate the average rating
average_rating = movie_ratings['rating'].mean()

print(f"The average user rating for 'Terminator 2: Judgment Day (1991)' is {average_rating:.2f}")
