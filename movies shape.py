import pandas as pd

# Load the CSV file
df = pd.read_csv('movies.csv')

# Get the shape of the dataframe
shape = df.shape

# Print the shape in (a, b) format
print(f"({shape[0]}, {shape[1]})")
