import csv
import os

from recipes import Recipes
from ingredients import Ingredients

# Stored in the data folder
recipes_file = "myapp/data/my_recipes.csv"
ingredients_file = "myapp/data/my_ingredients.csv"

# Store recipe into a csv with headers
def write_recipes_to_csv(recipes, mode):
    try:
        print("Saving...")
        file_exists = os.path.isfile(recipes_file)

        with open(recipes_file, mode, newline="") as file:
            writer = csv.writer(file)

            # Write header only if the file doesn't exist
            if not file_exists or mode == "w":
                writer.writerow(["Name", "Ingredients", "Ready In Minutes", 
                                 "Serving Size", "Steps", "Description", "Status"])

            for current_recipe in recipes:
                if current_recipe.get_status() == "active":
                    # Join methods with a delimiter
                    # methods_str = "; ".join(current_recipe.get_methods())
                    methods_str = "; ".join([", ".join(method) 
                                             if isinstance(method, list) 
                                             else method for method in current_recipe.get_methods()])

                    # Write recipe details including methods
                    writer.writerow([
                        current_recipe.get_name(),
                        current_recipe.get_ingredients_csv(),
                        current_recipe.get_ready_in_minutes(),
                        current_recipe.get_serves(),
                        methods_str,
                        current_recipe.get_description(),
                        current_recipe.get_status()
                    ])

    except IOError:
        print(f"Error writing to '{recipes_file}'")

# Read from csv at the start
def read_recipes_from_csv():
    all_recipes = []

    try:
        with open(recipes_file, mode="r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row['Name']
                ingredients_data = row['Ingredients']
                ingredients = ingredients_data.split('; ') if ingredients_data else []
                ready_in_minutes = row['Ready In Minutes']
                serves = row['Serving Size']
                methods_data = row['Steps']
                methods = methods_data.split('; ') if methods_data else []
                description = row['Description']
                status = row['Status']

                recipe = Recipes(name, ready_in_minutes, serves, description)
                recipe.set_status(status)
                recipe.set_ingredients(ingredients)
                recipe.read_csv_method(methods)
                
                all_recipes.append(recipe)

    except FileNotFoundError:
        print(f"Error - File '{recipes_file}' not found.")
        print("Creating New File...")

    return all_recipes

# Store ingredients into a csv with headers
def write_ingredients_to_csv(ingredients_set):
    
    try:
        if len(ingredients_set) > 0:
            print("Writing to csv...")

            with open(ingredients_file, mode="w", newline="") as file:
                writer = csv.writer(file)

                # Write header
                writer.writerow(["Name", "Amount", "Unit"])

                # Write ingredients
                for ingredient in ingredients_set:
                    writer.writerow(ingredient.store_csv_info().split(','))
        else:
            print("Nothing to submit.")

    except IOError:
        print(f"Error writing to '{ingredients_file}'")

# Read from csv at the start
def read_ingredients_from_csv(ingredients_set):
    ingredients_set = set()  # Set of ingredients

    try:
        with open(ingredients_file, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row

            for row in reader:
                name, amount, unit = row
                ingredients_set.add(Ingredients(name, amount, unit))

    except FileNotFoundError:
        print(f"File '{ingredients_file}' not found.")
        print("Creating New File...")
    
    return ingredients_set