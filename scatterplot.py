#plot the release year v.s data added to show how long it takes for each streaming platform to upload movies
import matplotlib.pyplot as plt
import pandas as pd

df_netflix = pd.read_csv("netflix.csv")
df_hulu = pd.read_csv("hulu.csv")
df_amazon = pd.read_csv("amazon.csv")

#change the date added to column to datetime
df_netflix['date_added'] = pd.to_datetime(df_netflix['date_added'].str.strip(), errors='coerce')
df_hulu['date_added'] = pd.to_datetime(df_hulu['date_added'].str.strip(), errors='coerce')
df_amazon['date_added'] = pd.to_datetime(df_amazon['date_added'].str.strip(), errors='coerce')

#plot the scatter plot for netflix
plt.figure(figsize=(8, 6))
plt.scatter(df_netflix['date_added'], df_netflix['release_year'], alpha=0.5, color='blue')
plt.title('Netflix: Date Added vs Release Year')
plt.xlabel('Date Added')
plt.ylabel('Release Year')
plt.grid(True)
plt.show()

#plot the scatter plot for hulu
plt.figure(figsize=(8, 6))
plt.scatter(df_hulu['date_added'], df_hulu['release_year'], alpha=0.5, color='green')
plt.title('Hulu: Date Added vs Release Year')
plt.xlabel('Date Added')
plt.ylabel('Release Year')
plt.grid(True)
plt.show()

#plot the scatter plot for amazon prime
plt.figure(figsize=(8, 6))
plt.scatter(df_amazon['date_added'], df_amazon['release_year'], alpha=0.5, color='red')
plt.title('Amazon Prime: Date Added vs Release Year')
plt.xlabel('Date Added')
plt.ylabel('Release Year')
plt.grid(True)
plt.show()
