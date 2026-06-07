import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load dataset
df = pd.read_csv("student_performance.csv", sep=';')

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Dataset statistics
print("\nStatistics:")
print(df.describe())

# Average scores
print("\nAverage Scores:")
print(df[['G1', 'G2', 'G3']].mean())

# Graph 1 - Final Grade Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['G3'], bins=10, kde=True)
plt.title("Final Grade Distribution")
plt.xlabel("Final Grade")
plt.ylabel("Number of Students")
plt.show()

# Graph 2 - Gender vs Final Grade
plt.figure(figsize=(6,5))
sns.barplot(x='sex', y='G3', data=df)
plt.title("Gender vs Final Grade")
plt.xlabel("Gender")
plt.ylabel("Final Grade")
plt.show()

# Graph 3 - Study Time vs Final Grade
plt.figure(figsize=(6,5))
sns.barplot(x='studytime', y='G3', data=df)
plt.title("Study Time vs Final Grade")
plt.xlabel("Study Time")
plt.ylabel("Final Grade")
plt.show()

# Graph 4 - Absences vs Final Grade
plt.figure(figsize=(8,5))
sns.scatterplot(x='absences', y='G3', data=df)
plt.title("Absences vs Final Grade")
plt.xlabel("Absences")
plt.ylabel("Final Grade")
plt.show()

print("\nTask Completed Successfully!")