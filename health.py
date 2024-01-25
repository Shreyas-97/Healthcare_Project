# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the healthcare dataset (replace 'your_dataset.csv' with the actual file path)
# For this example, let's assume the dataset has columns like 'Age', 'Gender', 'Condition', 'HospitalVisits', etc.
df = pd.read_csv('healthcare_dataset.csv')

# Data Exploration
print("Dataset Overview:")
print(df.info())

# Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Data Cleaning (Handling Missing Values)
df.dropna(inplace=True)

# Exploratory Data Analysis (EDA)
# Visualize age distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=20, kde=True)
plt.title('Age Distribution')
plt.show()

# Explore disease prevalence
plt.figure(figsize=(12, 8))
sns.countplot(x='Condition', data=df, order=df['Condition'].value_counts().index)
plt.title('Disease Prevalence')
plt.xticks(rotation=45)
plt.show()

# Patient Demographics
plt.figure(figsize=(8, 5))
sns.countplot(x='Gender', data=df)
plt.title('Gender Distribution')
plt.show()

# Utilization Metrics
plt.figure(figsize=(10, 6))
sns.boxplot(x='HospitalVisits', data=df)
plt.title('Hospital Visits Distribution')
plt.show()

# Correlation Analysis
plt.figure(figsize=(12, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Insights and Recommendations
# Provide any additional analysis or insights based on the visualizations and descriptive statistics.
