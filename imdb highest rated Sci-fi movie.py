import pandas as pd

filtered_movies_df = pd.read_csv('filtered_movies_with_imdb_links.csv')
scraped_ratings_df = pd.read_csv('scraped_ratings.csv')

merged_df = pd.merge(filtered_movies_df, scraped_ratings_df, on='title', how='inner')

merged_df['imdb_rating'] = merged_df['imdb_rating'].astype(float)

sci_fi_movies_df = merged_df[merged_df['genres'].str.contains('Sci-Fi')]

highest_rated_sci_fi_movie = sci_fi_movies_df.loc[sci_fi_movies_df['imdb_rating'].idxmax()]

highest_rated_sci_fi_movie_id = highest_rated_sci_fi_movie['movieId']
highest_rated_sci_fi_movie_name = highest_rated_sci_fi_movie['title']
print(f"Movie ID of the highest-rated Sci-Fi movie: {highest_rated_sci_fi_movie_id}")
print(f"Title of the highest-rated Sci-Fi movie: {highest_rated_sci_fi_movie_name}")
