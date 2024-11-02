import pandas as pd

# Load the CSV file
df = pd.read_csv('champions.csv')

# Function to remove duplicate names
def remove_duplicate_name(name):
    parts = name.split()
    if len(parts) == 2 and parts[0] == parts[1]:
        return parts[0]
    return name

# Apply the function to the 'champion name' column
df['Champion'] = df['Champion'].apply(remove_duplicate_name)

# Save the modified DataFrame back to CSV
df.to_csv('champions.csv', index=False)