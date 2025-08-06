#Solution to Q3


import pandas as pd

# Create the DataFrame from the provided data
data = [
    # First table data
    ["North America", "C08:1", "2024-07-02", "Gamer", 1],
    ["Europe", "C08:2", "2024-07-03", "Casual", 2],
    ["Asia", "C08:3", "2024-07-04", "Tech Enthusiast", 1],
    ["Latin America", "C08:4", "2024-07-05", "Family", 3],
    ["Oceania", "C08:5", "2024-07-06", "Student", 2],
    ["North America", "C08:6", "2024-07-07", "Gamer", 5],
    ["Europe", "C08:7", "2024-07-08", None, 2],
    [None, "C08:8", "2024-07-09", "Casual", 1],
    ["Asia", "C08:9", "2024-07-10", "Family", 4],
    ["North America", "C08:10", "2024-07-11", "Gamer", 1],
    ["North America", "C08:11", "2024-07-12", "Student", 2],
    ["Europe", "C08:12", "2024-07-13", "Casual", 3],
    ["Latin America", "C08:13", "2024-07-14", "Tech Enthusiast", 2],
    ["Oceania", "C08:14", "2024-07-15", "Gamer", 5],
    ["North America", "C08:15", "2024-07-16", "Casual", 1],
    ["Europe", "C08:16", "2024-07-17", "Family", 4],
    ["Asia", "C08:17", "2024-07-18", "Student", 3],
    ["Latin America", "C08:18", "2024-07-19", "Gamer", 1],
    
    # Second table data
    ["Oceania", "C019", "2024-07-20", "Tech Enthusiast", 2],
    ["Oceania", "C019", "2024-07-20", "Tech Enthusiast", 2],
    ["North America", "C020", "2024-07-21", "Family", 3],
    ["Europe", "C021", "2024-07-22", "Gamer", 2],
    ["Asia", "C022", "2024-07-23", "Casual", 1],
    ["Latin America", "C023", "2024-07-24", "Student", 4],
    ["Oceania", "C024", "2024-07-25", "Family", 2],
    ["North America", "C025", "2024-07-26", "Tech Enthusiast", 1],
    ["Europe", "C026", "2024-07-27", "Student", 5],
    ["Asia", "C027", "2024-07-28", "Gamer", 2],
    ["Latin America", "C028", "2024-07-29", "Casual", 3],
    ["Oceania", "C029", "2024-07-30", "Family", 1],
    ["North America", "C030", "2024-08-01", "Gamer", 1],
    ["Asia", "C031", "2024-08-02", None, 2],
    ["Latin America", "C032", "2024-08-03", "Tech Enthusiast", 3],
    ["Oceania", "C033", "2024-08-04", "Student", 1],
    ["North America", "C034", "2024-08-05", "Family", 4],
    ["Europe", "C035", "2024-08-06", "Gamer", 2],
    ["Asia", "C036", "2024-08-07", "Casual", 5],
    ["Latin America", "C037", "2024-08-08", "Family", 1],
    
    # Additional text data
    ["Oceania", "C038", "2024-08-09", "Tech Enthusiast", 2],
    ["North America", "C039", "2024-08-10", "Student", 10],
    ["Europe", "C040", "2024-08-11", "Family", 3],
    ["Asia", "C041", "2024-08-12", "Gamer", 1],
    ["Latin America", "C042", "2024-08-13", "Casual", 2],
    ["Oceania", "C043", "2024-08-14", "Student", 5],
    ["North America", "C044", "2024-08-15", "Tech Enthusiast", 2],
    ["Europe", "C045", "2024-08-16", "Family", 1],
    ["Asia", "C046", "2024-08-17", "Gamer", 3],
    ["Latin America", "C047", "2024-08-18", "Casual", 2],
    ["Oceania", "C048", "2024-08-19", None, 4],
    ["North America", "C049", "2024-08-20", "Student", 1],
    ["Europe", "C050", "2024-08-21", "Gamer", 2],
    ["Asia", "C051", "2024-08-22", "Casual", 3],
    ["Latin America", "C052", "2024-08-23", "Tech Enthusiast", 2],
    ["Oceania", "C053", "2024-08-24", "Family", 1],
    ["North America", "C054", "2024-08-25", "Gamer", 1],
    ["Europe", "C055", "2024-08-26", "Casual", 2]
]

