import pandas as pd

df=pd.read_csv("superstore_excel-selected-columns.csv")

print("-"*100)
print('Sample Of DataSet:')
print(df.head())
print("-"*100)

print('Total Size of DataSet:')
print(df.shape)
print("-"*100)

print('Summary of DataSet:')
print(df.describe())
print("-"*100)
print(df.info())
print("-"*100)

print("Number Of Null Values In Dataset:")
print(df.isnull().sum())
print("-"*100)

sales=df.groupby("Category")["Region"].sum().sort_values(ascending=False)
print(sales)
print("-"*100)