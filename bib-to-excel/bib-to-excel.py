import pybtex.database
from pylatexenc.latex2text import LatexNodes2Text
import pandas as pd

# Parse the BibTeX file
bib_data = pybtex.database.parse_file('bibliography.bib')

# Initialize a DataFrame
df = pd.DataFrame(columns=['Paper Name', 'First Name', 'Last Name', 'Email'])

# Loop through entries and extract authors for entries with 'ID' in the LaTeX identifier
for entry in bib_data.entries.values():
    if 'ID' in entry.key:
        # Get paper name and use N/A as fallback value
        paper_name = LatexNodes2Text().latex_to_text(entry.fields.get('title', 'N/A'))

        for person in entry.persons['author']:
            for i in range(len(person.first_names)):
                first_name = LatexNodes2Text().latex_to_text(person.first_names[i])
                last_name = LatexNodes2Text().latex_to_text(person.last_names[i])
                df = pd.concat([df, pd.DataFrame({'Paper Name': [paper_name], 'First Name': [first_name], 'Last Name': [last_name]})], ignore_index=True)

# Save data to an Excel file
output_file = 'earable_contacts.xlsx'
df.to_excel(output_file, index=False)

print(f'Results were saved to {output_file}.')
