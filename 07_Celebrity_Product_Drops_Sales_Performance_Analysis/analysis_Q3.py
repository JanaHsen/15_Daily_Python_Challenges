#Solution for Question 3

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

# Convert sale_date to datetime and filter for Q1 2025
df['sale_date'] = pd.to_datetime(df['sale_date'])
q1_2025 = df[(df['sale_date'] >= '2025-01-01') & (df['sale_date'] <= '2025-03-31')]

# Group by celebrity-product collaboration and sum sales (excluding null values)
collab_sales = q1_2025.groupby(['celebrity_id', 'product_id'])['sale_amount'].sum().reset_index()

# Sort by total sales in descending order
ranked_collabs = collab_sales.sort_values('sale_amount', ascending=False)

# Get top 3 collaborations
top_3_collabs = ranked_collabs.head(3)

# Display results
print("Top 3 Celebrity-Product Collaborations by Sales (Q1 2025)")
print("="*60)
print(top_3_collabs.to_string(index=False, float_format='%.2f', header=True))

