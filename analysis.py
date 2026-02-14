import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
print("\nBasic Statistics:")
print(df.describe())
# Average scores by gender
print("\nAverage Scores by Gender:")
print(df.groupby("gender")[["math score", "reading score", "writing score"]].mean())

sns.barplot(x="gender", y="math score", data=df)
plt.title("Average Math Score by Gender")
plt.show()
plt.figure(figsize=(6,4))
sns.heatmap(df[["math score", "reading score", "writing score"]].corr(), annot=True)
plt.title("Correlation Between Scores")
plt.show()
print("\nAverage Scores by Test Preparation:")
print(df.groupby("test preparation course")[["math score","reading score","writing score"]].mean())

sns.barplot(x="test preparation course", y="math score", data=df)
plt.title("Impact of Test Preparation on Math Score")
plt.show()
sns.boxplot(x="lunch", y="math score", data=df)
plt.title("Lunch Type vs Math Score")
plt.show()
df["average score"] = (df["math score"] + df["reading score"] + df["writing score"]) / 3

print("\nTop 5 Students by Average Score:")
print(df.sort_values("average score", ascending=False).head())





