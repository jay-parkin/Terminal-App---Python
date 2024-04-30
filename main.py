import json

# Local modules
from ingredients import store_ingredient, Ingredients
from recipes import new_recipe, Recipes
from csv_functions import read_recipes_from_csv, write_recipes_to_csv, read_ingredients_from_csv
from recipe_api_request import random_recipe_request, recipe_by_ingredient_request, get_recipe_by_id
from helper_functions import word_wrap, remove_html_tags

# Print measurements to help with aligning
print_width = 50

# Introduces the app
def print_inital_welcome():
    print("\n**************************************************")
    print("Culinary Companion".center(print_width))
    print("**************************************************")
    print("Welcome to the Digital Dish".center(print_width))
    print("your ultimate culinary companion for exploring".center(print_width))
    print("creating and savouring delicious dished!".center(print_width))
    print("\n")
    print("Let's get started...".center(print_width))

def print_goodbye():
    print("\n")
    print("Thank you!".center(print_width))
    print("We hope you enjoyed using Digital Dish".center(print_width))
    print("Have a great day!".center(print_width))

# Load menu for user interaction
def create_menu():
    print("\n")
    print("*" * 19 + " Main Menu " + "*" * 20)
    # print("**************************************************")
    print("A. Add New Recipe") # Add a new recipe to the list
    print("B. Add Random Recipe") # Add a random recipe to the list
    print("C. Generate Recipe Using My Ingredients") # Generate a recipe using ingredients from the stored ingredient list
    print("D. My Ingredients") # Add ingredients found at home
    print("E. Delete Recipe") # Delete a recipe from the list
    print("F. View Recipes") # Allows the use to view and print recipe
    print("X. Exit") # Exits app

    return input("Enter Selection: ").lower()
    
# Display a single recipe after being selcted
def display_recipe(choice, all_recipes):
    # only used to adjust the title length
    choice_str = str(choice)
    choice_len = len(choice_str)
    title_spacing = 50 - int((choice_len + 9)) # 9 is the length of the word ' Recipe '
    half_spacing = int(title_spacing / 2)

    # name, ingredients, prep_time, cook_time, serves, steps, description
    # layout a nice display of the recipe selected
    print("\n")
    print("*" * half_spacing + f" Recipe {choice} " + "*" * half_spacing)
    print("\n")

    print(f"Name")
    print(f"\t{all_recipes[choice - 1].get_name()}")

    print(f"\nIngredients")
    for ingredient in all_recipes[choice - 1].get_ingredients():
        print(f"{ingredient.display_info()}")
    
    print(f"Ready In Minutes")
    print(f"\t{all_recipes[choice - 1].get_ready_in_minutes()}")

    print(f"\nServing Size")
    print(f"\t{all_recipes[choice - 1].get_serves()}")

    print(f"\nMethod")
    # Pass itselfs through a display method
    all_recipes[choice - 1].display_methods(all_recipes[choice - 1].get_methods())

    print(f"\nDescription")
    print(f"{all_recipes[choice - 1].get_description()}")

# Allow the user to view all recipes on the console
def display_all_recipes(all_recipes):
    print("*" * 50)
    print(f"{'No.':5}{'Name':<17}{'Description':<27}")
    print("*" * 50)

    count = 0
    for recipe in all_recipes:
        count += 1

        name = recipe.get_name()
        description = recipe.get_description()

        # Limit length for formatting
        if len(name) > 12:
            name = name[:12] + "..."  # Truncate if too long

        if len(description) > 25:
            description = description[:25] + "..."  # Truncate if too long

        print(f"{count:<5}{name:<17}{description:<30}")

    print("*" * 50)
    print("\n")

# Remove a recipe from the list
def delete_recipe(choice, all_recipes):
    print(f"\nDeleting Recipe: {all_recipes[choice - 1].get_name()}")

    print("1: Yes")
    print("2: No")

    # Confirm the choice to delete
    choice_yes = input("Are you sure? ") 

    if choice_yes == "1":
        # Confirmed to delete
        print(f"Deleting...")
        # Set recipe inactive
        all_recipes[choice - 1].set_status_inactive()

        # Write list of recipes without the inacive recipe selected
        write_recipes_to_csv(all_recipes, "my_recipes.csv", "w")

def view_recipes(action):
    print("\n")

    # Change the padding size depending on the type of view
    padding = 18
    if action == "Delete":
        padding = 17

    print("*" * padding + f" {action} Recipes " + "*" * padding)
    all_recipes = read_recipes_from_csv("my_recipes.csv")

    display_all_recipes(all_recipes)
            
    try:
        choice = int(input(f"Enter which Recipe to {action}: "))

        # Check user input is within list range
        if choice == 0 or choice > len(all_recipes):
            print(f"Recipe {choice} doesn't exist.")

        # View recipe
        elif action == "View":
            display_recipe(choice, all_recipes)

        # Delete recipe
        elif action == "Delete":
            delete_recipe(choice, all_recipes)

    except ValueError:
        print("Error - Please enter a number.")
 
def load_recipe_data(filename):
    with open(filename, "r") as file:
        recipe_data = json.load(file)
    return recipe_data

