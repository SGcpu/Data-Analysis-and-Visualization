import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('customer_data_dirty.csv')
df2 = pd.read_csv('purchase_data_dirty.csv')



df2.columns = df2.columns.str.strip()


print("Columns in df2 after stripping:", df2.columns)

df['Age'] = df['Age'].fillna(df['Age'].median())
df['Income'] = df['Income'].fillna(df['Income'].mean())

df2['PurchaseAmount'] = df2['PurchaseAmount'].fillna(0)

print(df.head())
print(df2.head())
