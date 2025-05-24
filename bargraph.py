import pandas as pd
import matplotlib.pyplot as plt

movies_filtered_df = pd.read_csv("combined.csv")

# duration to numeric form
def extract_duration_minutes(duration):
    try:
        return int(duration.split()[0])  
    except (ValueError, AttributeError):
        return None
movies_filtered_df.loc[:, 'duration_mins'] = movies_filtered_df['duration'].apply(extract_duration_minutes)

# seperate by platform
netflix_movies = movies_filtered_df[movies_filtered_df["Platform"] == "Netflix"]
hulu_movies = movies_filtered_df[movies_filtered_df["Platform"] == "Hulu"]
prime_movies = movies_filtered_df[movies_filtered_df["Platform"] == "Amazon Prime"]

# filter for over 90
netflix_long = netflix_movies[netflix_movies['duration_mins'] > 90]
hulu_long = hulu_movies[hulu_movies['duration_mins'] > 90]
prime_long = prime_movies[prime_movies['duration_mins'] > 90]

# storing as bar heights
heights = [
    len(netflix_long),
    len(hulu_long),
    len(prime_long)
]

# storing bar categories
categories = ["Netflix", "Hulu", "Amazon Prime"]

# plotting
plt.bar(categories, heights, width=0.5, color="pink")

#adding labels/titles
plt.title('Movies Over 90 Minutes by Platform')
plt.xlabel('Platform')
plt.ylabel('Number of Movies')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# display
plt.show()