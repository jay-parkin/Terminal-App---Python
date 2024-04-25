import csv
from ingredients import store_ingredient
from recipes import new_recipe, Recipes

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

# Read from csv at the start
def read_from_csv(file_name):
    all_recipes = [] # list of ingredients

    try:
        with open(file_name, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row

            for row in reader:
                name, ingredients, prep_time, cook_time, serves, description = row
                all_recipes.append(Recipes(name, ingredients, prep_time, 
                                        cook_time, serves, description))

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        print("Creating New File...")
    
    return all_recipes

def display_recipe(choice):
    # only used to adjust the title length
    choice_str = str(choice)
    choice_len = len(choice_str)
    title_spacing = 50 - int((choice_len + 9)) # 9 is the length of the word ' Recipe '
    half_spacing = int(title_spacing / 2)

    print(f"title: {title_spacing}")
    print(f"haalf: {half_spacing}")


    print("\n")
    print("*" * half_spacing + f" Recipe {choice} " + "*" * half_spacing)

def view_recipes():
    print("\n")
    print("*" * 18 + " View Recipes " + "*" * 18)
    all_recipes = read_from_csv("my_recipes.csv")
    
    count = 0
    for recipe in all_recipes:
        count += 1
        print(f"{count}: {recipe.get_name()}")
        
    print("\n")

    try:
        choice = int(input("Enter which Recipe to view: "))

        # Check user input is within list range
        if choice == 0 or choice > len(all_recipes):
            print(f"Recipe {choice} doesn't exist.")

        else:
            display_recipe(choice)

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
            print("")

        # View recipes // read csv
        case "f":
            view_recipes()

        # Exit app
        case "x":
            print_goodbye()
            break

        case _:
            print("Error - Invalid selection!")