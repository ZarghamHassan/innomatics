import pandas as pd

# Load the CSV file
df = pd.read_csv('ratings.csv')

# Count the number of unique userId values
unique_users = df['userId'].nunique()

print(f"Number of unique userId: {unique_users}")
