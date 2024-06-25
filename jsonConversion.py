# 4- Converting the texts files into JSON documents with the necessary fields
import json

# List of example nationalities
index = 1

while index <= 100:
    strRead = "food_" + str(index) + "pp.txt"
    with open(strRead, "r") as file:
        content = file.read()

    paragraphs = content.split('\n')


    recipe_data = {
        "title": paragraphs[0],  # The first paragraph as the "recipe" field
        "description": paragraphs[1],  # The second paragraph as the "instructions" field
        "rating": paragraphs[2],
        "time": paragraphs[3],
        "nationality": paragraphs[4]
    }

    json_data = json.dumps(recipe_data, indent=4)
    #print(json_data, end="\n")
    #print(index)

    strWriteJSON = "food_" + str(index) + "j.json"
    with open(strWriteJSON, "w") as json_file:
        json_file.write(json_data)
    index = index + 1

