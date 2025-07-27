import pandas as pd
import numpy as np

data = pd.read_csv('NFL_play_v4.csv')

missing_values = data.isnull().sum()
print(missing_values)
print("--------------------------")


missing_values_total = missing_values.sum()
print(missing_values_total)
print("--------------------------")


#Drop missing values:
x = data.dropna()
print(x.head())  #looks like whole dataset is gone empy as each row had at least one null value
print("--------------------------")



columns_with_na_dropped = data.dropna(axis= 1)
print(columns_with_na_dropped.head())
print("--------------------------")


#how much data we have lost:
print(f"Columns in original dataset: {data.shape[1]} columns")
print(f"Columns in original dataset: {columns_with_na_dropped.shape[1]} columns")
print("--------------------------")