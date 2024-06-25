import json

# Initialize a counter for creating file names
counter = 1

# Read the contents of elasticFood.json
with open('JSON Files/elasticFood.json', 'r') as file:
    # Process each line in the file
    lines = file.readlines()
    for i in range(1, len(lines), 2):  # Skip every alternate line (index lines)
        # Load the JSON data from the line
        json_data = json.loads(lines[i])

        # Extract relevant information
        title = json_data.get('title', '')
        description = json_data.get('description', '')
        nationality = json_data.get('nationality', '')
        rating = json_data.get('rating', '')
        time = json_data.get('time', '')

        # Create a dictionary with the extracted information
        response = {
            'title': title,
            'description': description,
            'nationality': nationality,
            'rating': rating,
            'time': time,
        }

        # Write the dictionary to a new food_keyj.json file
        with open(f'food_{counter}j.json', 'w') as output_file:
            json.dump(response, output_file, indent=2)

        # Increment the counter for the next file
        counter += 1
