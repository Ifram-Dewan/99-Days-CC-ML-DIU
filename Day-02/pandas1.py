import pandas as pd

# Creating a DataFrame
data = {
    "Name": ["Elias Bhai", "RIon BHai", "Pollab Bhai"],
    "Age": [25, 30, 35],
    "City": ["Nandipara", "Satarkul", "Badda"]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Selecting columns
print("\nAges:", df["Age"])

# Filtering rows
filtered_df = df[df["Age"] > 28]
print("\nFiltered DataFrame:\n", filtered_df)

# Adding a new column
df["Salary"] = [90000, 80000, 75000]
print("\nDataFrame with Salary:\n", df)

# Handling missing values
df.loc[1, "Salary"] = None  # Introducing a NaN value
print("\nDataFrame with NaN:\n", df)
df["Salary"].fillna(0, inplace=True)  # Replacing NaN with 0
print("\nDataFrame after filling NaN:\n", df)
