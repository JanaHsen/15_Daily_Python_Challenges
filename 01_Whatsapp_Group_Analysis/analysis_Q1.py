# Solution for question 1
import pandas as pd
# Create the data according to the table provided

data = {
    'group_id' : [1,2,3,4,5,6,7,8,9,10,11,12],

    'created_date' : ['2024-10-01' , '2024-10-10' , '2024-11-05' , '2024-10-15' , '2024-12-01' , '2024-10-20' , '2024-10-25' , '2024-11-10' , '2024-10-30' , '2024-12-15' , '2024-10-05' , '2024-12-12'] ,

    'total_messages':[100,200,150,500,120,300,400,220,450,80,600,50],

    'participant_count' : [25,55,40,100,35,50,60,45,80,15,90,10]
}

# Create DataFrame
df =pd.DataFrame(data)

# Convert created_data to datetime
df['created_date'] = pd.to_datetime(df['created_date'])

# Filter for October 2024
october_groups = df[(df['created_date'].dt.month == 10) & (df['created_date'].dt.year == 2024)]

# Get the maximum number of participants
max_participants = october_groups['participant_count'].max()
print('The maximum number of participants in October 2024 is ' , max_participants)
