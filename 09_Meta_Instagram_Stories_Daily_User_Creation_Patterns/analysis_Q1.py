#Solution to Question 1

import pandas as pd
import numpy as np

# Create DataFrame from the provided data
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

# Clean user_id column
df['user_id'] = df['user_id'].str.lower().replace('', np.nan)

# Convert story_date to datetime with multiple format handling
date_formats = ['%Y-%m-%d', '%m/%d/%Y', '%Y/%m/%d']
df['story_date'] = pd.to_datetime(df['story_date'], 
                                 format='mixed',  # Handles multiple formats automatically
                                 errors='coerce')  # Converts invalid dates to NaT

# Display cleaning results
print("Data Cleaning Summary")
print("="*40)
print(f"Original records: {len(df)}")
print(f"Missing user_ids: {df['user_id'].isna().sum()}")
print(f"Invalid/missing dates: {df['story_date'].isna().sum()}")
print("\nSample of cleaned data:")
print(df.head(10).to_string())

# Optional: Save cleaned data
clean_df = df.dropna(subset=['user_id', 'story_date']).copy()
