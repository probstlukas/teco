import re

file_path = 'persons.txt'

# Initialize a list to store the matched occurrences
matched_occurrences = []
count = 0  # Initialize a count

# Open the file for reading
with open(file_path, 'r') as file:
    # Read the file line by line
    for line in file:
        # Use regular expression to find occurrences in the specified format
        matches = re.findall(r"Person\('\{(.*?)\}'\)", line)
        matched_occurrences.extend(matches)
        count += len(matches)

# Print the count and matched occurrences
print(f"Total count: {count}")
print("Matched occurrences:")
for occurrence in matched_occurrences:
    print(occurrence)
