import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    'X': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'y': [1, 3, 2, 5, 7, 8, 8, 9, 10, 12]
}
df = pd.DataFrame(data)

x_mean = df['X'].mean()
y_mean = df['y'].mean()


numerator = ((df['X'] - x_mean) * (df['y'] - y_mean)).sum()
denominator = ((df['X'] - x_mean)**2).sum()


b1 = numerator / denominator
b0 = y_mean - b1 * x_mean


print(f"c) Regression coefficients:")
print(f"b1 (Slope): {b1:.4f}")
print(f"b0 (Intercept): {b0:.4f}")

print(f"d) Regression line equation:")
print(f"y = {b0:.4f} + {b1:.4f} * x")

df['y_pred'] = b0 + b1 * df['X']
rss = ((df['y'] - df['y_pred'])**2).sum()
tss = ((df['y'] - y_mean)**2).sum()
r_squared = 1 - (rss / tss)
rmse = np.sqrt(rss / len(df))


print(f"\ne) Performance metrics:")
print(f"   Residual Sum of Squares (RSS): {rss:.4f}")
print(f"   Coefficient of Determination (R^2): {r_squared:.4f}")
print(f"   Root Mean Squared Error (RMSE): {rmse:.4f}")

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='X', y='y', label='Actual_Data', s=150)
sns.lineplot(x=df['X'], y=df['y_pred'], color='green', label='Regression_Line')
plt.title('Regression Line Fit (Seaborn)')
plt.legend()
plt.show()