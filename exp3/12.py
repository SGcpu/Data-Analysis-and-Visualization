import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('customer_data_dirty.csv')
df2 = pd.read_csv('purchase_data_dirty.csv')

merged_df = pd.merge(df, df2, on='CustomerID', how='inner')

""" female_customers = merged_df[merged_df['Gender'] == 'Female']

total_purchase_female = female_customers['PurchaseAmount'].sum()
average_purchase_female = female_customers['PurchaseAmount'].mean()

print("Total Purchase Amount for Female Customers:", total_purchase_female)
print("Average Purchase Amount for Female Customers:", average_purchase_female)
 """
""" # 12.2 Dice operation: Gender = Male, ProductCategory = Electronics
male_electronics = merged_df[(merged_df['Gender'] == 'Male') & (merged_df['ProductCategory'] == 'Electronics')]
number_of_purchases = male_electronics.shape[0]
average_purchase_male_electronics = male_electronics['PurchaseAmount'].mean()

print("Number of Purchases (Male, Electronics):", number_of_purchases)
print("Average Purchase Amount (Male, Electronics):", average_purchase_male_electronics)
 """
""" # 12.3 Roll-up operation: Total purchase amount by Gender
total_purchase_by_gender = merged_df.groupby('Gender')['PurchaseAmount'].sum()
print("Total Purchase Amount by Gender:")
print(total_purchase_by_gender)
"""
# 12.4 Drill-down operation: Analyze purchase amount by Gender and ProductCategory
purchase_by_gender_category = merged_df.groupby(['Gender', 'ProductCategory'])['PurchaseAmount'].sum()
print("Purchase Amount by Gender and Product Category:")
print(purchase_by_gender_category) 