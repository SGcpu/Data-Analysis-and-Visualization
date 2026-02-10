import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('customer_data_dirty.csv')
df2 = pd.read_csv('purchase_data_dirty.csv')
print(df.info())
print(df2.info())
#1
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Income'] = df['Income'].fillna(df['Income'].mean())
df2['PurchaseAmount'] = df['PurchaseAmount'].fillna(0)

#2
df = df[(df['Age'] >= 0) & (df['Age']<=100)]

#3
gender_mapping = {'MALE': 'Male', 'male': 'Male', 'M': 'Male', 'FEMALE': 'Female', 'female': 'Female', 'F': 'Female'}
df['Gender'] = df['Gender'].replace(gender_mapping)

df['ProductCategory'] = df['ProductCategory'].str.lower()

#4
df = df.drop_duplicates(subset='CustomerID')
print(df.head())

#5
df['Income_equal_width'] = pd.cut(df['Income'], bins=4, labels=['Very Low', 'Low', 'Medium', 'High'])

#6
plt.figure(figsize=(6,4))
df['Income_equal_width'].value_counts().sort_index().plot(kinf='bar', title='Income equal Width binning')
plt.show()

df['Income_EqualFreq'] = pd.qcut(df['Income'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])

#7
df['Z_Score'] = (df['PurchaseAmount']- df['PurchaseAmount'].mean()/df['PurchaseAmount'].std())

outliers = df[np.abs(df['Z_Score'])>3]
print(outliers)
df[np.abs(df['Z_Score'])<=3]

#9
df['Age_normalized'] = (df['Age']-df['Age'].min())/(df['Age'].max()-df['Age'].min())
df['Income_normalized'] = (df['Income']-df['Income'].min())/(df['Income'].max()-df['Income'].min())

#10
merged_df = pd.merge(df, df2, on='CustomerID', how='inner')

#11
avg_purchase = merged_df['PurchaseAmount'].mean()
merged_df['HighSpender'] = np.where(merged_df['PurchaseAmount']>avg_purchase, 1, 0)

merged_df = pd.get_dummies(merged_df, columns=['Gender'])

print(merged_df.head())
