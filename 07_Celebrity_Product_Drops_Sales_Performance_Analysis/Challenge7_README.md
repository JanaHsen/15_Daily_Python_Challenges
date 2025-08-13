# Nike Celebrity Collaboration Performance Analysis

## Objective  
Evaluate the effectiveness of Nike's celebrity product collaborations in Q1 2025 to inform future marketing strategies and partnership decisions.

## Key Questions  
1. **Data Completeness**: Which celebrity collaboration records have missing sales amounts?  
2. **Collaboration Inventory**: What unique celebrity-product combinations exist?  
3. **Performance Ranking**: Which are the top 3 highest-grossing collaborations?  

## Analytical Approach  
1. **Data Quality Check**  
   - Identified records with missing `sale_amount` values  
   - Filtered for Q1 2025 (Jan 1 - Mar 31) timeframe  

2. **Collaboration Mapping**  
   - Extracted unique celebrity-product pairs  
   - Verified no duplicate partnerships  

3. **Performance Evaluation**  
   - Aggregated sales by celebrity-product combination  
   - Ranked collaborations by total sales  
   - Flagged potential data inconsistencies in top performers  

4. **Pandas Implementation**  
   - Used groupby-sum for sales aggregation  
   - Applied sorting for ranking  
   - Formatted output for clear business interpretation  