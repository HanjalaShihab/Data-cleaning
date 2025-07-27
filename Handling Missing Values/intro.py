import pandas as pd
import numpy as np

data = pd.read_csv('NFL_play_v4.csv')

print(data.head())
print("--------------------")


print(data.columns)
print("--------------------")

np.random.seed(0)


#There are many mnissing data points.How many?
missing_values = data.isnull().sum()
print(missing_values[0:10])
print("--------------------")


#how many total missin values do we have in percentage?
total_cells = np.prod(data.shape)
print(total_cells)

total_missing = missing_values.sum()
print(total_missing)


missing_percentage = (total_missing / total_cells) * 100
print(f"{missing_percentage:.2f}%")
