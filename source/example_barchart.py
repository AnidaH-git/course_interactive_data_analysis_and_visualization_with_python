import matplotlib.pyplot as plt
import pandas as pd
from books_data_prep import prepare_data

df = pd.read_csv("data/books.csv")
df = prepare_data(df)

section_counts = df["genre"].value_counts()
labels = section_counts.index
sizes = section_counts.values

plt.bar(x=labels, height=sizes)
plt.xticks(rotation=90)
plt.tight_layout()
plt.title("Books per Genre", loc="left")
plt.show()
