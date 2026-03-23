import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('customer_data_dirty.csv')
df2 = pd.read_csv('purchase_data_dirty.csv')

#4
df = df.drop_duplicates(subset='CustomerID')
print(df.head())

