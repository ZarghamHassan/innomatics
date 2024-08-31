import pandas as pd
df = pd.read_csv('ratings.csv')
shape = df.shape
print(f"({shape[0]}, {shape[1]})")