# Find recipes id from the api > https://rapidapi.com/spoonacular/api/recipe-food-nutrition
def get_recipe_id(data):
    response_data = data

    # Extract title from the first recipe in the response
    if "recipes" in response_data and len(response_data["recipes"]) > 0:
        for recipe_data in response_data["recipes"]:
            id = recipe_data.get("id", "n/a")

        return id

# Create a recipes from id > pull https://rapidapi.com/spoonacular/api/recipe-food-nutrition
def get_recipe_from_api(id):
    # Load recipe data from the JSON file
    # response_data = found_recipe_request()

    # Loaded local data for testing
    # filename = "recipe_data1.json"
    # recipe_data = load_recipe_data(filename)

    # 634486 - brisket
    recipe_data = get_recipe_by_id(id)

    found_recipe = []
    # Extract title from the first recipe in the response        
    if recipe_data:
        # recipe name
        title = recipe_data.get("title", "n/a")
        print(f"Adding: {title}")

        # add ingredients
        ingredients = []
        name = ""
        amount = ""
        unit = ""
        extendedIngredients = recipe_data.get("extendedIngredients", [])
        
        for ingredient in extendedIngredients:
            name = ingredient.get("nameClean")
            amount = ingredient.get("amount")
            unit = ingredient.get("unit")

            ingredients.append(Ingredients(name, amount, unit))

        # method > steps
        methods = []
        length = 0 # Length of each step
        ready_in_minutes = 0
        analyzed_instructions = recipe_data.get("analyzedInstructions", [])

        # move through get instuction and add to step
        for instruction in analyzed_instructions:
            steps = instruction.get("steps", [])
            for step in steps:
                methods.append(word_wrap(step["step"]))
                # collect length as well
                # get ready time from the length of each step
                # ready_time = recipe_data.get("readyInMinutes", "n/a")
                length = step["length"]["number"] if "length" in step else 0
                ready_in_minutes += length

        serves = recipe_data.get("servings", "n/a")
        
        description = remove_html_tags(recipe_data.get("summary", title))

        # #  Create a Recipes object
        found_recipe = Recipes(title, ready_in_minutes, serves, description)
        found_recipe.add_ingredients(ingredients)
        found_recipe.read_csv_method(methods)

        return found_recipe
    else:
        print("No recipes found..")

# Loads stored ingredients and pulls 5 random recipes from api
def recipe_by_ingredient():
    print("\n")
    print("*" * 14 + " Recipe By Ingredient " + "*" * 14)
    # list of 5 recipe titles. + cancel = 0
    # which recipe would you like to view?
        # get id and search in api
        # save recipe
    # remove from list of 5
    file_name = "my_ingredients.csv"
    
    # Load ingredients
    ingredients_set = set() # Set of ingredients
    ingredients_set = read_ingredients_from_csv(ingredients_set, file_name)

    ingredients = ""
    # Extract name from ingredients
    for ingredient_name in ingredients_set:
        ingredients += ingredient_name.get_name() +","
    
    response_data = recipe_by_ingredient_request(ingredients)
    # response_data = load_recipe_data("new.json") # used for testing

    # Extract title from all recipes in the response
   
    removed_recipe = []
    count = []
    choice = ""

    while True:
        # Add all recipes from api to a list
        available_recipes = []
        for recipe in response_data:
            if recipe.get("title") not in removed_recipe:
                available_recipes.append(recipe)

        # create a range starting 1 to the length of recipes
        count = list(range(1, len(available_recipes) + 1))

        for i, recipe in enumerate(available_recipes):
            print(f"{count[i]}: {recipe['title']}")

        print("0: Back")
        choice = input("Enter which Recipe to Add: ")

        if choice == "0":
            break 

        # append choice
        # Make sure the choice is a number and more than 0 and less then count length
        if choice.isdigit() and 0 < int(choice) <= len(count):
            index = int(choice) - 1 # started at 1

            if 0 <= index < len(available_recipes):
                selected_title = available_recipes[index]["title"]
                removed_recipe.append(selected_title)

                # add recipe to stored list
                id = available_recipes[index]["id"]
                
                
                # save to csv file
                recipe = Recipes()
                recipe = get_recipe_from_api(id)

                write_recipes_to_csv([recipe], "my_recipes.csv", "a")

                print(f"{selected_title} has been added..")
            else:
                print("Invalid input. Please try again.")
        else:
            print("Invalid input. Please try again.")

        # Clear init values
        choice = ""

        print("")

# App starts here
print_inital_welcome()

# Loop menu until user exitsa
choice = ""
while choice != "x":
    choice = create_menu()

    # Add switch case to decide selection
    match choice:
        # Add new recipe
        case "a":
            new_recipe()

        # Add random recipe
        case "b":
            recipe = Recipes()
            #  Find the id from a random reicpe and pass it 
            #  into a function to pull the rest of the info
            recipe = get_recipe_from_api(get_recipe_id(random_recipe_request()))

            write_recipes_to_csv([recipe], "my_recipes.csv", "a")

        # Generate recipe using my ingredients
        case "c":
            recipe_by_ingredient()

        # Store my ingredients
        case "d":
            store_ingredient(False)

        # Delete recipe
        case "e":
            view_recipes("Delete")

        # View recipes // read csv
        case "f":
            view_recipes("View")

        # Exit app
        case "x":
            print_goodbye()
            break

        case _:
            print("Error - Invalid selection!")
