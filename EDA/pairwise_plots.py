import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations

df = pd.read_csv("winequality-red.csv")

# Comparing Alcohol content vs Acidity and pH
features = [
    "alcohol",
    "fixed acidity",
    "pH"
]

pairs = combinations(features, 2)

for x, y in pairs:
    plt.figure()
    plt.scatter(df[x], df[y], alpha=0.5, c='darkred')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f"{x} vs {y}")
    plt.show()
