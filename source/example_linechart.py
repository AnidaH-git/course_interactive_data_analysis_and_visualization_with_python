import matplotlib.pyplot as plt
import pandas as pd
from books_data_prep import prepare_data

df = pd.read_csv("data/books.csv")
df = prepare_data(df)

borrowed_by_year = df.groupby("year_published")["times_borrowed"].sum()

plt.plot(borrowed_by_year.index, borrowed_by_year.values)

plt.show()