df = pd.DataFrame(data, columns=["region", "customer_id", "pre_order_date", "demographic_group", "pre_order_quantity"])

# Fix typos in the data
df['region'] = df['region'].replace({'Oceania': 'Oceania', 'Oceania': 'Oceania'})
df['demographic_group'] = df['demographic_group'].replace({'Tech Enthusiast': 'Tech Enthusiast', 'Tech Enthusiast': 'Tech Enthusiast'})

# Calculate percentage of records with missing values
total_records = len(df)
missing_values = df.isnull().any(axis=1).sum()
percentage_missing = (missing_values / total_records) * 100

print(f"Total records: {total_records}")
print(f"Records with missing values: {missing_values}")
print(f"Percentage of records with missing values: {percentage_missing:.2f}%")

# Handle missing values
# Remove rows with missing region (only 1 row)
df_cleaned = df.dropna(subset=['region'])

# Fill missing demographic_group with 'Unknown'
df_cleaned['demographic_group'] = df_cleaned['demographic_group'].fillna('Unknown')

# Verify no missing values remain
print("\nAfter cleaning:")
print(f"Total records remaining: {len(df_cleaned)}")
print(f"Missing values in each column:\n{df_cleaned.isnull().sum()}")

# Save cleaned dataset
df_cleaned.to_csv('cleaned_pre_sale_data.csv', index=False)
print("\nCleaned dataset saved to 'cleaned_pre_sale_data.csv'")

# Convert pre_order_date to datetime and extract month
df_cleaned['pre_order_date'] = pd.to_datetime(df_cleaned['pre_order_date'])
df_cleaned['month'] = df_cleaned['pre_order_date'].dt.month_name()

# Group by month, region, and demographic_group, then sum pre_order_quantity
monthly_region_demo_sales = df_cleaned.groupby(
    ['month', 'region', 'demographic_group']
)['pre_order_quantity'].sum().reset_index()

# Pivot for better visualization (optional)
pivot_table = monthly_region_demo_sales.pivot_table(
    index=['month', 'region'],
    columns='demographic_group',
    values='pre_order_quantity',
    aggfunc='sum',
    fill_value=0
)

# Print results
print("Total Pre-Sale Orders by Month, Region, and Demographic Group:")
print(monthly_region_demo_sales.to_string(index=False))

print("\nPivot Table View:")
print(pivot_table)

# Save results to CSV
monthly_region_demo_sales.to_csv('monthly_region_demographic_sales.csv', index=False)
pivot_table.to_csv('monthly_region_demographic_sales_pivot.csv')

print("\nResults saved to CSV files")

# df_cleaned = pd.read_csv('cleaned_pre_sale_data.csv')

# Ensure datetime and extract month
df_cleaned['pre_order_date'] = pd.to_datetime(df_cleaned['pre_order_date'])
df_cleaned['month'] = df_cleaned['pre_order_date'].dt.month_name()

# 1. Calculate total pre-orders by region for July and August
monthly_totals = df_cleaned.groupby(['month', 'region'])['pre_order_quantity'].sum().unstack(level=0)

# Filter only July and August (in case other months exist)
monthly_totals = monthly_totals[['July', 'August']]

# 2. Calculate growth rates
monthly_totals['growth_rate'] = (monthly_totals['August'] - monthly_totals['July']) / monthly_totals['July']

# 3. Forecast September
monthly_totals['September_forecast'] = monthly_totals['August'] * (1 + monthly_totals['growth_rate'])

# Format results
result = monthly_totals[['July', 'August', 'growth_rate', 'September_forecast']]
result['growth_rate'] = result['growth_rate'].apply(lambda x: f"{x:.1%}")
result['September_forecast'] = result['September_forecast'].round().astype(int)

print("Pre-Sales Analysis by Region:")
print(result.to_string())

# Export results
result.to_csv('pre_sales_forecast_by_region.csv')