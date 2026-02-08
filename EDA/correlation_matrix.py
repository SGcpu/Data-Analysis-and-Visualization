import pandas as pd

df = pd.read_csv("winequality-red.csv")
numeric_cols = df.select_dtypes(include=["float64", "int64"])

correlation = numeric_cols.corr()
print("Correlation Matrix:\n")
print(correlation)
