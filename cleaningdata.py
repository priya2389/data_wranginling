import pandas as pd

#reading csv files
df_netflix = pd.read_csv("netflix_titles.csv")
df_hulu = pd.read_csv("hulu_titles.csv")
df_amazon = pd.read_csv("amazon_prime_titles.csv")

#using forward fill
df_netflix.ffill(inplace=True)
df_hulu.ffill(inplace=True)
df_amazon.ffill(inplace=True)

#deleting all duplicates
df_netflix.drop_duplicates(keep="first", inplace=True)
df_hulu.drop_duplicates(keep="first", inplace=True)
df_amazon.drop_duplicates(keep="first", inplace=True)

#writing to csv
df_netflix.to_csv('netflix.csv', index=False)
df_hulu.to_csv('hulu.csv', index=False)
df_amazon.to_csv('amazon.csv', index=False)