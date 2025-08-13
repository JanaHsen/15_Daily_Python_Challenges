#Solution to Question 1

import pandas as pd
import numpy as np

# Create DataFrame from the provided data
data = {
    'app_id': ['app001', 'app002', 'app001', 'app003', 'app004', 'app005', 'app006', 
               'app007', 'app008', 'app009', 'app010', 'app011', 'app012', 'app013',
               'app014', 'app015', 'app016', 'app017', 'app018', 'app019', 'app020',
               'app002', 'app003', 'app001', 'app004', 'app005', 'app006', 'app007',
               'app008', 'app009', 'app010', 'app011', 'app012', 'app013', 'app014',
               'app015', 'app016', 'app017', 'app018', 'app019', 'app020', 'app002',
               'app003', 'app004', 'app005', 'app006', 'app007', 'app008', 'app009'],
    'rating': ['4.5', '3.9', '4.7', '4.0', 'five', '', '4.2', '4', '3.5', '4.9', 
               '4,2', '3.5', '4.0', '2.1', '3.8', '4.5', '3.3', '4.8', '4.6', '',
               '3.2', '3.7', '4.0', '4.6', '5', '6.0', '4.1', '3.0', '4.2', '4.4',
               '3.5', '4.0', '4.3', '4.1', 'not available', '3.9', '4.6', '4.0',
               '3.8', '4.2', '4.7', '3.8', '4.3', '4.4', '4.5', '4.0', '', '4.6',
               '3.9'],
    'category': ['Games', 'Productivity', 'Games', 'Health & Fitness', 'Education', 
                'Games', 'Lifestyle', 'Utilities', 'Entertainment', 'Health & Fitness',
                'Games', 'Productivity', 'Education', 'Games', 'Lifestyle', 'Games',
                'Utilities', 'Entertainment', 'Health & Fitness', 'Education', 'Games',
                'Productivity', 'Health & Fitness', 'Games', 'Education', 'Games',
                'Lifestyle', 'Utilities', 'Entertainment', 'Health & Fitness', 'Games',
                'Productivity', 'Education', 'Games', 'Lifestyle', 'Games', 'Utilities',
                'Entertainment', 'Health & Fitness', 'Education', 'Games', 'Productivity',
                'Health & Fitness', 'Education', 'Games', 'Lifestyle', 'Utilities',
                'Entertainment', 'Health & Fitness'],
    'review_date': ['2024-07-05', '2024-07-06', '2024-07-10', '2024-08-15', '2024-09-01',
                   '2024-10-11', '2024-10-20', '2024-11-15', '2024-12-01', '2024-12-15',
                   '2025-01-07', '2025-01-15', '2025-01-20', '2025-02-14', '2025-02-20',
                   '2025-03-03', '2025-03-12', '2025-03-20', '2025-04-01', '2025-04-10',
                   '2025-04-15', '2025-04-20', '2025-05-01', '2025-05-05', '2025-05-11',
                   '2025-05-13', '2025-05-15', '2025-05-20', '2025-06-02', '2025-06-07',
                   '2025-06-10', '2025-06-12', '2025-06-15', '2025-06-18', '2025-06-20',
                   '2025-06-21', '2025-06-22', '2024-07-07', '2024-07-08', '2024-07-09',
                   '2024-07-10', '2024-07-11', '2024-07-12', '2024-07-13', '2024-07-14',
                   '2024-07-15', '2024-07-16', '2024-07-17', '2024-07-18']
}

df = pd.DataFrame(data)

# Convert review_date to datetime
df['review_date'] = pd.to_datetime(df['review_date'])

# Clean rating column
def clean_rating(rating):
    if pd.isna(rating) or rating == '':
        return np.nan
    
    # Remove whitespace
    rating = str(rating).strip()
    
    # Handle comma decimals
    rating = rating.replace(',', '.')
    
    # Convert word numbers to digits
    word_to_num = {'five': '5', 'one': '1', 'two': '2', 
                   'three': '3', 'four': '4'}
    if rating.lower() in word_to_num:
        rating = word_to_num[rating.lower()]
    
    # Convert to float if possible
    try:
        return float(rating)
    except:
        return np.nan

df['rating'] = df['rating'].apply(clean_rating)

# Validate ratings are between 1-5 (standard rating scale)
df['rating'] = df['rating'].apply(lambda x: x if 1 <= x <= 5 else np.nan)

# Show cleaning results
print("Data Cleaning Summary")
print("="*40)
print(f"Original records: {len(df)}")
print(f"Valid ratings after cleaning: {df['rating'].notna().sum()}")
print(f"Invalid ratings cleaned: {len(df) - df['rating'].notna().sum()}")
print("\nSample of cleaned data:")
print(df.head(10).to_string())

# Show distribution of cleaned ratings
print("\nRating Distribution After Cleaning:")
print(df['rating'].describe())