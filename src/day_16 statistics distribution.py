import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Make results reproducible
np.random.seed(42)

# ----------------------------
# 1. Create Datasets
# ----------------------------

# Normal Distribution (Heights)
heights = np.random.normal(170, 10, 1000)

# Right-Skewed Distribution (Income)
incomes = np.random.exponential(50000, 1000)

# Left-Skewed Distribution (Easy Exam Scores)
scores = 100 - np.random.exponential(10, 1000)
scores = np.clip(scores, 0, 100)

# Store in dictionary
datasets = {
    "Heights (Normal)": heights,
    "Incomes (Right-Skewed)": incomes,
    "Scores (Left-Skewed)": scores
}

# ----------------------------
# 2. Analyze and Plot
# ----------------------------

for name, data in datasets.items():
    
    df = pd.DataFrame(data, columns=["Values"])
    
    mean = df["Values"].mean()
    median = df["Values"].median()
    
    print("\n", name)
    print("Mean:", round(mean, 2))
    print("Median:", round(median, 2))
    
    # Check skew type
    if mean > median:
        print("This data is Right-Skewed")
    elif mean < median:
        print("This data is Left-Skewed")
    else:
        print("This data is Normally Distributed")
    
    # Plot Histogram
    plt.figure()
    plt.hist(df["Values"], bins=30)
    plt.title(name)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.show()
    
# task 2
    
import numpy as np
import pandas as pd

# ----------------------------
# 1. Create Simple Dataset
# ----------------------------

np.random.seed(42)

# Generate random marks of students
marks = np.random.normal(70, 10, 1000)

# Add some extreme marks (outliers)
marks = np.append(marks, [30, 120])

# Create DataFrame
df = pd.DataFrame(marks, columns=["Marks"])

# ----------------------------
# 2. Calculate Mean and Standard Deviation
# ----------------------------

mean = df["Marks"].mean()
std = df["Marks"].std()

print("Mean (μ):", round(mean, 2))
print("Standard Deviation (σ):", round(std, 2))

# ----------------------------
# 3. Calculate Z-Score
# Formula: Z = (x - μ) / σ
# ----------------------------

df["Z_score"] = (df["Marks"] - mean) / std

# ----------------------------
# 4. Find Outliers (|Z| > 3)
# ----------------------------

outliers = df[abs(df["Z_score"]) > 3]

print("\nOutliers (|Z| > 3):")
print(outliers)

# task 3

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)

# Skewed population (e.g., incomes)
population = np.random.lognormal(mean=10, sigma=1.0, size=100_000)

sample_means = []

for _ in range(1000):
    sample = np.random.choice(population, size=30, replace=False)
    sample_means.append(sample.mean())
plt.figure(figsize=(7,4))
plt.hist(sample_means, bins=30)
plt.title("Distribution of Sample Means (n = 30, samples = 1000)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()
