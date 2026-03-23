import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats
from pandas.plotting import parallel_coordinates


df = sns.load_dataset('tips')


print(df.head())
print(df.info())

# Set global style
sns.set_theme(style="whitegrid")

# 2. Generate Plots

# a) Bar Chart (Average feature values - e.g., Total Bill by Day)
plt.figure(figsize=(8, 6))
sns.barplot(x='day', y='total_bill', data=df, estimator=np.mean, errorbar=None)
plt.title('Average Total Bill by Day')
plt.ylabel('Average Total Bill')
plt.savefig('bar_chart.png')
plt.close()

# b) Stacked Bar Chart (e.g., Count of Smokers vs Non-Smokers by Day)
# Create a crosstab
ct = pd.crosstab(df['day'], df['smoker'])
ct.plot(kind='bar', stacked=True, figsize=(8, 6))
plt.title('Smoker counts by Day')
plt.ylabel('Count')
plt.savefig('stacked_bar_chart.png')
plt.close()

# c) Line Graph
# Since tips isn't time-series, let's simulate a trend or plot values sorted
# We can plot the cumulative sum of tips or just the tips over the index
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['total_bill'], label='Total Bill', alpha=0.5)
plt.plot(df.index, df['tip'], label='Tip', alpha=0.8)
plt.title('Line Graph of Total Bill and Tips (Index Sequence)')
plt.xlabel('Index')
plt.ylabel('Amount')
plt.legend()
plt.savefig('line_graph.png')
plt.close()

# d) Histogram
plt.figure(figsize=(8, 6))
sns.histplot(df['total_bill'], kde=False, bins=20)
plt.title('Histogram of Total Bill')
plt.savefig('histogram.png')
plt.close()

# e) Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='total_bill', y='tip', data=df, hue='day')
plt.title('Scatter Plot: Total Bill vs Tip')
plt.savefig('scatter_plot.png')
plt.close()

# f) Box Plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='day', y='total_bill', data=df)
plt.title('Box Plot of Total Bill by Day')
plt.savefig('box_plot.png')
plt.close()

# g) Parallel Coordinate Plot
# Needs normalization ideally, but we'll plot raw
plt.figure(figsize=(10, 6))
pc_df = df[['total_bill', 'tip', 'size', 'day']].copy()
parallel_coordinates(pc_df, 'day', color=sns.color_palette("husl", 4))
plt.title('Parallel Coordinate Plot')
plt.savefig('parallel_coordinate_plot.png')
plt.close()

# h) Heatmap
plt.figure(figsize=(8, 6))
corr = df.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.savefig('heatmap.png')
plt.close()

# i) QQ Plot
plt.figure(figsize=(8, 6))
stats.probplot(df['total_bill'], dist="norm", plot=plt)
plt.title('Q-Q Plot for Total Bill')
plt.savefig('qq_plot.png')
plt.close()

# j) Violin Plot
plt.figure(figsize=(8, 6))
sns.violinplot(x='day', y='total_bill', data=df)
plt.title('Violin Plot of Total Bill by Day')
plt.savefig('violin_plot.png')
plt.close()

# k) Pair Plot
# This creates a large figure automatically
plt = sns.pairplot(df, hue='sex')
plt.fig.suptitle('Pair Plot of Tips Dataset', y=1.02)
plt.savefig('pair_plot.png')
plt.close()

# l) KDE Plot
plt.figure(figsize=(8, 6))
sns.kdeplot(x='total_bill', y='tip', data=df, fill=True, cmap="Blues")
plt.title('KDE Plot (2D Density) of Total Bill vs Tip')
plt.savefig('kde_plot.png')
plt.close()

# m) Bubble Chart
# Scatter plot with size determined by a variable
plt.figure(figsize=(8, 6))
sns.scatterplot(x='total_bill', y='tip', size='size', sizes=(20, 200), hue='sex', data=df, alpha=0.7)
plt.title('Bubble Chart: Total Bill vs Tip (Size by Party Size)')
plt.savefig('bubble_chart.png')
plt.close()