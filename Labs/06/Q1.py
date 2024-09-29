import pandas as pd

movies = {
  'Title': [movie 1, movie 2, movie 3, movie 4, movie 5, movie 6],
  'Revenue': [1.8, 2.7, 4.9, 0.8, 3.2, 2.2],
  'Budget': [1, 1.3, 2.1, 0.5, 1.2, 0.8]
}

df = pd.DataFrame(movies)
filtered_movies = df[(df['Revenue'] > 2) and (df['Budget'] < 1)]
print(filtered_movies)
