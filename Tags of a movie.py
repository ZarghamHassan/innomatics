import pandas as pd

movies_df = pd.read_csv('movies.csv')
tags_df = pd.read_csv('tags.csv')

matrix_movie_id = movies_df[movies_df['title'] == "Matrix, The (1999)"]['movieId'].values[0]


matrix_tags = tags_df[tags_df['movieId'] == matrix_movie_id]['tag'].unique()
print("Tags for 'The Matrix (1999)':", matrix_tags)