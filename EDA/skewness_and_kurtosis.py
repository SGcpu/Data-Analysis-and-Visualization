import pandas as pd


df = pd.read_csv("winequality-red.csv")
numeric_cols = df.select_dtypes(include=["float64", "int64"])

print("Skewness:\n")
print(numeric_cols.skew())

print("\nKurtosis:\n")
print(numeric_cols.kurtosis())
