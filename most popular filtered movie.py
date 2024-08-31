import pandas as pd

ratings_df = pd.read_csv('ratings.csv')  
movies_df = pd.read_csv('movies.csv')  


grouped_ratings = ratings_df.groupby('movieId').agg(rating_count=('rating', 'count'),average_rating=('rating', 'mean')).reset_index()
merged_df = pd.merge(movies_df, grouped_ratings, on='movieId')
filtered_df = merged_df[merged_df['rating_count'] > 50]


most_popular_movie = filtered_df.loc[filtered_df['average_rating'].idxmax()]
print(f"The most popular movie based on average user ratings is: {most_popular_movie['title']}")
