# Lululemon Payment Method Analysis

## Objective  
Evaluate the potential impact of introducing installment payments by analyzing current payment behaviors and estimating sales lift.

## Key Questions  
1. **Baseline Distribution**: What are current payment method shares?  
2. **Spending Patterns**: How does average order value vary by payment method?  
3. **Opportunity Sizing**: What sales lift could installment payments generate?  

## Analytical Approach  
1. **Current State Analysis**  
   - Calculated transaction counts by payment method (Q2 2025)  
   - Compared average order values across payment types  

2. **Installment Payment Simulation**  
   - Isolated credit card transactions (64% of volume)  
   - Modeled 20% conversion to installments  
   - Applied 15% AOV lift to converted transactions  

3. **Pandas Implementation**  
   - Used datetime filtering for period isolation  
   - Applied groupby-aggregate for payment metrics  
   - Calculated weighted sales lift projections  