import numpy as np
import pandas as pd
import seaborn as sns
import datetime

landslides = pd.read_csv('Parsing Dates/catalog.csv')

print(landslides.head())


#we will be working with the date column:
print(landslides['date'].head())

#checking the datatype of the date column:
print("Datatype of the date column is -", landslides['date'].dtype)


#converting the date column to datetime:
landslides['date_parsed'] = pd.to_datetime(landslides['date'], format = "%m/%d/%y")

print(landslides.columns)
print()
print(landslides['date_parsed'].head())