# Instagram Stories Analysis

## Objective  
Analyze user story creation patterns to understand daily posting behavior and identify highly engaged users.

## Key Questions  
1. **Data Quality**: How should we clean and standardize the raw story posting data?  
2. **Usage Patterns**: What are the 25th, 50th, and 75th percentiles of stories created per user daily?  
3. **Power Users**: What percentage of users have at least one high-activity day (>10 stories)?  

## Analytical Approach  
1. **Data Preparation**  
   - Standardized user IDs and datetime formats  
   - Aggregated duplicate entries (same user-day combinations)  
   - Removed invalid/missing data points  

2. **Behavior Analysis**  
   - Calculated daily story totals per user  
   - Computed distribution percentiles using numpy  
   - Identified users exceeding activity thresholds  

3. **Engagement Insights**  
   - Quantified "power user" prevalence  
   - Delivered clear metrics for segmentation strategies  