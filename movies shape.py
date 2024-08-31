import pandas as pd
df = pd.read_csv('movies.csv')
shape = df.shape
print(f"({shape[0]}, {shape[1]})")
