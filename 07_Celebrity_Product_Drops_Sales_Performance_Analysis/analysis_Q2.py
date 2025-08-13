#Solution for Question 2

import pandas as pd

# Create DataFrame from the provided data
data = {
    'sale_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    'sale_date': [
        '2025-01-10', '2025-01-15', '2025-02-03', '2025-03-12', '2025-03-20',
        '2025-02-28', '2025-03-25', '2025-03-30', '2025-01-20', '2025-02-05',
        '2025-03-01', '2025-02-15', '2025-03-15', '2025-01-25', '2025-02-20',
        '2025-03-28', '2024-11-15', '2024-07-30'
    ],
    'product_id': [901, 901, 902, 903, 904, 901, 902, 905, 903, 906, 907, 908, 909, 910, 905, 902, 901, 902],
    'sale_amount': [
        None, 1500, 2000.5, 2500.75, None, 1000, 300, 1800, 1200, 500,
        2200, 1300, None, 900, 700, 1500, 800, 1000
    ],
    'celebrity_id': [101, 101, 102, 103, 104, 101, 102, 105, 103, 106, 107, 101, 102, 108, 105, 102, 101, 102]
}

df = pd.DataFrame(data)

# Convert sale_date to datetime
df['sale_date'] = pd.to_datetime(df['sale_date'])

# Filter for Q1 2025 (Jan 1 - Mar 31)
q1_2025 = df[
    (df['sale_date'] >= '2025-01-01') &
    (df['sale_date'] <= '2025-03-31')
]

# Get unique celebrity-product combinations
unique_collabs = q1_2025[['celebrity_id', 'product_id']].drop_duplicates()

# Sort for better readability
unique_collabs = unique_collabs.sort_values(['celebrity_id', 'product_id'])

# Display results
print("Unique Celebrity-Product Collaborations (Q1 2025)")
print("="*50)
print(unique_collabs.to_string(index=False, header=True))