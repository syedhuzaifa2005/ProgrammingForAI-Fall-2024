import pandas as pd

df = pd.read_csv('./world_alcohol_consumption.csv')

print("Dimensions of the dataset:", df.shape)
print("Column names in the dataset:", df.columns.tolist())