#Solution to Question 3

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

# Data Cleaning
def clean_rating(rating):
    if pd.isna(rating) or rating == '':
        return np.nan
    
    rating = str(rating).strip()
    rating = rating.replace(',', '.')
    
    word_to_num = {'five': '5', 'one': '1', 'two': '2', 
                   'three': '3', 'four': '4'}
    if rating.lower() in word_to_num:
        rating = word_to_num[rating.lower()]
    
    try:
        rating_float = float(rating)
        return rating_float if 1 <= rating_float <= 5 else np.nan
    except:
        return np.nan

df['rating'] = df['rating'].apply(clean_rating)
df['review_date'] = pd.to_datetime(df['review_date'])

# Correct aggregation approach
category_stats = df.groupby('category')['rating'].agg(
    ['mean', 'median', 'std', 'count']
).reset_index()

# Rename columns
category_stats.columns = [
    'category', 
    'mean_rating', 
    'median_rating', 
    'std_deviation', 
    'count_ratings'
]

# Format results
category_stats['mean_rating'] = category_stats['mean_rating'].round(2)
category_stats['std_deviation'] = category_stats['std_deviation'].round(2)

# Display results
print("App Rating Statistics by Category")
print("="*60)
print(category_stats.to_string(index=False))

print("\nKey Insights:")
print(f"- Highest average rating: {category_stats.loc[category_stats['mean_rating'].idxmax()]['category']} ({category_stats['mean_rating'].max():.2f})")
print(f"- Most consistent ratings: {category_stats.loc[category_stats['std_deviation'].idxmin()]['category']} (σ={category_stats['std_deviation'].min():.2f})")
print(f"- Most rated category: {category_stats.loc[category_stats['count_ratings'].idxmax()]['category']} ({category_stats['count_ratings'].max()} ratings)")