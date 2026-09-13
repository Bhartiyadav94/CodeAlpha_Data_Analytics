import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_dataset.csv")

# Convert price into numeric value
df["Price_Numeric"] = df["Price"].str.replace("£", "", regex=False).astype(float)

# -------------------------------
# 1. Bar Chart - Top 10 Expensive Books
# -------------------------------

top10 = df.nlargest(10, "Price_Numeric")

plt.figure(figsize=(10, 6))
plt.bar(top10["Book Title"], top10["Price_Numeric"])
plt.title("Top 10 Expensive Books")
plt.xlabel("Book Title")
plt.ylabel("Price (£)")
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()


# -------------------------------
# 2. Histogram - Price Distribution
# -------------------------------

plt.figure(figsize=(8, 5))
plt.hist(df["Price_Numeric"], bins=10)
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.show()


# -------------------------------
# 3. Pie Chart - Availability
# -------------------------------

availability = df["Availability"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(
    availability,
    labels=availability.index,
    autopct="%1.1f%%"
)
plt.title("Book Availability")
plt.show()


# -------------------------------
# 4. Line Chart - Book Prices
# -------------------------------

plt.figure(figsize=(10, 5))
plt.plot(df.index + 1, df["Price_Numeric"], marker="o")
plt.title("Book Prices")
plt.xlabel("Book Number")
plt.ylabel("Price (£)")
plt.grid(True)
plt.tight_layout()
plt.show()


# -------------------------------
# 5. Display Summary
# -------------------------------

print("===== DATA VISUALIZATION SUMMARY =====")
print("Total Books:", len(df))
print("Average Price: £", round(df["Price_Numeric"].mean(), 2))
print("Highest Price: £", df["Price_Numeric"].max())
print("Lowest Price: £", df["Price_Numeric"].min())

print("\nVisualization completed successfully!")
