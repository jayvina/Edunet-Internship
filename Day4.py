"""
File Name : 11-07-2026.py
Subject   : Python Data Analysis using Pandas

Dataset:
Global Data on Sustainable Energy (2000-2020)

Instructions Completed:
1. Import dataset
2. Analyze dataset
3. Handle null values
4. Study relations between columns
5. Summarize work
"""

import pandas as pd

# ============================================================
# STEP 1 : Import Dataset
# Download the dataset and keep it in the same folder.
# File name: global-data-on-sustainable-energy.csv
# ============================================================

df = pd.read_csv("global-data-on-sustainable-energy.csv")

print("="*60)
print("FIRST FIVE RECORDS")
print("="*60)
print(df.head())

# ============================================================
# STEP 2 : Dataset Information
# ============================================================

print("\nShape of Dataset:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nDataset Information")
df.info()

print("\nStatistical Summary")
print(df.describe())

# ============================================================
# STEP 3 : Checking Null Values
# ============================================================

print("\nNull Values Before Cleaning")
print(df.isnull().sum())

# Numerical columns -> Median
# Categorical columns -> Mode

for col in df.columns:
    if df[col].dtype == "object":
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        df[col].fillna(df[col].median(), inplace=True)

print("\nNull Values After Cleaning")
print(df.isnull().sum())

# ============================================================
# STEP 4 : General Analysis
# ============================================================

print("\nNumber of Rows:", len(df))
print("Number of Columns:", len(df.columns))

if "Country" in df.columns:
    print("Unique Countries:", df["Country"].nunique())

if "Year" in df.columns:
    print("Years Covered:", df["Year"].min(), "-", df["Year"].max())

# ============================================================
# STEP 5 : Relation Between Columns
# ============================================================

"""
General Observations

1. Higher electricity access generally improves GDP.
2. Renewable energy production is positively related to clean energy usage.
3. Higher CO2 emissions are usually linked with industrial development.
4. Countries with higher GDP often have better electricity access.
5. Population growth increases energy demand.
6. Renewable energy share helps reduce dependence on fossil fuels.
7. Energy production and energy consumption are positively related.
8. Correlation matrix helps identify positive and negative relationships.
"""

print("\nCorrelation Matrix")
numeric_df = df.select_dtypes(include="number")
print(numeric_df.corr())

# ============================================================
# STEP 6 : Pandas Operations
# ============================================================

print("\nFirst 10 Records")
print(df.head(10))

print("\nLast 5 Records")
print(df.tail())

print("\nSorted by Year")
if "Year" in df.columns:
    print(df.sort_values("Year").head())

print("\nAverage of Numerical Columns")
print(df.mean(numeric_only=True))

print("\nMaximum Values")
print(df.max(numeric_only=True))

print("\nMinimum Values")
print(df.min(numeric_only=True))

# ============================================================
# SUMMARY
# ============================================================

print("\n" + "="*60)
print("SUMMARY")
print("="*60)

print("""
1. Imported sustainability dataset using Pandas.
2. Displayed dataset information and statistics.
3. Checked missing values.
4. Filled numerical null values using Median.
5. Filled categorical null values using Mode.
6. Performed basic analysis.
7. Studied relationships between columns.
8. Generated correlation matrix.
9. Applied several Pandas functions:
   head(), tail(), info(), describe(), shape,
   columns, isnull(), fillna(), sort_values(),
   mean(), max(), min(), corr().
10. Dataset analysis completed successfully.
""")
