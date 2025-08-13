#Solution to Question 3

import pandas as pd

# Create DataFrame from the provided data
data = {
    'customer_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115, 116, 117, 118, 119, 120,
                   121, 122, 123, 124, 125],
    'order_value': [275, 285, 280, 290, 270, 295, 280, 275, 285, 290,
                   270, 280, 295, 285, 280, 275, 285, 290, 270, 280,
                   275, 285, 290, 280, 275],
    'payment_method': ['credit_card'] * 25,
    'transaction_id': range(11, 36),
    'transaction_date': ['2025-04-02', '2025-04-05', '2025-04-10', '2025-04-15', '2025-04-20',
                        '2025-04-25', '2025-05-01', '2025-05-05', '2025-05-10', '2025-05-15',
                        '2025-05-20', '2025-05-25', '2025-05-30', '2025-06-01', '2025-06-05',
                        '2025-06-10', '2025-06-15', '2025-06-20', '2025-06-25', '2025-06-30',
                        '2025-04-08', '2025-04-18', '2025-05-08', '2025-05-18', '2025-06-08']
}

df = pd.DataFrame(data)
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# Filter for credit card transactions in Q2 2025
credit_transactions = df[(df['payment_method'] == 'credit_card') & 
                        (df['transaction_date'] >= '2025-04-01') & 
                        (df['transaction_date'] <= '2025-06-30')]

# Calculate key metrics
total_credit_txns = len(credit_transactions)
avg_credit_aov = credit_transactions['order_value'].mean()
txns_to_convert = int(round(total_credit_txns * 0.20))  # 20% of credit transactions

# Calculate sales lift
current_sales = credit_transactions['order_value'].sum()
lift_per_txn = avg_credit_aov * 0.15  # 15% increase per converted transaction
total_lift = lift_per_txn * txns_to_convert

# Results formatting
results = pd.DataFrame({
    'Metric': [
        'Total Credit Card Transactions',
        'Average Order Value (Credit)',
        'Transactions to Convert (20%)',
        'Projected Sales Lift (15% AOV increase on converted txns)'
    ],
    'Value': [
        total_credit_txns,
        f"${avg_credit_aov:.2f}",
        txns_to_convert,
        f"${total_lift:.2f}"
    ],
    'Calculation': [
        f"Count of credit transactions in period",
        "Mean of order_value for credit transactions",
        "20% of total credit transactions (rounded)",
        f"{txns_to_convert} txns × (${avg_credit_aov:.2f} × 15%)"
    ]
})

print("Pay Over Time Option Impact Analysis")
print("="*50)
print(results.to_string(index=False, justify='left'))