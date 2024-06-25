# 5- Converting the documents into the JSON format that are valid for elastic search and combining everything in one file
# in addition to added fields for identification of original documents and search efficiency
import json

output_data_list = []

# Load your original JSON data (recipe_data)
index = 1
while index <= 100:
    readOriginal = "originalJSON" + str(index) + ".json"
    strRead = "food_" + str(index) + "j.json"
    with open(strRead, "r") as input_file:
        recipe_data = json.load(input_file)

    with open(readOriginal, 'r') as input_original_file:
        recipe_data_original = json.load(input_original_file)
    # Prepare the transformed JSON data and append it to the list
    # output_data = {
        # "index": {"_index": "search-foodrecipe"},
    # }
    # output_data_list.append(json.dumps(output_data))

    data_to_index = {
        "id": f"ID{index}",  # Add the 'id' field
        "title": recipe_data["title"],
        "description": recipe_data_original["Text File"],
        # "description": recipe_data["description"],
        "rating": recipe_data["rating"],
        "time": recipe_data["time"],
        "nationality": recipe_data["nationality"],
        "combined": " ".join(
            [recipe_data["title"], recipe_data["description"], recipe_data["rating"], recipe_data["time"], recipe_data["nationality"]]
        ),
    }
    with open(f"food_{index}j.json", "w") as output_file:
        json.dump(data_to_index, output_file, indent=2)
    output_data_list.append(json.dumps(data_to_index))

    index = index + 1

# Write the list of JSON objects to a single file
# with open("elasticFoodDummy.json", "w") as output_file:
    # output_file.write('\n'.join(output_data_list) + '\n')
