import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('customer_data_dirty.csv')
df2 = pd.read_csv('purchase_data_dirty.csv')

#3
gender_mapping = {'MALE': 'Male', 'male': 'Male', 'M': 'Male', 'FEMALE': 'Female', 'female': 'Female', 'F': 'Female'}
df['Gender'] = df['Gender'].replace(gender_mapping)

df2['ProductCategory'] = df2['ProductCategory'].str.lower()

print(df.head())
print(df2.head())