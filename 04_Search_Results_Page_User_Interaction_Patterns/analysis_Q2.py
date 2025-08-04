# Solution to Question 1

import pandas as pd

# Create the DataFrame from the provided data
data = [
    # First table
    ["user_1", "2024-07-05", 35.5, 10],
    ["user_2", "2024-07-10", 22.3, 5],
    ["user_1", "2024-07-05", 35.5, 10],  # Duplicate of first row
    ["user_3", "2024-08-01", 48, 15],
    ["user_4", "2024-08-15", 20, None],  # Missing search_results_displayed
    ["user_5", "2024-09-05", 60.2, 10],
    ["user_6", "2024-10-10", 12, 5],
    ["user_7", "2024-11-20", 80, 15],
    
    # Second table
    ["user_8", "2024-12-31", 55, 20],
    ["user_9", "2025-01-15", 75.5, 10],
    ["user_10", "2025-02-20", 30, 5],
    ["user_2", "2024-07-10", 22.3, 5],  # Duplicate of second row
    ["user_11", "2025-03-01", 92.5, 10],
    ["user_12", "2025-03-05", 15, 15],
    ["user_13", "2025-03-10", 45.3, 20],
    ["user_14", "2025-03-15", 5, 5],
    ["user_15", "2025-03-20", 68, 10],
    ["user_16", "2025-03-25", 110, 15],
    
    # Third table (contains invalid dates which we'll keep for this analysis)
    ["user_17", "2025-94-61", 29.9, 20],
    ["user_18", "2025-94-65", 159, 10],
    ["user_19", "2025-94-10", 33.3, 5],
    ["user_20", "2025-94-15", 25, 15],
    ["user_21", "2025-94-26", 40, 20],
    ["user_22", "2025-94-25", 85.5, 10],
    ["user_23", "2025-94-30", None, 5],
    ["user_24", "2025-95-65", 55.5, 15],
    ["user_25", "2025-95-10", 65, 20],
    ["user_26", "2025-95-15", 70, 10],
    ["user_27", "2025-95-20", 95, 5],
    ["user_28", "2025-95-25", 50, 15],
    ["user_29", "2025-96-61", 88, 20],
    ["user_30", "2025-96-65", 42, 10],
    ["user_31", "2025-96-10", 37, 5],
    ["user_32", "2025-96-15", 82, 15],
    ["user_33", "2025-96-20", 20, 20],
    ["user_34", "2025-96-25", 90, 10],
    ["user_35", "2025-96-29", 77, 5],
    
    # Fourth table
    ["user_36", "2025-06-30", 66.6, 15],
    ["user_37", "2024-07-15", 100, 20],
    ["user_38", "2024-07-20", 110.5, 10],
    ["user_39", "2024-08-05", 35, 5],
    ["user_40", "2024-08-10", 59.9, 15],
    ["user_41", "2024-08-15", 47.3, 20],
    ["user_42", "2024-08-20", None, 10],
    ["user_43", "2024-09-01", 68.5, 5],
    ["user_44", "2024-09-05", 72.7, 15],
    ["user_45", "2024-09-10", 55.5, 20],
    ["user_46", "2024-09-15", 62, 10],
    ["user_47", "2024-09-20", 40, 5],
    ["user_48", "2024-09-25", 85, 15],
    ["user_49", "2024-10-01", 95, 20],
    ["user_50", "2024-10-05", 33.3, 10],
    ["user_51", "2024-10-10", 44.4, 5],
    ["user_52", "2024-10-15", 88.8, 15],
    ["user_53", "2024-10-20", 75.5, 20],
    ["user_54", "2024-10-25", 90, 10],
    ["user_55", "2024-10-30", None, 5],
    
    # Fifth table
    ["user_51", "2024-10-10", 44.4, 5],  # Duplicate
    ["user_52", "2024-10-15", 88.8, 15],  # Duplicate
    ["user_53", "2024-10-20", 76.5, 20],  # Note: interaction_time is different (75.5 vs 76.5)
    ["user_54", "2024-10-25", 90, 10],    # Duplicate
    ["user_55", "2024-10-30", None, 5],   # Duplicate
    ["user_56", "2024-11-01", 101, 15],
    ["user_57", "2024-11-05", 59, 20],
    ["user_58", "2024-11-10", 66, 10]
]

# Create DataFrame
columns = ["user_id", "interaction_date", "interaction_time", "search_results_displayed"]
user_engagement_data = pd.DataFrame(data, columns=columns)

# Count duplicates
duplicates = user_engagement_data.duplicated()
num_duplicates = duplicates.sum()

# Remove duplicates
cleaned_data = user_engagement_data.drop_duplicates()

# Group by 'search_results_displayed' and calculate mean interaction time
average_interaction = cleaned_data.groupby('search_results_displayed')['interaction_time'].mean().reset_index()

# Rename columns for clarity
average_interaction.columns = ['search_results_displayed', 'average_interaction_time']

# Display the results sorted by search_results_displayed
average_interaction.sort_values('search_results_displayed')