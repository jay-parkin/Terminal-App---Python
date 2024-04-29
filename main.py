from ingredients import store_ingredient, Ingredients
from recipes import new_recipe
from csv_functions import read_recipes_from_csv, write_recipes_to_csv

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
    
    print(f"Prep Time")
    print(f"\t{all_recipes[choice - 1].get_prepare_time()}")

    print(f"\nCook Time")
    print(f"\t{all_recipes[choice - 1].get_cook_time()}")

    print(f"\nServing Size")
    print(f"\t{all_recipes[choice - 1].get_serves()}")

    print(f"\nMethod")
    # Pass itselfs through a display method
    all_recipes[choice - 1].display_methods(all_recipes[choice - 1].get_methods())

    print(f"\nDescription")
    print(f"{all_recipes[choice - 1].get_description()}")


# Allow the user to view all recipes on the console
def display_all_recipes(all_recipes):
    print("\n")
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
    print(f"\nDeleting Recipe: {choice}")

    print("1: Yes")
    print("2: No")

    # Confirm the choice to delete
    choice_yes = input("Are you sure? ") 

    if choice_yes == "1":
        # Confirmed to delete
        print(f"Deleting {all_recipes[choice - 1].get_name()}...")
        # Set recipe inactive
        all_recipes[choice - 1].set_status_inactive()
        print(f"{all_recipes[choice - 1].get_name()} is now: {all_recipes[choice - 1].get_status()}")

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
            print("")

        # Generate recipe using my ingredients
        case "c":
            print("")

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
