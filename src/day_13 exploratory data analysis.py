# task 1


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample housing dataset
df = pd.read_excel("Housing_with_City.xlsx")

# 1. Histogram with KDE

sns.histplot(df["price"], kde=True)
plt.title("Distribution of Housing prices")
plt.xlabel("price")
plt.ylabel("Frequency")
plt.show()

# 2. Skewness and Kurtosis
print("Skewness:", df["price"].skew())
print("Kurtosis:", df["price"].kurt())

# 3. Count Plot for categorical column
sns.countplot(x="City", data=df)
plt.title("City Frequency")
plt.show()

#task 2

#task2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("Housing_with_City.xlsx")

# 1. Scatter Plot: Area vs Price
plt.scatter(df["area"], df["price"])
plt.title("House Area vs price")
plt.xlabel("Area (Square Footage)")
plt.ylabel("price")
plt.show()

# 2. Boxplot: City vs Price
sns.boxplot(x="City", y="price", data=df)
plt.title("Price Distribution by City")
plt.xlabel("City")
plt.ylabel("Price")
plt.show()

#task 3


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("Housing_with_City.xlsx")

# 1. Correlation Matrix
corr_matrix = df.corr(numeric_only=True)
print(corr_matrix)

# Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 2. Boxplot for outliers (Price)
sns.boxplot(y=df["price"])
plt.title("Outliers in Housing Prices")
plt.ylabel("Price")
plt.show()
