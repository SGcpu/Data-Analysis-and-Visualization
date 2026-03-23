import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('customer_data_dirty.csv')
df2 = pd.read_csv('purchase_data_dirty.csv')

#7
df2['Z_Score'] = (df2['PurchaseAmount'] - df2['PurchaseAmount'].mean()) / df2['PurchaseAmount'].std()

outliers = df2[np.abs(df2['Z_Score']) > 3]
print(outliers)
df2[np.abs(df2['Z_Score']) <= 3]

filtered_df = df2[np.abs(df2['Z_Score']) <= 3]
new_mean = filtered_df['PurchaseAmount'].mean()
print("New mean after removing outliers:", new_mean)
