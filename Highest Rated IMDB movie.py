import pandas as pd

filtered_movies_df = pd.read_csv('filtered_movies_with_imdb_links.csv')
scraped_ratings_df = pd.read_csv('scraped_ratings.csv')

merged_df = pd.merge(filtered_movies_df, scraped_ratings_df, on='title', how='inner')

merged_df['imdb_rating'] = merged_df['imdb_rating'].astype(float)


highest_rated_movie = merged_df.loc[merged_df['imdb_rating'].idxmax()]
highest_rated_movie_id = highest_rated_movie['movieId']
highest_rated_movie_name = highest_rated_movie['title']
print(f"Movie ID of the film with the highest IMDb rating: {highest_rated_movie_id}")
print(f"Title of the film with the highest IMDb rating: {highest_rated_movie_name}")
