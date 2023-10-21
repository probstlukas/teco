from pybtex.database import parse_file
from pylatexenc.latex2text import LatexNodes2Text
import pandas as pd

def bib_to_df(bib_data):
    # Initialize a DataFrame
    df = pd.DataFrame(columns=['Paper Name', 'First Name', 'Last Name', 'Email'])

    # Create a dictionary to keep track of counts for each (First Name, Last Name) combination
    counts = {}

    # Loop through entries and extract authors for entries with 'ID' in the LaTeX identifier
    for entry in bib_data.entries.values():
        if 'ID' in entry.key:
            # Get paper name and use N/A as a fallback value
            paper_name = LatexNodes2Text().latex_to_text(entry.fields.get('title', 'N/A'))

            # Note: Persons appearing as "{Firstname Lastname}" in the .bib file are not included here. Since it only affects 11 out of 1263 people, I added them manually
            for person in entry.persons['author']:
                for i in range(len(person.first_names)):
                    first_name = LatexNodes2Text().latex_to_text(person.first_names[i])
                    last_name = LatexNodes2Text().latex_to_text(person.last_names[i])

                    # Get the current count for this combination
                    count = counts.get((first_name, last_name), 0)

                    # Update the count
                    counts[(first_name, last_name)] = count + 1

                    # Determine if it's a duplicate
                    is_duplicate = count >= 1

                    # Label all persons that appear more than once with 'Duplicate'
                    if is_duplicate:
                        df = pd.concat([df, pd.DataFrame({'Paper Name': [paper_name], 'First Name': [first_name], 'Last Name': [last_name], 'Email': 'Duplicate'})], ignore_index=True)
                    else: 
                        df = pd.concat([df, pd.DataFrame({'Paper Name': [paper_name], 'First Name': [first_name], 'Last Name': [last_name]})], ignore_index=True)

    return df

# Main function to run the program
def main():
    output_file = 'earable-contacts.xlsx'
    bib_data = parse_file('bibliography.bib')
    df = bib_to_df(bib_data)
    # Save data to an Excel file
    df.to_excel(output_file, index=False)

    print(f'Results were saved to {output_file}.')

if __name__ == "__main__":
    main()