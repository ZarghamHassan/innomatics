import pandas as pd

ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')  

grouped_ratings = ratings_df.groupby('movieId').agg(rating_count=('rating', 'count'),average_rating=('rating', 'mean')).reset_index()
merged_df = pd.merge(movies_df, grouped_ratings, on='movieId')
filtered_df = merged_df[merged_df['rating_count'] > 50]

top_5_movies = filtered_df.nlargest(5, 'rating_count')
print("Top 5 popular movies based on the number of user ratings:")
print(top_5_movies[['title', 'rating_count']])
