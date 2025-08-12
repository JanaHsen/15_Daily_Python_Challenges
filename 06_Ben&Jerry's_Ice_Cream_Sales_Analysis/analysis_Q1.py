#Solution to Q1:

import pandas as pd

# Create DataFrame from the provided data
data = [
    # [All the data rows from your input]
]

df = pd.DataFrame(data, columns=["sale_date", "temperature", "product_name", "sales_volume", "transaction_id"])

# Convert sale_date to datetime
df['sale_date'] = pd.to_datetime(df['sale_date'])

# Check for duplicates (considering all columns except transaction_id)
duplicates = df[df.duplicated(subset=['sale_date', 'product_name', 'sales_volume', 'temperature'], keep=False)]

print(f"Found {len(duplicates)} potential duplicate transactions")
print(duplicates.sort_values(['sale_date', 'product_name']))

# Remove duplicates (keeping first occurrence)
cleaned_df = df.drop_duplicates(
    subset=['sale_date', 'product_name', 'sales_volume', 'temperature'],
    keep='first'
)

print(f"\nOriginal records: {len(df)}")
print(f"Cleaned records: {len(cleaned_df)}")
print(f"Duplicates removed: {len(df) - len(cleaned_df)}")