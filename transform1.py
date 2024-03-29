import csv

def read_and_modify_csv(input_filename):
    # Read and modify the data, removing newlines
    modified_data = []
    parent_comments = {}  # To store parent_id to comment mapping
    with open(input_filename, newline='') as csvfile:
        reader = csv.reader(csvfile, quotechar='"')
        next(reader)  # Skip the first two lines if they are not needed
        next(reader)
        headers = next(reader)  # Assuming the third line is headers
        headers.append('parent_comment')  # Add new column for parent comment
        
        for row in reader:
            if row:  # Check if row is not empty
                # Remove newlines in each field and prepare for adding parent comment
                row = [field.replace('\n', ' ') for field in row] + ['']
                parent_id = row[headers.index('parent_id')]
                comment = row[headers.index('comment')]

                if parent_id and int(parent_id) > 0:
                    parent_comments[parent_id] = comment

                modified_data.append(row)

    # Second pass: Add parent comment to child and filter out non-specific subnet records
    final_data = [headers]  # Start with headers
    for row in modified_data:
        parent_id = row[headers.index('parent_id')]
        if parent_id and int(parent_id) > 0:
            # If this is a child, add the parent comment
            row[-1] = parent_comments.get(parent_id, '')
        # Only keep records that are specific subnets
        if parent_id and int(parent_id) > 0:
            final_data.append(row)

    return final_data

# Usage
input_filename = 'original.csv'
modified_data = read_and_modify_csv(input_filename)

# Write the final modified data to a new file
with open('modified.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, quotechar='"')
    writer.writerows(modified_data)
