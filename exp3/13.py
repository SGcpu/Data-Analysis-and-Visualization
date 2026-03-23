import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('customer_data_dirty.csv')
df2 = pd.read_csv('purchase_data_dirty.csv')

encoded_gender = pd.get_dummies(df['Gender'], prefix='Gender')

df = pd.concat([df, encoded_gender], axis=1)

df = df.drop('Gender', axis=1)

print("Dataset after one-hot encoding:")
print(df.head())
