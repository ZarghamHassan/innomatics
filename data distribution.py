import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew


ratings_df = pd.read_csv('ratings.csv') 
movies_df = pd.read_csv('movies.csv')  

movie_id = movies_df[movies_df['title'] == 'Fight Club (1999)']['movieId'].values[0]
movie_ratings = ratings_df[ratings_df['movieId'] == movie_id]['rating']

skewness = skew(movie_ratings)
print(f"Skewness of the rating distribution: {skewness:.2f}")

if skewness > 0:
    print("The distribution is right skewed.")
elif skewness < 0:
    print("The distribution is left skewed.")
else:
    print("The distribution is approximately normal.")
