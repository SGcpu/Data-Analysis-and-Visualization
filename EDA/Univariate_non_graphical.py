import pandas as pd


df = pd.read_csv("winequality-red.csv")


numeric_cols = df.select_dtypes(include=["float64", "int64"])

print("Summary Statistics:\n")
print(numeric_cols.describe())
