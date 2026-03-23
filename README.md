# Data Analysis and Visualization

A small collection of Python scripts for **exploratory data analysis (EDA)** and **data visualization** using the classic **Wine Quality (Red)** dataset (`winequality-red.csv`).

This repository is meant to be easy to read and run: each script focuses on one concept (e.g., histograms, scatter plots, correlation) so you can learn EDA step-by-step.

---

## What we’re planning to do (Project Goals)

This repo is an ongoing EDA + visualization walkthrough. The plan is to:

1. **Understand the dataset**
   - Identify columns, data types, missing values, and basic summary statistics.

2. **Run univariate analysis (one variable at a time)**
   - Central tendency and spread (mean/median/std, min/max, IQR)
   - Distribution shape (skewness and kurtosis)
   - Visual checks with histograms and box plots

3. **Run multivariate analysis (relationships between variables)**
   - Scatter plots for feature-to-feature relationships
   - Pairwise plots to quickly scan multiple relationships
   - Correlation and covariance matrices to measure linear relationships

4. **Connect features to wine quality**
   - See which physicochemical properties appear most related to the **`quality`** target
   - Use visuals + correlation to support conclusions (not just guesses)

5. **Make results easier to understand** (planned improvements)
   - Add clearer plot titles/labels and consistent styling
   - Add short written interpretations after each analysis step
   - (Optional) Export plots to an `outputs/` folder for easy viewing

---

## What’s included

### Scripts
- `histogram.py` — histograms to view distributions.
- `boxplot.py` — box plots to detect outliers and compare spread.
- `scatter_plot.py` — scatter plots to explore relationships.
- `pairwise_plots.py` — pair plots for quick multivariate scanning.
- `correlation_matrix.py` — correlation heatmap / matrix.
- `covariance_matrix.py` — covariance matrix.
- `skewness_and_kurtosis.py` — distribution shape metrics.
- `Univariate_non_graphical.py` — non-graphical summary statistics.

### Dataset
- `winequality-red.csv` — physicochemical properties of red wines plus a **quality score** (target).

---

## Requirements

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## How to run

```bash
git clone https://github.com/SGcpu/Data-Analysis-and-Visualization.git
cd Data-Analysis-and-Visualization
python histogram.py
```

Run any other script the same way, for example:

```bash
python correlation_matrix.py
```

---

## Dataset columns (Wine Quality - Red)

- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol
- Quality (target variable)

---

## License

MIT License (see `LICENSE`).

## Author

Developed by [SGcpu](https://github.com/SGcpu).