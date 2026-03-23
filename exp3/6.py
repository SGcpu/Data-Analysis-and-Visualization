import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('customer_data_dirty.csv')
df2 = pd.read_csv('purchase_data_dirty.csv')

df['Income_equal_width'] = pd.cut(df['Income'], bins=4, labels=['Very Low', 'Low', 'Medium', 'High'])

#6
plt.figure(figsize=(6,4))
df['Income_equal_width'].value_counts().sort_index().plot(kind='bar', title='Income equal Width binning')
plt.show()

df['Income_EqualFreq'] = pd.qcut(df['Income'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
print(df.head())
