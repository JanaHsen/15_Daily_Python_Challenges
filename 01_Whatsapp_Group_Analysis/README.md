# Day 01 – WhatsApp Group Messaging Analysis

## Challenge Overview  
As a Product Analyst on the WhatsApp team, the goal is to investigate group messaging dynamics. Specifically, the team wants to understand how large WhatsApp groups are being used and their messaging patterns to support feature development.

---

## Challenge Questions  

1. **What is the maximum number of participants among WhatsApp groups created in October 2024?**  
   This metric helps identify the largest group size available on the platform.

2. **What is the average number of participants in WhatsApp groups created in October 2024?**  
   This number indicates the typical group size and informs considerations for group messaging features.

3. **For WhatsApp groups with more than 50 participants created in October 2024, what is the average number of messages sent?**  
   This insight helps assess engagement levels in larger groups and supports recommendations for group messaging features.

---

## Approach  

- Simulated the dataset as a Python dictionary to reflect WhatsApp groups’ participant counts, message volumes, and creation dates.  
- Used Pandas to convert the dictionary into a DataFrame for data manipulation.  
- Filtered groups based on creation date (October 2024).  
- Calculated the maximum and average number of participants as per the questions.  
- For groups with more than 50 participants, calculated the average number of messages sent to gauge engagement.

---

## Key Learnings  

- Practiced filtering data by date using Pandas datetime operations.  
- Learned to compute aggregate metrics such as max and average on grouped data.  
- Gained insight into how data analysis can inform product feature decisions by uncovering user behavior patterns.

---

## Notes  

- The dataset used is a simulated sample created for demonstration and learning purposes, based on the challenge description.  
- Real-world datasets may require additional preprocessing steps not covered here.

