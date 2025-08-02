# Solution to Question 2 
import pandas as pd
# Create the DataFrames
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

# Filter for October 2024 and merge with product data
ad_performance['recorded_date'] = pd.to_datetime(ad_performance['recorded_date'])
october_ads = ad_performance[ad_performance['recorded_date'].dt.month == 10]
merged_data = pd.merge(october_ads, products, on='product_id')

# Calculate CTR for each ad
merged_data['CTR'] = (merged_data['clicks'] / merged_data['impressions']) * 100

# Calculate overall average CTR
overall_avg_ctr = merged_data['CTR'].mean()

# Calculate average CTR by category
category_ctr = merged_data.groupby('product_category')['CTR'].mean().round(2)

# Identify high-performing categories
high_performing_categories = category_ctr[category_ctr > overall_avg_ctr].sort_values(ascending=False)

# Display results
print(f"Overall Average CTR (October 2024): {overall_avg_ctr:.2f}%\n")
print("Categories Performing Above Average:")
print(high_performing_categories.to_string())