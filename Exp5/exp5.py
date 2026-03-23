# %%
# ==========================================
# IMPORTING LIBRARIES
# ==========================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# %%
# ==========================================
# TASK 1: Multiple Linear Regression (Using Formula)
# ==========================================

# Data extracted from the provided PDF
X1 = np.array([10, 12, 10, 9, 15, 16, 10, 15, 15, 14])
X2 = np.array([8, 12, 9, 11, 11, 11, 10, 9, 10, 10])
y = np.array([10, 9, 10, 10, 10, 10, 9, 9, 11, 11])

# Create a DataFrame for easier handling
df1 = pd.DataFrame({'X1': X1, 'X2': X2, 'y': y})

# a) Print first 5 rows of data and display a scatter plot
print("--- Task 1a: First 5 rows ---")
print(df1.head())

print("\n--- Task 1a: Scatter plot ---")
# Using seaborn pairplot to show scatter plots between all variables
sns.pairplot(df1)
plt.suptitle("Scatter Plots of X1, X2, and y", y=1.02)
plt.show()

# %%
# b) Calculate (using formula) and print regression coefficients b0, b1, and b2
# Direct calculation of coefficients without matrix formula
mean_X1 = np.mean(X1)
mean_X2 = np.mean(X2)
mean_y = np.mean(y)

var_X1 = np.sum((X1 - mean_X1)**2)
var_X2 = np.sum((X2 - mean_X2)**2)
cov_X1_y = np.sum((X1 - mean_X1) * (y - mean_y))
cov_X2_y = np.sum((X2 - mean_X2) * (y - mean_y))

b1 = cov_X1_y / var_X1
b2 = cov_X2_y / var_X2
b0 = mean_y - b1 * mean_X1 - b2 * mean_X2

print("--- Task 1b: Regression Coefficients (Direct Calculation) ---")
print(f"b0 (Intercept): {b0:.4f}")
print(f"b1 (Coefficient for X1): {b1:.4f}")
print(f"b2 (Coefficient for X2): {b2:.4f}")

# %%
# c) Display regression line equation
print("--- Task 1c: Regression Equation ---")
print(f"Equation: y = {b0:.4f} + ({b1:.4f})*X1 + ({b2:.4f})*X2")

# %%
# d) Calculate and print coefficient of determination (R squared), RSS, and RMSE
# First, get the predicted y values using our coefficients
y_pred = b0 + b1 * X1 + b2 * X2

# Residual Sum of Squares (RSS)
rss = np.sum((y - y_pred)**2)

# Root Mean Square Error (RMSE)
rmse = np.sqrt(np.mean((y - y_pred)**2))

# Total Sum of Squares (TSS) for R-squared
tss = np.sum((y - np.mean(y))**2)
r_squared = 1 - (rss / tss)

print("--- Task 1d: Evaluation Metrics ---")
print(f"Residual Sum of Squares (RSS): {rss:.4f}")
print(f"Root Mean Square Error (RMSE): {rmse:.4f}")
print(f"Coefficient of Determination (R^2): {r_squared:.4f}")

# %%
# e) Plot regression line (3D plot since we have two independent variables)
print("--- Task 1e: Plotting Regression Plane ---")
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of actual data
ax.scatter(X1, X2, y, color='red', label='Actual Data', s=50)

# Create a meshgrid for the regression plane
x1_surf, x2_surf = np.meshgrid(np.linspace(X1.min(), X1.max(), 10), 
                               np.linspace(X2.min(), X2.max(), 10))
y_surf = b0 + b1*x1_surf + b2*x2_surf

# Plot the surface
ax.plot_surface(x1_surf, x2_surf, y_surf, alpha=0.5, cmap='viridis')

ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('y')
plt.title('3D Scatter Plot with Regression Plane')
plt.show()

# %%
# f) Predict the value of y given X1=10, X2=11
new_x1, new_x2 = 10, 11
predicted_y = b0 + b1*new_x1 + b2*new_x2

print("--- Task 1f: Prediction ---")
print(f"Predicted y for X1={new_x1} and X2={new_x2} is: {predicted_y:.4f}")


# %%
# ==========================================
# TASK 2: Multiple Linear Regression (Using sklearn)
# ==========================================

# a) Packages are already imported at the top (numpy, pandas, seaborn, sklearn)

# b) Read dataset "Advertising.csv"
try:
    df2 = pd.read_csv("Advertising.csv")
    print("--- Task 2b: Dataset Loaded Successfully ---")
    print(df2.head())
    
    # Assuming standard advertising.csv structure: Features (TV, Radio, Newspaper), Target (Sales)
    # Using the last column as Target, and the rest as Features for flexibility
    X = df2.iloc[:, :-1]  # Features: TV, Radio, Newspaper
    y_target = df2.iloc[:, -1]  # Target: Sales

    print(X)
    print(y_target)
    
    # c) Divide data into training and testing split (e.g., 80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y_target, test_size=0.2, random_state=42)
    
    # d) Create an instance of the class LinearRegression
    model = LinearRegression()
    
    # e) Fit the model for training data
    model.fit(X_train, y_train)
    
    # f) Get coefficients of regression and coefficient of determination
    train_r2 = model.score(X_train, y_train)
    
    print("\n--- Task 2f: Sklearn Model Coefficients & R2 ---")
    print(f"Intercept: {model.intercept_:.4f}")
    print(f"Coefficients: {model.coef_}")
    print(f"R-squared (Training): {train_r2:.4f}")
    
    # g) Apply the model for predictions on testing data and show residual plot
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    
    print("\n--- Task 2g: Residual Error Plot ---")
    plt.figure(figsize=(8, 5))
    
    # Residual error = Predicted - Actual
    plt.scatter(y_train_pred, y_train_pred - y_train, color='green', label='Training data residuals')
    plt.scatter(y_test_pred, y_test_pred - y_test, color='blue', label='Testing data residuals')
    
    # Zero residual error line
    plt.axhline(y=0, color='black', linestyle='--', linewidth=2)
    
    plt.xlabel('Predicted Values')
    plt.ylabel('Residuals')
    plt.title('Residual Error Plot')
    plt.legend()
    plt.show()

except FileNotFoundError:
    print("Error: 'Advertising.csv' not found. Please ensure the file is in the same directory as this script to run Task 2.")

# %%
# ==========================================
# POST LAB QUESTION
# ==========================================
print("""
--- Post Lab Question: Short note on logistic regression ---
Logistic Regression is a statistical and machine learning classification algorithm used to predict the probability of a categorical dependent variable. 
Unlike linear regression, which outputs continuous values, logistic regression uses a logistic (sigmoid) function to map predicted values to probabilities between 0 and 1. 
It is primarily used for binary classification tasks (e.g., spam vs. not spam, pass vs. fail), classifying a sample into the class with the highest probability threshold (commonly 0.5).
""")