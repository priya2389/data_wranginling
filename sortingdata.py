import pandas as pd

df_netflix = pd.read_csv("netflix.csv")
df_hulu = pd.read_csv("hulu.csv")
df_amazon = pd.read_csv("amazon.csv")

#sorting the data by release year
df_netflix_sorted = df_netflix.sort_values(by='release_year', ascending=True)
df_hulu_sorted = df_hulu.sort_values(by='release_year', ascending=True)
df_amazon_sorted = df_amazon.sort_values(by='release_year', ascending=True)

#sorting by rating
sorted_netflix_by_rating = df_netflix.sort_values(by='rating', ascending=True)
sorted_hulu_by_rating = df_hulu.sort_values(by='rating', ascending=True)
sorted_amazon_by_rating = df_amazon.sort_values(by='rating', ascending=True)

#sorting by date_added
sorted_netflix_by_date_added = df_netflix.sort_values(by='date_added', ascending=False)
sorted_hulu_by_date_added = df_hulu.sort_values(by='date_added', ascending=False)
sorted_amazon_by_date_added = df_amazon.sort_values(by='date_added', ascending=False)

#sorting by country
sorted_netflix_by_country = df_netflix.sort_values(by='country', ascending=True)
sorted_hulu_by_country = df_hulu.sort_values(by='country', ascending=True)
sorted_amazon_by_country = df_amazon.sort_values(by='country', ascending=True)

#writing to csv
df_netflix.to_csv('netflix.csv', index=False)
df_hulu.to_csv('hulu.csv', index=False)
df_amazon.to_csv('amazon.csv', index=False)

