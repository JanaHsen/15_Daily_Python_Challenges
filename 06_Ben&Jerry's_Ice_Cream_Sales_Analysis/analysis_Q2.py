#Solution to Question 2

import pandas as pd
import numpy as np

# Create the dataset as a dictionary
data = {
    'sale_date': [
        '2024-07-05', '2024-08-15', '2024-09-25', '2024-10-05', '2025-01-05',
        '2025-02-15', '2024-07-10', '2024-08-20', '2024-12-25', '2025-06-25',
        '2024-07-15', '2024-08-25', '2024-11-05', '2025-03-15', '2025-04-20'
    ],
    'temperature': [
        62, 64, 66, 68, 74, 105, 58, 92, 45, 82,
        72, 78, 65, 88, 76
    ],
    'product_name': [
        'Cherry Garcia', 'Chunky Monkey', 'Phish Food', 'Americone Dream', 'Chocolate Fudge Brownie',
        'Half Baked', 'New York Super Fudge Chunk', 'Cherry Garcia', 'Chunky Monkey', 'Phish Food',
        'Americone Dream', 'Chocolate Fudge Brownie', 'Half Baked', 'New York Super Fudge Chunk', 'Cherry Garcia'
    ],
    'sales_volume': [
        23, 26, 29, 32, 41, 80, 45, 38, 55, 42,
        37, 44, 51, 48, 39
    ],
    'transaction_id': [
        'TX0001', 'TX0002', 'TX0003', 'TX0004', 'TX0005',
        'TX0006', 'TX0007', 'TX0008', 'TX0009', 'TX0010',
        'TX0011', 'TX0012', 'TX0013', 'TX0014', 'TX0015'
    ]
}

# Create DataFrame from dictionary
df = pd.DataFrame(data)

# Convert sale_date to datetime and extract month
df['sale_date'] = pd.to_datetime(df['sale_date'])
df['month'] = df['sale_date'].dt.month_name()

# Define temperature bins exactly as specified
temperature_bins = [-np.inf, 60, 70, 80, 90, 100, np.inf]
bin_labels = [
    '<60°F', 
    '60-69°F', 
    '70-79°F', 
    '80-89°F', 
    '90-99°F', 
    '100°F+'
]

# Categorize temperatures with correct boundary handling
df['temp_range'] = pd.cut(
    df['temperature'],
    bins=temperature_bins,
    labels=bin_labels,
    right=False,
    include_lowest=True
)

# Create the pivot table
pivot_table = pd.pivot_table(
    df,
    values='sales_volume',
    index='month',
    columns='temp_range',
    aggfunc='sum',
    fill_value=0,
    margins=True
)

# Ensure chronological month ordering
month_order = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]
pivot_table = pivot_table.reindex(month_order)

# Display results
print("Ben & Jerry's Sales Analysis by Month and Temperature Range")
print("="*55)
print(pivot_table)

# Optional: Print the cleaned dataset
print("\nSample of Processed Data:")
print(df.head())