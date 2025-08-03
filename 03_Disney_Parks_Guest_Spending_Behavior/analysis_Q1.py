# Solution to Question 1
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


# Filter data to include only visits from July 2024
july_df = df[(df['visit_date'].dt.month == 7) & (df['visit_date'].dt.year == 2024)]

# Calculate average spending per guest per experience type
# (total spent / number of guest visits per experience type)
avg_spending = (
    july_df.groupby('park_experience_type')
    .agg(total_spent=('amount_spent', 'sum'), total_visits=('guest_id', 'count'))
    .assign(avg_spending_per_guest=lambda x: x['total_spent'] / x['total_visits'])
    .reset_index()
)

#Ensure all experience types are included, even those with no transactions
all_types = pd.DataFrame({
    'park_experience_type': ['Attraction', 'Dining', 'Retail', 'Entertainment', 'Character Meet', 'Parade']
})

# Merge and fill missing averages with 0.0
final_result = pd.merge(all_types, avg_spending[['park_experience_type', 'avg_spending_per_guest']], 
                        on='park_experience_type', how='left')
final_result['avg_spending_per_guest'] = final_result['avg_spending_per_guest'].fillna(0.0)

print('The result is' ,final_result.sort_values(by='park_experience_type'))
