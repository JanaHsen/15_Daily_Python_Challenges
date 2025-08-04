🔍 Google Search Results Engagement Analysis – 2024 Data
Welcome to the Search Team Engagement Analytics project!
This repository analyzes how the number of search results impacts user interaction time, helping optimize Google’s results presentation strategy.

📌 Project Context
You're a Product Analyst on the Google Search Team, tasked with investigating user engagement patterns from a 2024 dataset. Your goal is to determine the optimal number of search results to display per page to maximize interaction time.

🔍 Business Questions
📊 Q1: Duplicate Removal for Data Quality
How many duplicate entries exist in the dataset, and what’s the clean record count?

python
duplicates = user_engagement_data.duplicated().sum()  # Output: 5
cleaned_data = user_engagement_data.drop_duplicates()  # 53 records remaining
Key Insight:
✔️ Removed 5 duplicates (9% of raw data) to ensure analysis accuracy.

🔄 Q2: Average Interaction Time by Results Count
What’s the average interaction time for each search_results_displayed value?

python
avg_times = cleaned_data.groupby('search_results_displayed')['interaction_time'].mean()
Results:

Results Displayed	Avg Time (s)
5	32.77
10	57.31
15	62.77
20	63.70
Key Insight:
✔️ Interaction time increases with more results, peaking at 20 results/page.

🧮 Q3: Optimal Results Configuration
Which search_results_displayed value maximizes engagement?

python
optimal_results = avg_times.sort_values(ascending=False)
Recommendation:
🎯 20 results/page yields the highest interaction time (63.7s).
⚠️ Consider testing 15 results (62.77s) for balance with page performance.

✅ Outcomes
✅ Data Quality: Cleansed dataset ready for analysis.
✅ Engagement Trends: Quantified time gains from 5→20 results.
✅ Strategic Insight: 20 results optimal, but 15 is a strong alternative.