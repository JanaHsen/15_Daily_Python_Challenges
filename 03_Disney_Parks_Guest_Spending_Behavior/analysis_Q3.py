# Solution to Question 3
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

# Filter for September 2024
df['visit_date'] = pd.to_datetime(df['visit_date'])
sept_data = df[(df['visit_date'] >= '2024-09-01') & (df['visit_date'] <= '2024-09-30')]

# Group by guest and sum
total_spending = sept_data.groupby('guest_id')['amount_spent'].sum().reset_index()

# Exclude guests with no purchases
total_spending = total_spending[total_spending['amount_spent'] > 0]

# Categorize into segments
def categorize(spend):
    if spend < 50:
        return 'Low'
    elif spend < 100:
        return 'Medium'
    else:
        return 'High'

total_spending['spending_segment'] = total_spending['amount_spent'].apply(categorize)

# Final result
print(total_spending)
