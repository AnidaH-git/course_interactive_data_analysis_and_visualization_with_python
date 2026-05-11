import matplotlib.pyplot as plt
import pandas as pd
from books_data_prep import prepare_data

df = pd.read_csv("data/books.csv")
df = prepare_data(df)

section_counts = df["section"].value_counts()
labels = section_counts.index
sizes = section_counts.values

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Books per Section")
plt.show()
