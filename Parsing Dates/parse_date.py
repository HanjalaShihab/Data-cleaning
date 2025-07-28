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


print(landslides.head())  #containign both the date and date_parsed column

landslides.drop(columns=['date'], inplace= True)    #dropped the date column
print(landslides.head())


#reordering the columns as the date_parsed column added to the last-
cols = ['date_parsed'] + [cols for cols in landslides.columns if cols != 'date_parsed']
landslides = landslides[cols]
print(landslides.head())


#Select the day of the month:
day_of_month = landslides['date_parsed'].dt.day
print(day_of_month.head())


x = landslides['date_parsed'].isnull().sum().sum() 
print(x)

day_of_month = day_of_month.dropna()

sns.displot(day_of_month, kde = False, bins = 31)