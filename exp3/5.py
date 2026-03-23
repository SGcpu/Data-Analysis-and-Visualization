import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('customer_data_dirty.csv')
df2 = pd.read_csv('purchase_data_dirty.csv')

#5
labels = ["Very Low", "Low", "Medium", "High"]
df["Income_equal_width"] = pd.cut(df["Income"], bins=4, labels=labels)
df["Income"].hist(bins=4, edgecolor="black")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.title("Income Distribution")
plt.show()

