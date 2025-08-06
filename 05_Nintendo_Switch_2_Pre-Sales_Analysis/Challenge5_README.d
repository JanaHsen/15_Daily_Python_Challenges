
# Nintendo Switch 2 Pre-Sales Analysis

## Challenge Overview  
As a Product Analyst on the Nintendo Switch 2 team, the goal is to analyze regional pre-order patterns and customer segmentation to guide marketing strategies and inventory planning.

---

## Challenge Questions  

1. **What percentage of records have missing values in at least one column?**  
   Identified data quality issues that needed cleaning before analysis.

2. **What are the total pre-sale orders per month for each region and demographic group?**  
   Revealed purchasing patterns across different customer segments and geographic markets.

3. **What is the predicted total pre-sales quantity for each region in September 2024?**  
   Forecasted demand using month-over-month growth rates to inform production planning.

---

## Approach  

### Data Preparation
- Cleaned missing values by removing records with null regions and imputing unknown demographics
- Standardized region names and demographic group categories
- Extracted month from order dates for temporal analysis

### Analysis Techniques
1. **Missing Values Analysis**:
   - Calculated percentage of incomplete records
   - Implemented appropriate imputation strategies

2. **Monthly Sales Analysis**:
   - Grouped data by month, region, and demographic group
   - Calculated sum of pre-order quantities for each segment
   - Created pivot tables for cross-dimensional analysis

3. **Growth Forecasting**:
   - Calculated July-to-August growth rates by region
   - Projected September sales using same growth patterns
   - Rounded forecasts to whole units for realistic planning

---

## Key Learnings  

- **Data Cleaning**: Developed strategies for handling missing geographic and demographic data
- **Time-Series Analysis**: Practiced monthly aggregation and growth rate calculations
- **Market Forecasting**: Learned to project future demand using simple growth models
- **Segmentation Insights**: Discovered varying growth patterns across regions (North America +70% vs Europe -7.1%)

---

## Notes  

- Analysis based on simulated pre-order data representing Nintendo Switch 2 launch period
- Growth rate assumptions could be refined with:
  - Longer historical data
  - Seasonality adjustments
  - External market factors
- All forecasts rounded to whole numbers as partial units cannot be sold

---
