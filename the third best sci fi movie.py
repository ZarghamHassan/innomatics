import pandas as pd

ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')

grouped_ratings = ratings_df.groupby('movieId').agg(rating_count=('rating', 'count'),average_rating=('rating', 'mean')).reset_index()
merged_df = pd.merge(movies_df, grouped_ratings, on='movieId')
filtered_df = merged_df[merged_df['rating_count'] > 50]
sci_fi_movies = filtered_df[filtered_df['genres'].str.contains('Sci-Fi')]


sci_fi_movies_sorted = sci_fi_movies.sort_values(by='rating_count', ascending=False)
third_most_popular = sci_fi_movies_sorted.iloc[2] 
print(f"The third most popular Sci-Fi movie based on the number of user ratings is: {third_most_popular['title']}")
