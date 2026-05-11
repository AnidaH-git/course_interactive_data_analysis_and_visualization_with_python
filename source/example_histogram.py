import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from books_data_prep import prepare_data

df = pd.read_csv("data/books.csv")
df = prepare_data(df)

plt.figure(figsize=(10, 5))
sns.histplot(df["rating"], bins=15, color="skyblue", edgecolor="black")

plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
