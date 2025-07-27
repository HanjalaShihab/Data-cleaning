import pandas as pd

data = data = pd.read_csv('NFL_play_v4.csv')

x = data.dropna(axis= 1)

print(x.shape)
print("--------------------")
print(x.head())


#get a small subset of the dataset:
subset_data = data.loc[:, 'EPA': 'Season'].head()
print(subset_data)
print("--------------------")


#filling the null values of the subset_data:
y = subset_data.fillna(0)
print(y)
print("--------------------")


# replace all NA's the value that comes directly after it in the same column, 
# then replace all the remaining na's with 0
z = subset_data.fillna(method = "bfill", axis= 0).fillna(0)
print(z)