import pandas as pd

df_netflix = pd.read_csv("netflix.csv")
df_hulu = pd.read_csv("hulu.csv")
df_amazon = pd.read_csv("amazon.csv")
df_combined = pd.read_csv("combined.csv")

#does an inner merge on Netflix and hulu datasets on the title column
shared_titles_netflix_and_hulu_df = pd.merge(df_netflix, df_hulu, on= "title", how = "inner")

#does an inner merge on the above dataframe and amazon prime dataset on the title column 
shared_titles_all_three_df = pd.merge(shared_titles_netflix_and_hulu_df, df_amazon, on= "title", how = "inner") 

#uses outer merge on release year, type, and platform columns for Netfliz and Hulu datasets
release_years_df = pd.merge(df_netflix[["release_year", "type", "Platform"]], df_hulu[["release_year", "type", "Platform"]], on = ["release_year", "type", "Platform"], how = "outer") 


#uses outer merge on release year, type, and platform (Hulu and Amazon Prime)
release_years_df = pd.merge(df_hulu[["release_year", "type", "Platform"]], df_amazon[["release_year", "type", "Platform"]], on = ["release_year", "type", "Platform"], how = "outer") 

#uses outer merge on release year, type, and platform (Netflix and Amazon Prime)
release_years_df = pd.merge(df_netflix[["release_year", "type", "Platform"]], df_amazon[["release_year", "type", "Platform"]], on = ["release_year", "type", "Platform"], how = "outer") 

#writing to csv
df_netflix.to_csv('netflix.csv', index=False)
df_hulu.to_csv('hulu.csv', index=False)
df_amazon.to_csv('amazon.csv', index=False)