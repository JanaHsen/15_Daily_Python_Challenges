#Solution to Question 1

import pandas as pd

# Create DataFrames (same as previous solution)
ad_performance = pd.DataFrame({
    'ad_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
    'product_id': [1, 1, 2, 2, 3, 3, 4, 5, 6, 8, 9, 11, 11, 12, 2],
    'clicks': [10, 15, 20, 18, 5, 12, 50, 8, 14, 22, 30, 7, 13, 9, 16],
    'impressions': [200, 300, 250, 230, 150, 180, 500, 250, 200, 220, 300, 120, 150, 190, 160],
    'recorded_date': ['2024-10-02', '2024-10-12', '2024-10-05', '2024-10-29', 
                    '2024-10-15', '2024-10-25', '2024-10-07', '2024-10-13', 
                    '2024-10-19', '2024-10-30', '2024-10-08', '2024-10-22', 
                    '2024-10-28', '2024-10-11', '2024-11-01']
})

products = pd.DataFrame({
    'product_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'product_category': ['Home Electronics', 'Electronics & Gadgets', 'Electronics Appliances',
                       'Books', 'Fashion', 'Kitchen', 'Outdoor', 'Home Electronics',
                       'Electronics Accessories', 'Health & Beauty', 'Electronics Gadgets']
})

# Process data (same as before)
ad_performance['recorded_date'] = pd.to_datetime(ad_performance['recorded_date'])
october_ads = ad_performance[ad_performance['recorded_date'].dt.month == 10]
merged_data = pd.merge(october_ads, products, on='product_id')
merged_data['CTR'] = (merged_data['clicks'] / merged_data['impressions']) * 100

# Calculate metrics
overall_avg_ctr = merged_data['CTR'].mean()
category_stats = merged_data.groupby('product_category').agg(
    avg_ctr=('CTR', 'mean'),
    total_clicks=('clicks', 'sum'),
    total_impressions=('impressions', 'sum')
).round(2)

# Filter high-performing categories (from previous question)
high_performers = category_stats[category_stats['avg_ctr'] > overall_avg_ctr]

# Calculate percentage difference from overall average
high_performers['pct_difference'] = ((high_performers['avg_ctr'] - overall_avg_ctr) / overall_avg_ctr) * 100
high_performers = high_performers.sort_values('pct_difference', ascending=False)

# Format results
results = high_performers[['avg_ctr', 'pct_difference']].rename(columns={
    'avg_ctr': 'Category CTR (%)',
    'pct_difference': 'Performance Gap (%)'
})

print(f"Overall Average CTR: {overall_avg_ctr:.2f}%\n")
print("High-Performing Categories vs. Overall Average:")
print(results.to_string())