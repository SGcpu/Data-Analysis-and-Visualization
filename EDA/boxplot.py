import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("winequality-red.csv")

# Select specific columns to keep the plot readable
cols_to_plot = df[['residual sugar', 'chlorides', 'pH', 'sulphates']]

plt.figure(figsize=(10, 6))
cols_to_plot.boxplot()
plt.title("Boxplot of Wine Chemical Features")
plt.ylabel("Value")
plt.show()
