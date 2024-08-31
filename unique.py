import pandas as pd

df = pd.read_csv('ratings.csv')

unique_users = df['userId'].nunique()
print(f"Number of unique userId: {unique_users}")
