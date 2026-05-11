import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from books_data_prep import prepare_data

df = pd.read_csv("data/books.csv")
df = prepare_data(df)

sns.scatterplot(data=df, x="ratings_count", y="rating")

plt.title("Relationship Between Ratings Count and Rating")
plt.xlabel("Ratings Count")
plt.ylabel("Rating")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
