# Solution to Question 1
import pandas as pd

# 1. Create the DataFrames from provided data
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
    'product_name': ['Smart TV', 'Wireless Earbuds', 'Refrigerator', 'Bestselling Novel',
                   'Designer Jeans', 'Blender', 'Tent', 'Smart Home Hub',
                   'Phone Charger', 'Skincare Set', 'Drone'],
    'product_category': ['Home Electronics', 'Electronics & Gadgets', 'Electronics Appliances',
                        'Books', 'Fashion', 'Kitchen', 'Outdoor', 'Home Electronics',
                        'Electronics Accessories', 'Health & Beauty', 'Electronics Gadgets']
})

# 2. Convert date column to datetime and filter for October 2024
ad_performance['recorded_date'] = pd.to_datetime(ad_performance['recorded_date'])
october_ads = ad_performance[
    (ad_performance['recorded_date'] >= '2024-10-01') & 
    (ad_performance['recorded_date'] <= '2024-10-31')
]

# 3. Merge with product data
merged_data = pd.merge(october_ads, products, on='product_id')

# 4. Filter for electronics categories
electronics_ads = merged_data[merged_data['product_category'].str.contains('Electronics', case=False)]

# 5. Calculate CTR for each ad
electronics_ads['CTR'] = (electronics_ads['clicks'] / electronics_ads['impressions']) * 100

# 6. Group by category and calculate average CTR
results = electronics_ads.groupby('product_category')['CTR'].mean().round(2).sort_values(ascending=False)

print("Average CTR by Electronics Category (October 2024):")
print(results.to_string())