import pandas as pd
import matplotlib.pyplot as plt

df_netflix = pd.read_csv("netflix.csv")
df_hulu = pd.read_csv("hulu.csv")
df_amazon = pd.read_csv("amazon.csv")
df_combined = pd.read_csv("combined.csv")

#filter movies
df_netflix_movie = df_netflix[df_netflix['type'] == 'Movie']
df_hulu_movie = df_hulu[df_hulu['type'] == 'Movie']
df_amazon_movie = df_amazon[df_amazon['type'] == 'Movie']

#extracting numeric value 
df_netflix_movie['duration_numeric'] = pd.to_numeric(df_netflix_movie['duration'].str.replace(' min', '', regex=False), errors='coerce')
df_hulu_movie['duration_numeric'] = pd.to_numeric(df_hulu_movie['duration'].str.replace(' min', '', regex=False), errors='coerce')
df_amazon_movie['duration_numeric'] = pd.to_numeric(df_amazon_movie['duration'].str.replace(' min', '', regex=False), errors='coerce')
df_netflix_movie.dropna(subset=["duration_numeric"], inplace=True)
df_hulu_movie.dropna(subset=["duration_numeric"], inplace=True)
df_amazon_movie.dropna(subset=["duration_numeric"], inplace=True)
	
#boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(
   [df_netflix_movie['duration_numeric'], df_hulu_movie['duration_numeric'], df_amazon_movie['duration_numeric']],
   labels=['Netflix', 'Hulu', 'Amazon Prime'],
)

#labels
plt.title('Distribution of Movie Durations by Platform', fontsize=16)
plt.ylabel('Duration (Minutes)', fontsize=12)
plt.xlabel('Platform', fontsize=12)

#layout
plt.tight_layout()
plt.show()
