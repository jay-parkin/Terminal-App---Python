import csv
import os

from recipes import Recipes
from ingredients import Ingredients

# Store recipe into a csv with headers
# def write_recipes_to_csv(current_recipe, file_name, mode):
#     try:
#         if current_recipe.get_status() == "active":
#             print("Writing to csv...")
#             file_exists = os.path.isfile(file_name)

#             with open(file_name, mode, newline="") as file:
#                 writer = csv.writer(file)

#                 # Write header only if the file doesn't exist
#                 if not file_exists:
#                     # Write header
#                     writer.writerow(["Name", "Ingredients", "Prep Time", 
#                                         "Cook Time", "Serving Size", "Methods", "Description", "Status"])

#                 # Join methods with a delimiter
#                 methods_str = "; ".join(current_recipe.get_methods())

#                 # Write recipe details including methods
#                 writer.writerow([
#                     current_recipe.get_name(),
#                     current_recipe.get_ingredients_csv(),
#                     current_recipe.get_prepare_time(),
#                     current_recipe.get_cook_time(),
#                     current_recipe.get_serves(),
#                     methods_str,
#                     current_recipe.get_description(),
#                     current_recipe.get_status()
#                 ])

#     except IOError:
#         print(f"Error writing to '{file_name}'")

def write_recipes_to_csv(recipes, file_name, mode):
    try:
        print("Writing to csv...")
        file_exists = os.path.isfile(file_name)

        with open(file_name, mode, newline="") as file:
            writer = csv.writer(file)

            # Write header only if the file doesn't exist
            if not file_exists or mode == "w":
                writer.writerow(["Name", "Ingredients", "Prep Time", 
                                 "Cook Time", "Serving Size", "Steps", "Description", "Status"])



            for current_recipe in recipes:
                if current_recipe.get_status() == "active":
                    # Join methods with a delimiter
                    methods_str = "; ".join(current_recipe.get_methods())

                    # Write recipe details including methods
                    writer.writerow([
                        current_recipe.get_name(),
                        current_recipe.get_ingredients_csv(),
                        current_recipe.get_prepare_time(),
                        current_recipe.get_cook_time(),
                        current_recipe.get_serves(),
                        methods_str,
                        current_recipe.get_description(),
                        current_recipe.get_status()
                    ])

    except IOError:
        print(f"Error writing to '{file_name}'")

# Read from csv at the start
def read_recipes_from_csv(file_name):
    all_recipes = []

    try:
        with open(file_name, mode="r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row['Name']
                ingredients_data = row['Ingredients']
                ingredients = ingredients_data.split('; ') if ingredients_data else []
                prepare_time = row['Prep Time']
                cook_time = row['Cook Time']
                serves = row['Serving Size']
                methods_data = row['Steps']
                methods = methods_data.split('; ') if methods_data else []
                description = row['Description']
                status = row['Status']

                recipe = Recipes(name, prepare_time, cook_time, serves, description)
                recipe.set_status(status)
                recipe.set_ingredients(ingredients)
                recipe.read_csv_method(methods)
                all_recipes.append(recipe)

    except FileNotFoundError:
        print(f"Error - File '{file_name}' not found.")
        print("Creating New File...")

    return all_recipes

# Store ingredients into a csv with headers
def write_ingredients_to_csv(ingredients_set, file_name):
    try:
        if len(ingredients_set) > 0:
            print("Writing to csv...")

            with open(file_name, mode="w", newline="") as file:
                writer = csv.writer(file)

                # Write header
                writer.writerow(["Name", "Amount", "Unit"])

                # Write ingredients
                for ingredient in ingredients_set:
                    writer.writerow(ingredient.store_csv_info().split(','))
        else:
            print("Nothing to submit.")

    except IOError:
        print(f"Error writing to '{file_name}'")

# Read from csv at the start
def read_ingredients_from_csv(ingredients_set, file_name):
    ingredients_set = set()  # Set of ingredients

    try:
        with open(file_name, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row

            for row in reader:
                name, amount, unit = row
                ingredients_set.add(Ingredients(name, amount, unit))

    except FileNotFoundError:
        print(f"Error - File '{file_name}' not found.")
        print("Creating New File...")
    
    return ingredients_set