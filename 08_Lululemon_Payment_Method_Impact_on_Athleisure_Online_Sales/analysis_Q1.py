#Solution to Question 1

import pandas as pd

# Create DataFrame from the provided data
data = {
    'customer_id': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 
                   101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115, 116, 117, 118, 119, 120,
                   121, 122, 123, 124, 125, 126, 127, 128, 129, 130,
                   131, 132, 133, 134, 135, 136, 137, 138],
    'order_value': [250, 95, 75, 310, 65, 265, 290, 275, 280, 90,
                   275, 285, 280, 290, 270, 295, 280, 275, 285, 290,
                   270, 280, 295, 285, 280, 275, 285, 290, 270, 280,
                   275, 285, 290, 280, 275, 92, 88, 90, 85, 95,
                   90, 92, 88, 70, 72, 68, 70, 69],
    'payment_method': ['credit_card', 'debit_card', 'paypal', 'credit_card', 'paypal',
                      'credit_card', 'credit_card', 'credit_card', 'credit_card', 'debit_card',
                      'credit_card', 'credit_card', 'credit_card', 'credit_card', 'credit_card',
                      'credit_card', 'credit_card', 'credit_card', 'credit_card', 'credit_card',
                      'credit_card', 'credit_card', 'credit_card', 'credit_card', 'credit_card',
                      'credit_card', 'credit_card', 'credit_card', 'credit_card', 'credit_card',
                      'credit_card', 'credit_card', 'credit_card', 'credit_card', 'credit_card',
                      'debit_card', 'debit_card', 'debit_card', 'debit_card', 'debit_card',
                      'debit_card', 'debit_card', 'debit_card', 'paypal', 'paypal', 'paypal',
                      'paypal', 'paypal'],
    'transaction_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                      11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                      21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                      31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                      41, 42, 43, 44, 45, 46, 47, 48],
    'transaction_date': ['2025-03-15', '2025-03-20', '2025-03-25', '2024-11-10', '2024-12-05',
                        '2024-07-15', '2024-08-10', '2024-09-05', '2024-10-20', '2024-10-25',
                        '2025-04-02', '2025-04-05', '2025-04-10', '2025-04-15', '2025-04-20',
                        '2025-04-25', '2025-05-01', '2025-05-05', '2025-05-10', '2025-05-15',
                        '2025-05-20', '2025-05-25', '2025-05-30', '2025-06-01', '2025-06-05',
                        '2025-06-10', '2025-06-15', '2025-06-20', '2025-06-25', '2025-06-30',
                        '2025-04-08', '2025-04-18', '2025-05-08', '2025-05-18', '2025-06-08',
                        '2025-04-07', '2025-04-12', '2025-04-17', '2025-04-22', '2025-05-12',
                        '2025-05-22', '2025-06-15', '2025-06-25', '2025-04-07', '2025-04-17',
                        '2025-04-27', '2025-05-07', '2025-05-27']
}

df = pd.DataFrame(data)

# Convert transaction_date to datetime
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# Filter for Q2 2025 (April 1 - June 30)
q2_2025 = df[(df['transaction_date'] >= '2025-04-01') & 
             (df['transaction_date'] <= '2025-06-30')]

# Count transactions by payment method
payment_counts = q2_2025['payment_method'].value_counts().reset_index()
payment_counts.columns = ['payment_method', 'transaction_count']

# Calculate percentage distribution
payment_counts['percentage'] = (payment_counts['transaction_count'] / payment_counts['transaction_count'].sum()) * 100

# Display results
print("Payment Method Distribution (April 1 - June 30, 2025)")
print("="*50)
print(payment_counts.to_string(index=False, float_format="%.1f"))