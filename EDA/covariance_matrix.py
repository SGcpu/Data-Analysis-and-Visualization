import pandas as pd

df = pd.read_csv("winequality-red.csv")
numeric_cols = df.select_dtypes(include=["float64", "int64"])

covariance = numeric_cols.cov()
print("Covariance Matrix:\n")
print(covariance)
