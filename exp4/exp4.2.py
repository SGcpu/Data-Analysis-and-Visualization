import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('advertising.csv')

X = df[['TV']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

intercept = model.intercept_
slope = model.coef_[0]
r_squared = model.score(X_train, y_train)
print(f"Regression Coefficient (Slope): {slope:.4f}")
print(f"Intercept: {intercept:.4f}")
print(f"Coefficient of Determination (R^2): {r_squared:.4f}")

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)


plt.figure(figsize=(10, 6))


train_residuals = y_train - y_train_pred
test_residuals = y_test - y_test_pred


sns.scatterplot(x=y_train_pred, y=train_residuals, color='red', label='Training Data', alpha=0.7)


sns.scatterplot(x=y_test_pred, y=test_residuals, color='green', label='Testing Data', alpha=0.7)


plt.axhline(y=0, color='blue', linestyle='--', linewidth=2, label='Zero Error Line')


plt.title('Residual Error Plot')
plt.xlabel('Predicted Sales')
plt.ylabel('Residuals')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()