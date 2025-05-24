import pandas as pd
import matplotlib.pyplot as plt

df_netflix = pd.read_csv("netflix.csv")
df_hulu = pd.read_csv("hulu.csv")
df_amazon = pd.read_csv("amazon.csv")
df_combined = pd.read_csv("combined.csv")

#years after 1970
df_netflix_filtered = df_netflix[df_netflix['release_year'] > 1970]
df_hulu_filtered = df_hulu[df_hulu['release_year'] > 1970]
df_amazon_filtered = df_amazon[df_amazon['release_year'] > 1970]

#grouping and counting release year column
netflix_titles_per_year = df_netflix_filtered.groupby('release_year').size()
hulu_titles_per_year = df_hulu_filtered.groupby('release_year').size()
amazon_titles_per_year = df_amazon_filtered.groupby('release_year').size()

#plotting
plt.figure(figsize=(12, 6))

#netflix
plt.plot(netflix_titles_per_year.index, netflix_titles_per_year.values,
        marker='o', linestyle='-', label='Netflix', color='red')

#hulu
plt.plot(hulu_titles_per_year.index, hulu_titles_per_year.values,
        marker='s', linestyle='--', label='Hulu', color='green')

#amazon
plt.plot(amazon_titles_per_year.index, amazon_titles_per_year.values,
        marker='d', linestyle=':', label='Amazon Prime', color='blue')

#adding labels
plt.title('Number of Titles Released Per Year (After 1970)', fontsize=16)
plt.xlabel('Release Year', fontsize=12)
plt.ylabel('Number of Titles', fontsize=12)
plt.legend(fontsize=12, loc='upper left')
plt.xticks(range(1970, max(df_combined['release_year']) + 1, 5),
          rotation=45, fontsize=10)  # Show every 5th year


#grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

#layout
plt.tight_layout()
plt.show()
