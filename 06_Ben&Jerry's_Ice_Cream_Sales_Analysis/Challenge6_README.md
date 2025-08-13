# Ben & Jerry's Seasonal Sales Analysis

## Objective
Analyze seasonal sales patterns of Ben & Jerry's ice cream to understand how temperature variations impact sales volume and identify unusual sales periods.

## Key Questions
1. How does temperature affect ice cream sales volume?
2. What are the seasonal patterns in sales performance?
3. Which months show statistically unusual sales volumes (outliers)?

## Analytical Approach
1. **Data Preparation**:
   - Cleaned transaction data by removing duplicates
   - Extracted month from sale dates for seasonal analysis
   - Categorized temperatures into meaningful ranges

2. **Exploratory Analysis**:
   - Created pivot tables showing sales by month and temperature range
   - Calculated monthly sales aggregates

3. **Outlier Detection**:
   - Computed quartiles (Q1, Q3) and Interquartile Range (IQR)
   - Identified outlier months using the 1.5×IQR rule
   - Generated text-based visualizations of the distribution

4. **Pandas-Only Implementation**:
   - Performed all analysis using pandas' built-in functionality
   - Developed alternative visualizations without matplotlib