import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("winequality-red.csv")
target_cols = ['alcohol', 'pH', 'fixed acidity', 'quality']

for col in target_cols:
    plt.figure()
    plt.hist(df[col], bins=20, color='skyblue', edgecolor='black')
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()
