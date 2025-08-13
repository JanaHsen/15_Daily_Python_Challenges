#Solution to Question 2

import pandas as pd
import numpy as np

# Create DataFrame from raw data
data = {
    'user_id': ['user_001', 'user_001', 'user_001', 'user_001', 'user_001', 'user_001',
                'user_002', 'user_002', 'user_002', 'user_002', 'user_002', 'user_002',
                'user_003', 'user_003', 'user_003', 'user_003', None, 'USER_003',
                'user_004', 'user_004', 'user_004', 'user_004', 'user_004', 'user_004',
                'user_005', 'user_005', 'user_005', 'user_005', 'user_005', 'user_005',
                'user_006', 'user_006', 'user_006', 'user_006', 'user_006', 'user_006',
                'user_007', 'user_007', 'user_007', 'user_007', 'user_007', 'user_007',
                'user_008', 'user_008', 'user_008', 'user_008', 'user_008', 'user_008',
                'user_009', 'user_009', 'user_009', 'user_009', 'user_009', 'user_009',
                'user_010', 'user_010', 'user_010', 'user_010', 'user_010', 'user_010'],
    'story_date': ['2024-07-03', '2024-07-03', '2024-08-15', '2024-09-10', '2024-10-05', '07/15/2024',
                   '2024-07-03', '2024-07-04', '', '2024-12-25', '2025-01-15', '2025-06-29',
                   '2024-07-10', '2024-08-20', '2024-08-20', '2025-03-11', '2025-03-12', '2025-04-01',
                   '2024-07-15', '2024-09-30', '2024/10/10', '2024-11-11', '2025-02-28', '2025-03-01',
                   '2024-08-01', '2024-08-02', '2024-08-03', '2024-08-04', '2024-08-05', '2024-08-06',
                   '2024-09-01', '2024-09-02', '2024-09-03', '2024-09-04', '2024-09-05', '',
                   '2024-10-10', '2024-10-11', '2024-10-12', '2024-10-13', '2024-10-14', '2024-10-15',
                   '2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05', '2025-01-06',
                   '2024-12-01', '2024-12-02', '2024-12-03', '2024-12-04', '2024-12-05', 'invalid_date',
                   '2025-03-15', '2025-03-16', '2025-03-17', '2025-03-18', '2025-03-19', '2025-03-20'],
    'story_count': [3, 3, 5, 0, 20, 2, 4, 3, 6, 1, 7, 10, 2, 8, 8, 5, 3, 4, 6, 7, 4, 3, 12, 0,
                    1, 2, 3, 4, None, 5, 9, 10, 9, 50, 8, 7, 4, 4, 4, 3, 2, 1, 11, 12, 13, 14, 15, 0,
                    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
}

df = pd.DataFrame(data)

# Data Cleaning
# 1. Standardize user_ids
df['user_id'] = df['user_id'].str.lower().replace('', np.nan)

# 2. Convert story_date to datetime
df['story_date'] = pd.to_datetime(df['story_date'], format='mixed', errors='coerce')

# 3. Remove rows with missing critical data
clean_df = df.dropna(subset=['user_id', 'story_date', 'story_count']).copy()

# Calculate daily totals per user
daily_totals = clean_df.groupby(['user_id', 'story_date'])['story_count'].sum().reset_index()

# Calculate percentiles
percentiles = np.percentile(daily_totals['story_count'], [25, 50, 75])

# Create results report
results = pd.DataFrame({
    'Percentile': ['25th (Q1)', '50th (Median)', '75th (Q3)'],
    'Stories per Day': percentiles,
    'Interpretation': [
        '25% of user-days have ≤ this many stories',
        'Half of user-days create more/less than this',
        '75% of user-days have ≤ this many stories'
    ]
})

# Output results
print("Instagram Stories Creation Analysis")
print("="*50)
print("\nData Cleaning Summary:")
print(f"- Original records: {len(df)}")
print(f"- Cleaned records: {len(daily_totals)}")
print(f"- Records removed: {len(df) - len(clean_df)} (invalid dates, missing user_ids, or missing counts)")

print("\nDaily Stories Per User (Percentiles):")
print(results.to_string(index=False))

print("\nAdditional Statistics:")
print(f"- Mean stories per day: {daily_totals['story_count'].mean():.1f}")
print(f"- Range: {daily_totals['story_count'].min()} to {daily_totals['story_count'].max()} stories")
print(f"- Total user-days analyzed: {len(daily_totals)}")
print("\nSample of Daily Totals:")
print(daily_totals.head().to_string(index=False))