#Solution to Question 3

import pandas as pd

# Create DataFrame from the provided data
data = {
    'sale_date': [
        '2024-07-05', '2024-08-15', '2024-09-25', '2024-10-05', '2025-01-05',
        '2025-02-15', '2024-07-10', '2024-08-20', '2024-12-25', '2025-06-25',
        '2024-07-15', '2024-08-25', '2024-11-05', '2025-03-15', '2025-04-20'
    ],
    'temperature': [
        62, 64, 66, 68, 74, 105, 58, 92, 45, 82,
        72, 78, 65, 88, 76
    ],
    'product_name': [
        'Cherry Garcia', 'Chunky Monkey', 'Phish Food', 'Americone Dream', 'Chocolate Fudge Brownie',
        'Half Baked', 'New York Super Fudge Chunk', 'Cherry Garcia', 'Chunky Monkey', 'Phish Food',
        'Americone Dream', 'Chocolate Fudge Brownie', 'Half Baked', 'New York Super Fudge Chunk', 'Cherry Garcia'
    ],
    'sales_volume': [
        23, 26, 29, 32, 41, 80, 45, 38, 55, 42,
        37, 44, 51, 48, 39
    ],
    'transaction_id': [
        'TX0001', 'TX0002', 'TX0003', 'TX0004', 'TX0005',
        'TX0006', 'TX0007', 'TX0008', 'TX0009', 'TX0010',
        'TX0011', 'TX0012', 'TX0013', 'TX0014', 'TX0015'
    ]
}

df = pd.DataFrame(data)

# Convert sale_date to datetime and extract month
df['sale_date'] = pd.to_datetime(df['sale_date'])
df['month'] = df['sale_date'].dt.month_name()

# Group by month and sum sales volume
monthly_sales = df.groupby('month')['sales_volume'].sum().reset_index()

# Calculate quartiles and IQR
Q1 = monthly_sales['sales_volume'].quantile(0.25)
Q3 = monthly_sales['sales_volume'].quantile(0.75)
IQR = Q3 - Q1

# Define outlier thresholds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outlier months
outliers = monthly_sales[
    (monthly_sales['sales_volume'] < lower_bound) | 
    (monthly_sales['sales_volume'] > upper_bound)
]

# Print summary statistics
print("Sales Volume Analysis by Month")
print("="*30)
print(f"First Quartile (Q1): {Q1:.2f}")
print(f"Third Quartile (Q3): {Q3:.2f}")
print(f"Interquartile Range (IQR): {IQR:.2f}")
print(f"Lower Bound (Q1 - 1.5*IQR): {lower_bound:.2f}")
print(f"Upper Bound (Q3 + 1.5*IQR): {upper_bound:.2f}\n")

# Print outlier months if any exist
if not outliers.empty:
    print("Outlier Months Detected:")
    print(outliers.to_string(index=False))
else:
    print("No outlier months detected based on IQR method.")

# Print monthly sales summary
print("\nMonthly Sales Summary:")
print(monthly_sales.sort_values('sales_volume', ascending=False).to_string(index=False))

# Create a simple text-based visualization
print("\nText-Based Visualization:")
print("Sales Volume Distribution (Q1, Median, Q3 marked)")
print("-"*50)

# Get median for visualization
median = monthly_sales['sales_volume'].median()

# Create a simple scale
min_sales = monthly_sales['sales_volume'].min()
max_sales = monthly_sales['sales_volume'].max()
scale_length = 50
scale_unit = (max_sales - min_sales) / scale_length

def position_on_scale(value):
    return int((value - min_sales) / scale_unit)

# Print the scale markers
print(f"Min: {min_sales:.1f} {' '*(position_on_scale(Q1)-5)}Q1: {Q1:.1f} {' '*(position_on_scale(median)-position_on_scale(Q1)-5)}Median: {median:.1f} {' '*(position_on_scale(Q3)-position_on_scale(median)-5)}Q3: {Q3:.1f} {' '*(position_on_scale(max_sales)-position_on_scale(Q3)-5)}Max: {max_sales:.1f}")

# Print the IQR range
iqr_line = [' '] * (scale_length + 1)
iqr_start = position_on_scale(Q1)
iqr_end = position_on_scale(Q3)
for i in range(iqr_start, iqr_end + 1):
    iqr_line[i] = '='
print('IQR Range: ' + ''.join(iqr_line))

# Print lower and upper bounds
print(f"Lower Bound: {' '*(position_on_scale(lower_bound))}│")
print(f"Upper Bound: {' '*(position_on_scale(upper_bound))}│")