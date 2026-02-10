# Data-Analysis-and-Visualization

## Overview
This project focuses on exploring and analyzing datasets using various statistical and graphical techniques. It provides Python scripts for performing exploratory data analysis (EDA) and generating insightful visualizations.

## Features
- **Univariate Analysis**: Analyze individual variables using statistical measures and visualizations.
- **Multivariate Analysis**: Explore relationships between multiple variables.
- **Visualization Techniques**:
  - Histograms
  - Scatter Plots
  - Box Plots
  - Pairwise Plots
  - Correlation and Covariance Matrices
- **Dataset**: The project uses the `winequality-red.csv` dataset, which contains information about the physicochemical properties of red wine samples.

## Files in the Repository
- `histogram.py`: Generates histograms for visualizing the distribution of variables.
- `scatter_plot.py`: Creates scatter plots to analyze relationships between variables.
- `boxplot.py`: Produces box plots to identify outliers and understand data spread.
- `pairwise_plots.py`: Generates pairwise plots for multivariate analysis.
- `correlation_matrix.py`: Computes and visualizes the correlation matrix.
- `covariance_matrix.py`: Computes and visualizes the covariance matrix.
- `skewness_and_kurtosis.py`: Calculates skewness and kurtosis for variables.
- `Univariate_non_graphical.py`: Performs non-graphical univariate analysis.

## Requirements
To run the scripts, install the required Python packages listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/SGcpu/Data-Analysis-and-Visualization.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Data-Analysis-and-Visualization
   ```
3. Run the desired Python script:
   ```bash
   python histogram.py
   ```

## Dataset
The `winequality-red.csv` dataset contains the following columns:
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

## License
This project is open-source and available under the [MIT License](LICENSE).

## Author
Developed by [SGcpu](https://github.com/SGcpu).