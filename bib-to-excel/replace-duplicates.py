import pandas as pd

def replace_duplicates(df):
    # Create a dictionary to keep track of email values for each unique (First Name, Last Name) combination
    email_dict = {}

    # Iterate through the DataFrame and replace duplicate entries
    for index, row in df.iterrows():
        first_name = row['First Name']
        last_name = row['Last Name']
        email = row['Email']
        
        print(email)
        if (first_name, last_name) not in email_dict:
            # If it's the first occurrence of this combination, store the email (or 'n/a' if it's empty)
            email_dict[(first_name, last_name)] = email 
        else:
            # If it's a duplicate, replace the email with the stored value (or 'n/a' if the stored value is 'n/a')
            stored_value = email_dict[(first_name, last_name)]
            df.at[index, 'Email'] = stored_value
    df['Email'].fillna('n/a', inplace=True)
    return df

# Load the Excel file into a DataFrame
input_file = 'earable-contacts-filled.xlsx'  # Replace with your file path
df = pd.read_excel(input_file, na_values = ['n/a'])

# Replace duplicates and save the updated DataFrame to a new Excel file
output_file = 'earable-contacts-final.xlsx'  # Replace with the desired output file path
df = replace_duplicates(df)
df.to_excel(output_file, index=False)

print(f'Duplicates replaced and saved to {output_file}.')