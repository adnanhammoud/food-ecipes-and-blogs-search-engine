# 1- Adding the random fields to organize and structure documents
import random

id_list = []

# Generate 100 IDs and append them to the list
for i in range(1, 101):
    id_list.append(f"ID{i}")

recipe_names = [
    "Chocolate Chip Cookies", "Vanilla Cake", "Lemon Bars", "Red Velvet Cupcakes", "Blueberry Muffins",
    "Cheesecake", "Strawberry Shortcake", "Pumpkin Pie", "Apple Crisp", "Chocolate Brownies",
    "Tiramisu", "Key Lime Pie", "Pecan Pie", "Chocolate Mousse", "Fruit Salad", "Spaghetti Bolognese",
    "Chicken Alfredo", "Beef Stroganoff", "Chicken Parmesan", "Tacos", "Chicken Curry", "Mushroom Risotto",
    "Pumpkin Soup", "Salmon Teriyaki", "Beef Tacos", "Lemon Chicken", "Vegetable Stir-Fry",
    "Pesto Pasta", "Shrimp Scampi", "Chicken Enchiladas", "Tomato Basil Soup", "Cauliflower Rice",
    "Beef Stir-Fry", "Garlic Shrimp", "Spinach Salad", "Lobster Bisque", "Eggplant Parmesan",
    "Mango Salsa", "Lentil Soup", "Chicken Fajitas", "Beef and Broccoli", "Honey Mustard Chicken",
    "Coconut Shrimp", "Mushroom Soup", "Pork Tenderloin", "Potato Salad", "Pumpkin Pie", "Beef Tenders",
    "Grilled Cheese", "Chicken Marsala", "Egg Fried Rice", "Clam Chowder", "Avocado Salad", "Lamb Chops",
    "Cheese Pizza", "Sausage Gravy", "Lemon Sorbet", "Orange Chicken", "Chicken Tenders", "Beef Pot Pie",
    "French Onion Soup", "Cucumber Salad", "Pork Roast", "Chocolate Cake", "Pasta Salad", "Scallop Risotto",
    "Salmon Salad", "Baked Ziti", "Chicken Tostadas", "Shrimp Pasta", "Tomato Soup", "Ginger Chicken",
    "Pineapple Fried Rice", "Lentil Salad", "Taco Salad", "Lamb Curry", "Mac and Cheese", "Beef Sliders",
    "Sausage Rolls", "Berry Smoothie", "Chicken Quesadillas", "Coconut Rice", "Mushroom Gravy",
    "Pork Chops", "Apple Pie", "Garlic Bread", "Chicken Pot Pie", "Beef Ribs", "Broccoli Soup",
    "Caesar Salad", "Lamb Kebabs", "Margherita Pizza", "Sausage and Peppers", "Lemon Meringue Pie",
    "Teriyaki Salmon", "Butter Chicken", "Mango Sorbet", "Salmon Chowder", "Bacon Wrapped Shrimp",
    "Beef and Noodles", "Chicken Shawarma", "Peanut Butter Cookies", "Spaghetti Carbonara", "Mushroom Risotto",
    "Lemon Curd", "Chicken Tacos", "Beef Fajitas", "Pumpkin Soup", "Lobster Bisque"
]
nationalities = ["USA", "Italy", "France", "Japan", "India", "Mexico", "Greece", "Spain", "China", "Thailand", "Brazil",
                 "Sweden", "Canada", "Australia", "Germany", "South Korea", "Argentina", "Turkey", "Egypt", "Russia"]

index = 1
while index <= 100:
    strWriteTXT = "food_" + str(index) + ".txt"
    if index >= 4:
        recipe = random.choice(recipe_names)
        recipe_names.remove(recipe)
        with open(strWriteTXT, 'r+', encoding="utf-8") as file:
            file_data = file.read()
            file.seek(0, 0)
            file.write(recipe + '\n' + file_data)
    rating = round(random.uniform(5, 10), 1)
    time = random.randint(30, 90)
    nationality = random.choice(nationalities)
    writeFood = open(strWriteTXT, 'a')
    writeFood.write("\nrating " + str(rating) + "\ntime " + str(time) + "\nnationality " + str(nationality))
    strRemove = "ID" + str(index)
    temp = id_list.remove(strRemove)
    writeFood.write("\n" + strRemove)

    index = index + 1


