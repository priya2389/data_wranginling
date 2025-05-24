import pandas as pd

df_netflix = pd.read_csv("netflix.csv")
df_hulu = pd.read_csv("hulu.csv")
df_amazon = pd.read_csv("amazon.csv")

#adds platform in preparation for a combined df
df_netflix["Platform"] = "Netflix"
df_hulu["Platform"] = "Hulu" 
df_amazon["Platform"] = "Amazon Prime"

#creates and orders combined df
df_combined = pd.concat([df_netflix, df_hulu, df_amazon], ignore_index=True)
df_combined["release_year"] = pd.to_numeric(df_combined["release_year"], errors="coerce")

#filters for 2000-2010 
filtered_df = df_combined[ (df_combined["release_year"] >=2000) & (df_combined["release_year"] <= 2010)]
movies_filtered_df = filtered_df[filtered_df["type"] == "Movie"] 
tvShows_filtered_df = filtered_df[filtered_df["type"] == "TV Show"] 

#writing to csv
df_netflix.to_csv('netflix.csv', index=False)
df_hulu.to_csv('hulu.csv', index=False)
df_amazon.to_csv('amazon.csv', index=False)
filtered_df.to_csv('combined.csv', index=False)
