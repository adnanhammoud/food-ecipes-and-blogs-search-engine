# 2- Converting the raw files into JSON format to be returned to the front-end
import json

# Define the input and output file paths
index = 1

while index <= 100:
    input_file_path = "food_" + str(index) + ".txt"
    output_file_path = "originalJSON" + str(index) + ".json"
    # with open(input_file_path, 'r+', errors="ignore") as fp:
        # read an store all lines into list
        # lines = fp.readlines()
        # move file pointer to the beginning of a file
        # fp.seek(0)
        # truncate the file
        # fp.truncate()

        # start writing lines except the last line
        # lines[:-1] from line 0 to the second last line
        #fp.writelines(lines[:-3])

    # writeFood = open(input_file_path, 'a')
    # writeFood.write("ID" + str(index))

    with open(input_file_path, 'r', errors="ignore") as text_file:
        lines = text_file.readlines()

    # Extract the ID from the last line
    document_id = lines[-1].strip()

    data = {
        "Text File": ''.join(lines),  # Combine lines into a single string
        "id": document_id
    }

    # Write the data to a JSON file
    with open(output_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    index = index + 1
