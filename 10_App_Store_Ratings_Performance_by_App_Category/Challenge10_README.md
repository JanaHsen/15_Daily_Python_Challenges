# App Store Ratings Analysis

## Objective  
Analyze app rating patterns across categories to identify performance trends and data quality issues in the Apple App Store.

## Key Questions  
1. **Data Quality**: How should we clean inconsistent rating data (mixed formats, invalid values)?  
2. **Category Performance**: What are the rating statistics (mean, median, variability) by app category?  
3. **Insight Generation**: Which categories show exceptional performance or consistency?  

## Analytical Approach  
1. **Data Cleaning**  
   - Standardized rating formats (decimal points, numeric conversion)  
   - Handled missing/invalid values (empty strings, word numbers, out-of-range values)  
   - Validated rating ranges (1-5 scale)  

2. **Statistical Analysis**  
   - Grouped by category and calculated:  
     - Central tendency (mean, median)  
     - Dispersion (standard deviation)  
     - Rating volume (count)  

3. **Insight Generation**  
   - Identified top-performing categories  
   - Flagged categories with unusual rating patterns  
   - Highlighted data quality considerations  
