import csv
from ingredients import Ingredients

# Store ingredients into a csv with headers
def write_to_csv(ingredients_set, file_name):
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
def read_from_csv(ingredients_set, file_name):
    
    ingredients_set = set()  
    try:
        with open(file_name, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row

            for row in reader:
                name, amount, unit = row
                ingredients_set.add((name, amount, unit))  # Store as tuple

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        print("Creating New File...")
    return ingredients_set