import pandas as pd
import matplotlib.pyplot as plt

df_combined = pd.read_csv("combined.csv")

#plots histogram
plt.figure(figsize=(10, 6))
plt.hist(df_combined['Platform'], bins=3, color='purple', edgecolor='black')
plt.title('Content Count by Platform')
plt.xlabel('Platform')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()
