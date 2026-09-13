import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_dataset.csv")

# 1. Display dataset
print("===== DATASET =====")
print(df)

# 2. Basic information
print("\n===== DATASET INFORMATION =====")
print(df.info())

# 3. Number of rows and columns
print("\n===== SHAPE =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 4. Column names
print("\n===== COLUMNS =====")
print(df.columns.tolist())

# 5. Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# 6. Check duplicate values
print("\n===== DUPLICATES =====")
print("Duplicate rows:", df.duplicated().sum())

# 7. Basic statistics
print("\n===== STATISTICS =====")
print(df.describe(include="all"))

# 8. Availability count
print("\n===== AVAILABILITY =====")
print(df["Availability"].value_counts())

# 9. Convert price into numerical value
df["Price_Numeric"] = df["Price"].str.replace("£", "", regex=False).astype(float)

print("\n===== PRICE ANALYSIS =====")
print("Average Price:", df["Price_Numeric"].mean())
print("Minimum Price:", df["Price_Numeric"].min())
print("Maximum Price:", df["Price_Numeric"].max())

# 10. Most expensive books
print("\n===== TOP 5 EXPENSIVE BOOKS =====")
print(df.nlargest(5, "Price_Numeric")[["Book Title", "Price"]])

# 11. Visualization - Price distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Price_Numeric"], bins=10)
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.show()

# 12. Visualization - Top 10 expensive books
top_books = df.nlargest(10, "Price_Numeric")

plt.figure(figsize=(10, 6))
plt.bar(top_books["Book Title"], top_books["Price_Numeric"])
plt.title("Top 10 Expensive Books")
plt.xlabel("Book Title")
plt.ylabel("Price (£)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# 13. Final conclusion
print("\n===== EDA CONCLUSION =====")
print("The dataset was explored successfully.")
print("Missing values and duplicate records were checked.")
print("Book prices were analyzed using statistical measures.")
print("Graphs were created to understand the distribution of prices.")
