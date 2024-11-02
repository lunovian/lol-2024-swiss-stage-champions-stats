import pandas as pd

# Load the CSV file
df = pd.read_csv('champions.csv')

# Function to remove duplicate consecutive words in champion names
def remove_duplicate_name(name):
    words = name.split()
    cleaned_name = []
    for i, word in enumerate(words):
        if i == 0 or word.lower() != words[i - 1].lower():  # Avoid duplicate consecutive words
            cleaned_name.append(word.capitalize())
    return ' '.join(cleaned_name)

# Apply the function to the 'Champion' column
df['Champion'] = df['Champion'].apply(remove_duplicate_name)

# Save the modified DataFrame back to CSV
df.to_csv('champions.csv', index=False)
