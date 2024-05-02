import json

from rich.console import Console
from rich.table import Table

# Local modules
from ingredients import store_ingredient, Ingredients
from recipes import new_recipe, Recipes
from csv_functions import read_recipes_from_csv, write_recipes_to_csv, read_ingredients_from_csv
from utils.recipe_api_request import random_recipe_request, recipe_by_ingredient_request, get_recipe_by_id
from utils.helper_functions import word_wrap, remove_html_tags, get_first_sentence

# Console to print the tables
console = Console()

# Introduces the app
def print_inital_welcome():

    welcome_msg = "Welcome to the Digital Dish!\nyour ultimate culinary companion for exploring,\ncreating and savouring delicious dishes!\n\nLet's get started!"

    table = Table()

    table.add_column("Culinary Companion",justify="center", width=55)
    table.add_row(welcome_msg,)

    console.print(table)

def print_goodbye():
    print("\n")
    print("Thank you!".center(60))
    print("We hope you enjoyed using Digital Dish".center(60))
    print("Have a great day!".center(60))

# Load menu for user interaction
def create_menu():
    print("")
    table = Table(title="Main Menu",
                        title_style="bold",
                        title_justify="left")

    table.add_column(width=3)
    table.add_column("Options", justify="left", width=50)

    table.add_row("A.", "Add New Recipe")
    table.add_row("B.", "Add Random Recipe")
    table.add_row("C.", "Generate Recipe Using My Ingredients")
    table.add_row("D.", "My Ingredients")
    table.add_row("E.", "Delete Recipe")
    table.add_row("F.", "View Recipes")
    table.add_row("X.", "Exit")

    console.print(table)

    return input("Enter Selection: ").lower()
    
# Display a single recipe after being selcted
def display_recipe(choice, all_recipes):
    print("")
    # name, ingredients, prep_time, cook_time, serves, steps, description
    # layout a nice display of the recipe selected

    # Title of the entire recipe
    table_title = Table(title=f"{all_recipes[choice - 1].get_name()}",
                        title_style="bold",
                        title_justify="left")
    table_title.add_column("Ready In Minutes")
    table_title.add_column("Servings")
    table_title.add_row(f"{all_recipes[choice - 1].get_ready_in_minutes()}",
                        f"{all_recipes[choice - 1].get_serves()}")

    console.print(table_title)

    # start of the ingredients table
    print("")
    table_ingredient = Table(title="Ingredients",
                        title_style="bold",
                        title_justify="left")
    table_ingredient.add_column("Name", justify="left")
    table_ingredient.add_column("Amount", justify="left")
    table_ingredient.add_column("Unit / Sizing", justify="left")

    all_recipes[choice - 1].display_ingredient_info(table_ingredient, console)

    # Start of the method table
    print("")
    table_method = Table(title="Method",
                        title_style="bold",
                        title_justify="left")
    
    table_method.add_column("Steps", justify="left")
    table_method.add_column("Description", justify="left")
    # Pass itselfs through a display method
    all_recipes[choice - 1].display_methods(all_recipes[choice - 1].get_methods(), table_method, console)

    print("")
    table_description = Table()
    table_description.add_column("Description",justify="left",style="bold",width=100)
    
    table_description.add_row(f"{all_recipes[choice - 1].get_description()}")
    
    console.print(table_description)

# Allow the user to view all recipes on the console
def display_all_recipes(all_recipes, action):
    print("")
    # Display recipes in a table format
    table = Table(title=f"{action} Recipes",
                        title_style="bold",
                        title_justify="left")
    table.add_column("No.", justify="left", min_width=3)
    table.add_column("Name", justify="left", width=30)
    table.add_column("Description", justify="left", width=65)

    count = 0
    for recipe in all_recipes:
        count += 1

        name = get_first_sentence(recipe.get_name())
        description = get_first_sentence(recipe.get_description())

        table.add_row(f"{count}", f"{name}", f"{description}")

    console.print(table)

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
        write_recipes_to_csv(all_recipes, "w")

def view_recipes(action):
    all_recipes = read_recipes_from_csv()

    display_all_recipes(all_recipes, action)
            
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
    # list of 5 recipe titles. + cancel = 0
    # which recipe would you like to view?
        # get id and search in api
        # save recipe
    # remove from list of 5

    # Load ingredients
    ingredients_set = set() # Set of ingredients
    ingredients_set = read_ingredients_from_csv(ingredients_set)

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
        print("")
        table = Table(title="Recipe By Ingredients",
                  title_justify="left",
                  title_style="bold")
    
        table.add_column(width=3)
        table.add_column("Options",justify="left",width=50)

        # Add all recipes from api to a list
        available_recipes = []
        for recipe in response_data:
            if recipe.get("title") not in removed_recipe:
                available_recipes.append(recipe)

        # create a range starting 1 to the length of recipes
        count = list(range(1, len(available_recipes) + 1))

        for i, recipe in enumerate(available_recipes):
            table.add_row(f"{count[i]}.",f"{recipe['title']}")

        table.add_row("0.","Back")
        console.print(table)

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

                write_recipes_to_csv([recipe], "a")
            else:
                print("Invalid input. Please try again.")
        else:
            print("Invalid input. Please try again.")

        # Clear init values
        choice = ""

# App starts here
print_inital_welcome()

# Loop menu until user exits
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

            write_recipes_to_csv([recipe], "a")

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
