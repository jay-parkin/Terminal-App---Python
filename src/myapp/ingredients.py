from rich.console import Console
from rich.table import Table

# Console to print the tables
console = Console()

class Ingredients:
    def __init__(self, name, amount, unit):
        self._name = name
        self._amount = amount
        self._unit = unit
    
    def store_csv_info(self):
        return f"{self._name},{self._amount},{self._unit}"
    
    def get_name(self):
        return self._name
    
    def get_amount(self):
        return self._amount
    
    def get_unit(self):
        return self._unit

def ingredients_sub_menu():
    print("")

    table = Table(title="My Ingredients",
                        title_style="bold",
                        title_justify="left")

    table.add_column()
    table.add_column("Options",justify="left")

    table.add_row("A.", "Add New Ingredient") # Add a new ingredient to the list
    table.add_row("B.", "View Ingredients") # View ingredients
    table.add_row("S.", "Submit & Save") # Submits ingredients

    console.print(table)

    return input("Enter Selection: ").lower()

# Add ingredient to set object
def add_ingredient(count):
    print(f"\nIngredient {count}:")
    name = input("Enter Name: ") # Name
    amount = input("Enter Amount: ") # Quantity
    unit = input("Enter Unit: ") # Unit Size g, kg, ml, l

    if name == "":
        name = "n/a"

    if amount == "":
        amount = "n/a"

    if unit == "":
        unit = "n/a"

    # Return ingredients class
    return Ingredients(name, amount, unit)

def view_ingredients(current_recipe_ingredients):
    print("")

    table = Table(title="View Ingredients",
                  title_style="bold",
                  title_justify="left")
    
    table.add_column("Name", justify="left")
    table.add_column("Amount", justify="left")
    table.add_column("Unit / Sizing", justify="left")

    for ingredient in current_recipe_ingredients:
            table.add_row(f"{ingredient.get_name()}",
                      f"{ingredient.get_amount()}",
                      f"{ingredient.get_unit()}")
        
    console.print(table)

def store_ingredient(in_recipe, current_recipe_ingredients=""):
     
    # Load ingredients
    ingredients_set = set() # Set of ingredients
    
    # Load local import
    from csv_functions import read_ingredients_from_csv
    ingredients_set = read_ingredients_from_csv(ingredients_set)

    # Init count
    stored_ingredient_count = len(ingredients_set)
    current_ingredient_count = len(current_recipe_ingredients)

    # Loop menu until user exits
    choice = ""

    while choice != "s":
        choice = ingredients_sub_menu()

        # Add switch case to decide selection
        match choice :
            # Add new Ingredient to Ingredients class
            case "a":
                if in_recipe: # If this class has been reached from the recipe class, pass true
                    # Storing only for current recipe
                    current_ingredient_count += 1
                    current_recipe_ingredients.add(add_ingredient(current_ingredient_count))
                else:
                    stored_ingredient_count += 1
                    ingredients_set.add(add_ingredient(stored_ingredient_count))
 
            # View Ingredients
            case "b":
                # If true, print current recipe ingredient, else print stored
                if in_recipe:
                    view_ingredients(current_recipe_ingredients)

                    print(f"Total: {current_ingredient_count}")
                else:
                    view_ingredients(ingredients_set)
                    
                    print(f"Total: {stored_ingredient_count}")
                
            # Submits ingredients to csv
            case "s":
                # Import local module
                from csv_functions import write_ingredients_to_csv
                write_ingredients_to_csv(ingredients_set)              

            case _:
                print("Error - Invalid selection!")
    
    return current_recipe_ingredients