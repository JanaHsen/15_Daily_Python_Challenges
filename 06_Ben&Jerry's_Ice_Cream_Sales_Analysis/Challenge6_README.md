# Ben & Jerry's Seasonal Sales Analysis

## 📊 Project Overview
This analysis examines how temperature variations impact Ben & Jerry's ice cream sales across different seasons. By identifying key sales patterns, we aim to optimize inventory planning and targeted marketing campaigns.

## 🔍 Key Questions Answered

### 1. Data Quality Assessment
- Identified and handled duplicate transactions
- Processed missing temperature values
- Flagged potential outliers for further investigation

### 2. Temperature-Driven Sales Patterns
- Categorized sales by temperature ranges:
  - `<60°F` (Cold weather)
  - `60-69°F` (Mild)
  - `70-79°F` (Warm)
  - `80-89°F` (Hot)
  - `90°F+` (Extreme heat)

### 3. Seasonal Trends Analysis
- Compared monthly sales volumes
- Identified peak demand periods
- Analyzed unusual sales patterns

## 🛠 Methodology

### Data Processing Pipeline
```python
# Convert dates and extract months
df['month'] = pd.to_datetime(df['sale_date']).dt.month_name()

# Categorize temperatures
bins = [-float('inf'), 60, 70, 80, 90, float('inf')]
labels = ['<60°F', '60-69°F', '70-79°F', '80-89°F', '90°F+']
df['temp_range'] = pd.cut(df['temperature'], bins=bins, labels=labels)
```

### Analytical Approach
- Created time-series visualizations
- Built pivot tables for multi-dimensional analysis
- Calculated month-over-month growth rates
- Identified statistical outliers

   ```

## 🔑 Key Findings

1. **Optimal Sales Temperature**: 
   - 68% of sales occur between 60-79°F
   
2. **Unexpected Patterns**:
   - Significant sales at >90°F (12% of total)
   - Winter sales spikes during holiday periods

3. **Regional Variations**:
   - Northern states show stronger cold-weather sales
   - Southern states dominate extreme-temperature purchases

## 📈 Sample Output

| Month     | <60°F | 60-69°F | 70-79°F | 80-89°F | 90°F+ |
|-----------|-------|---------|---------|---------|-------|
| January   | 142   | 85      | 62      | 28      | 0     |
| July      | 15    | 320     | 415     | 285     | 180   |
| December  | 210   | 125     | 95      | 40      | 5     |

