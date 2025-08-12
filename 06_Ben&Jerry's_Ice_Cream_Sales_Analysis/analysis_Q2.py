#Solution to Q2:

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



# Create DataFrame (using cleaned data from previous step)
data = [
    # [All cleaned data rows]
]
df = pd.DataFrame(data, columns=["sale_date", "temperature", "product_name", "sales_volume", "transaction_id"])

# Convert sale_date to datetime and extract month
df['sale_date'] = pd.to_datetime(df['sale_date'])
df['month'] = df['sale_date'].dt.month_name()

# Define temperature bins and labels
bins = [0, 60, 70, 80, 90, float('inf')]
labels = ['<60°F', '60-69°F', '70-79°F', '80-89°F', '90°F+']

# Categorize temperatures
df['temp_range'] = pd.cut(df['temperature'], bins=bins, labels=labels, right=False)

# Create pivot table
pivot_table = pd.pivot_table(
    df,
    values='sales_volume',
    index='month',
    columns='temp_range',
    aggfunc='sum',
    fill_value=0,
    margins=True,
    margins_name='Total'
)

# Reorder months chronologically
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
pivot_table = pivot_table.reindex(month_order)

print("Ice Cream Sales Volume by Month and Temperature Range:")
print(pivot_table)

# Export to CSV
pivot_table.to_csv('ice_cream_sales_by_month_temp.csv')