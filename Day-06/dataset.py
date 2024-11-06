import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
# Replace 'your_dataset.csv' with the path to your dataset
try:
    df = pd.read_csv('your_dataset.csv')
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: The file was not found. Please check the file path.")
    exit()

# Display the first 5 rows of the dataset
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Display dataset summary
print("\nDataset Summary (Numerical Columns):")
print(df.describe())

# Check for missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Handle missing values (example: fill with mean for numerical columns)
df = df.fillna(df.mean())

# Calculate and display key statistics
print("\nMean of each column:")
print(df.mean(numeric_only=True))

print("\nMedian of each column:")
print(df.median(numeric_only=True))

print("\nStandard Deviation of each column:")
print(df.std(numeric_only=True))

# Visualize the data
# Make sure to replace 'your_column_name' with an actual numeric column name from your dataset
numeric_columns = df.select_dtypes(include=np.number).columns
if len(numeric_columns) > 0:
    # Histogram of the first numeric column
    plt.figure(figsize=(8, 6))
    sns.histplot(df[numeric_columns[0]].dropna(), kde=True)
    plt.title(f"Distribution of {numeric_columns[0]}")
    plt.xlabel(numeric_columns[0])
    plt.ylabel("Frequency")
    plt.show()

    # Boxplot of the first numeric column
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df[numeric_columns[0]].dropna())
    plt.title(f"Boxplot of {numeric_columns[0]}")
    plt.show()

    # Correlation matrix heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()
else:
    print("No numeric columns available for visualization.")

