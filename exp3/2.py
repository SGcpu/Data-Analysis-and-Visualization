import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('customer_data_dirty.csv')
df2 = pd.read_csv('purchase_data_dirty.csv')

#2
df = df[(df['Age'] >= 0) & (df['Age']<=100)]

print(df.head())
print(df2.head())
