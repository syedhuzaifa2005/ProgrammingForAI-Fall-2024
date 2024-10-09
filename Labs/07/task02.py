import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv("heart.csv")

# Check if the dataset is loaded correctly
print(data.head())  # Display the first few rows

# Rename 'sex' to 'gender'
data = data.rename(columns={'sex': "gender"})

# Replace values in the 'gender' column
data['gender'] = data['gender'].replace({1: "M", 0: "F"})

# Verify the changes in 'gender'
print(data['gender'].unique())

# Calculate and print mean, median, and mode for specified columns
print("\nMean:")
print(data[['Cholesterol', 'RestingBP', 'MaxHR']].mean())

print("\nMedian:")
print(data[['Cholesterol', 'RestingBP', 'MaxHR']].median())

print("\nMode:")
print(data[['Cholesterol', 'RestingBP', 'MaxHR']].mode())
