# Solution to Question 2
import pandas as pd

# Re-create the dataset 
data = {
    'guest_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 1, 2],
    'visit_date': [
        '2024-07-05', '2024-07-08', '2024-07-10', '2024-07-12', '2024-07-15',
        '2024-07-18', '2024-07-20', '2024-07-21', '2024-07-22', '2024-07-23',
        '2024-07-25', '2024-07-26', '2024-07-28', '2024-07-28', '2024-07-28',
        '2024-07-29', '2024-07-30', '2024-07-31', '2024-07-05', '2024-07-08'
    ],
    'amount_spent': [
        50, 30, 28.5, 40, 25, 22, 55, 48, 30, 35,
        60, 15, 28, 20, 45, 38, 26, 18, 25, 30
    ],
    'park_experience_type': [
        'Attraction', 'Dining', 'Retail', 'Entertainment', 'Dining',
        'Dining', 'Attraction', 'Dining', 'Dining', 'Attraction',
        'Retail', 'Entertainment', 'Dining', 'Character Meet', 'Retail',
        'Dining', 'Entertainment', 'Character Meet', 'Dining', 'Character Meet'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)
df['visit_date'] = pd.to_datetime(df['visit_date'])

# Update the DataFrame to include some sample August 2024 data
# For now, simulate a few August visits by copying some rows and adjusting the dates
august_visits = pd.DataFrame({
    'guest_id': [1, 1, 2, 2, 3, 4],
    'visit_date': ['2024-08-01', '2024-08-20', '2024-08-05', '2024-08-25', '2024-08-15', '2024-08-30'],
    'amount_spent': [40, 70, 20, 60, 35, 50],
    'park_experience_type': ['Dining', 'Retail', 'Dining', 'Attraction', 'Entertainment', 'Retail']
})
august_visits['visit_date'] = pd.to_datetime(august_visits['visit_date'])

# Append the August data to the original DataFrame
df_augmented = pd.concat([df, august_visits], ignore_index=True)

# Filter to August 2024 visits
august_df = df_augmented[
    (df_augmented['visit_date'].dt.month == 8) & 
    (df_augmented['visit_date'].dt.year == 2024)
]

# Keep only guests with more than one visit
visit_counts = august_df.groupby('guest_id')['visit_date'].count()
repeat_visitors = visit_counts[visit_counts > 1].index
repeat_visits_df = august_df[august_df['guest_id'].isin(repeat_visitors)]

# Get first and last visit spending for each guest
first_last_spending = (
    repeat_visits_df.sort_values(by=['guest_id', 'visit_date'])
    .groupby('guest_id')
    .agg(first_visit_spent=('amount_spent', 'first'), last_visit_spent=('amount_spent', 'last'))
)

# Calculate the difference in spending
first_last_spending['spending_difference'] = (
    first_last_spending['last_visit_spent'] - first_last_spending['first_visit_spent']
)

print (first_last_spending.reset_index())
