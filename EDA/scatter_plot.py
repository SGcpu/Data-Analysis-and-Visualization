import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("winequality-red.csv")



# Visualizing Fixed Acidity vs Density (physically related properties)
plt.figure()
sns.scatterplot(x=df["fixed acidity"], y=df["density"], hue=df["quality"], palette="viridis")
plt.xlabel("Fixed Acidity")
plt.ylabel("Density")
plt.title("Fixed Acidity vs Density (Colored by Quality)")
plt.show()
