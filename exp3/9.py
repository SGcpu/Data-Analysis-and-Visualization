import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('customer_data_dirty.csv')
df2 = pd.read_csv('purchase_data_dirty.csv')

#9
df['Age_normalized'] = (df['Age']-df['Age'].min())/(df['Age'].max()-df['Age'].min())
df['Income_normalized'] = (df['Income']-df['Income'].min())/(df['Income'].max()-df['Income'].min())
print(df.head())
print(df2.head())