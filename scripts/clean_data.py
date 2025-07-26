import os
import pandas as pd

# Paths
RAW_DATA_PATH = './data/raw/world_bank_iran_data.csv'
PROCESSED_DATA_PATH = './data/processed/cleaned_iran_data.csv'

print("--- Cleaning Data ---")
# Load the data
try:
    df = pd.read_csv(RAW_DATA_PATH)
    print(f"✅ Loaded {len(df)} rows from {RAW_DATA_PATH}")
    print(f"Shape of the data: {df.shape}")
except FileNotFoundError:
    print(f"❌ File not found at {RAW_DATA_PATH}")
    exit(1)

# Primary Cleaning
print("\n--- Initial Data Inspection")
print(df.info())

# Check for missing values
print("\n--- Missing Values Check Before Cleaning ---")
print(df.isnull().sum())

df['agricultural_land_sqkm'] = df['agricultural_land_sqkm'].fillna(method='ffill')

print("\n--- Missing Values Check After Cleaning ---")
print(df.isnull().sum())

# Final Data Inspection
df['population'] = df['population'].astype(int)
df['year'] = df['year'].astype(int)

print("\n--- Final Data Inspection ---")
print(df.info())
print("\n--- First 5 rows of the cleaned data ---")
print(df.head())

# Save the cleaned data 
# Create the output directory if it doesn't exist
os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)

# Save the cleaned data
df.to_csv(PROCESSED_DATA_PATH, index=False)
print(f"✅ Data cleaning completed. Cleaned data saved to {PROCESSED_DATA_PATH}")
