# Use pandas to create a new data frame consisting of 3 series and save it to a CSV file named
# ‘TestSheet.csv’. Once created, retrieve data from the same file, make changes to it and add another series
# and save the new data frame to the existing file. See the sample below for how your data should look
# like.

import pandas as pd

# Create initial DataFrame and save it to CSV
data = {
    'duration': [60, 60, 60, 45, 45],
    'pulse': [110, 117, 103, 109, 117],
    'max pulse': [130, 145, 135, 175, 148],
    'calories': [409.1, 479, 340, 282.4, 406]
}

df = pd.DataFrame(data)
df.to_csv('TestSheet.csv', index=False)

# Try to read the CSV file or create a new DataFrame if file does not exist
try:
    df = pd.read_csv('TestSheet.csv')
except FileNotFoundError:
    df = pd.DataFrame(columns=['duration', 'pulse', 'max pulse', 'calories'])

print("Current DataFrame:")
print(df)

# Input new data from the user
new_row = {
    'duration': int(input("Enter duration: ")),
    'pulse': int(input("Enter pulse: ")),
    'max pulse': int(input("Enter max pulse: ")),
    'calories': float(input("Enter calories: "))
}

# Append the new row to the DataFrame
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# Save the updated DataFrame back to CSV
df.to_csv('TestSheet.csv', index=False)

print("\nUpdated DataFrame:")
print(df)
