import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb

dataset = pd.read_csv('ToyotaCorolla.csv')

print(dataset)
print(dataset.iloc[3:7,2:5])
print(dataset.keys())
print(dataset.info())
print(dataset.describe())
print(dataset.iloc[:,8:13].describe())
print(dataset.duplicated().sum())
print(dataset.duplicated())

print(dataset['Fuel_Type'].unique())
print(dataset['Color'].unique())
print(dataset['Automatic'].unique())

fig, axes = plt.subplots(3, 1)
sb.countplot(data=dataset, x='Fuel_Type', ax=axes[0]).set(title='Fuel_Type')
sb.countplot(data=dataset, x='Color', ax=axes[1]).set(title='Color')
sb.countplot(data=dataset, x='Automatic', ax=axes[2]).set(title='Automatic')

plt.show()

print(dataset.isnull().sum())
print(dataset.shape)

dataset.drop(['Id'], axis=1, inplace=True)

print(dataset.shape)

print(dataset.corr())

print(dataset['Fuel_Type'].unique())
print(dataset['Color'].unique())
print(dataset['Automatic'].unique())

sb.heatmap(data=dataset.corr(), cmap="YlGnBu", annot=True)
plt.show()

print(dataset.keys())
