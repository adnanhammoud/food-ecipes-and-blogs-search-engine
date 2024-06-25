# List of file names to concatenate
 # Replace with your file names


# Output file name
output_file = "concatenated.txt"
index = 1
food = ""
while index <= 100:
    strRead = "food_" + str(index) + ".txt"
    openFood = open(strRead, 'r', errors="ignore")
    readFood = openFood.read()
    food = food + readFood + "~"
    index = index + 1

with open(output_file, "w") as concatenated_file:
    concatenated_file.write(food)  # Add a newline between files
    # print(f"Concatenation completed. Output saved to {output_file}")
