import readline
import textwrap

from rich.console import Console
from rich.table import Table

# Local modules
from ingredients import store_ingredient, Ingredients

# Console to print the tables
console = Console()

class Recipes():
    def __init__(self, name="", ready_in_minutes="", serves="", description=""):
        self._name = name
        self._ingredients = []
        self._methods = []
        self._ready_in_minutes = ready_in_minutes
        self._serves = serves
        self._description = description
        self._status = "active"

    # To print recipe
    def display_recipe(self):
        print("Recipe Details:")
        print(f"Name: {self._name}")

        print("Ingredients:")
        for ingredient in self._ingredients:
            print(f"- {ingredient.get_name()}")  

        print("Methods:")
        for method in self._methods:
            print(method)

        print(f"Ready In Minutes: {self._ready_in_minutes}")
        print(f"Serves: {self._serves}")
        print(f"Description: {self._description}")
    
    # Getter and setter for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

   # Getter and setter for ingredients
    def display_ingredient_info(self, table, console):
        for ingredient in self._ingredients:
            table.add_row(f"{ingredient.get_name()}",
                      f"{ingredient.get_amount()}",
                      f"{ingredient.get_unit()}")
        
        console.print(table)
    
    def get_ingredients_csv(self):
        # Join all ingredients data into one string for a single CSV cell
        return "; ".join([ing.store_csv_info() for ing in self._ingredients])

    def get_ingredients(self):
        return self._ingredients

    def add_ingredients(self, ingredients):
        if ingredients:
            self._ingredients.extend(ingredients)

    def clear_ingredients(self):
        self._ingredients = []

    # Initialise ingredients from csv
    def set_ingredients(self, ingredients):
        for ingredient in ingredients:
            ing_name, ing_quantity, ing_unit = ingredient.split(',')
            self._ingredients.append(Ingredients(ing_name, ing_quantity, ing_unit))

    # Getter and setter for method
    def get_methods(self):
        return self._methods
    
    # Initialise methods from csv
    def read_csv_method(self, methods):
        for step in methods:
            step = step.split(',')
            self._methods.append(step)

    def set_method(self, method):
        if method:
            self._methods.append(method)

    # Displaying the selected method from the main class
    def display_methods(self, methods, table, console):
        for i, step in enumerate(methods, start = 1):
            table.add_row(f"Step {i}:", f"{step[0]}")
        
        console.print(table)

    # Getter and setter for ready_in_minutes
    def get_ready_in_minutes(self):
        return self._ready_in_minutes

    def set_ready_in_minutes(self, ready_in_minutes):
        self._ready_in_minutes = ready_in_minutes

    # Getter and setter for serves
    def get_serves(self):
        return self._serves

    def set_serves(self, serves):
        self._serves = serves

    # Getter and setter for description
    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    # Getter and setter for status
    def get_status(self):
        return self._status
    
    def set_status(self, status):
        self._status = status
    
    def set_status_inactive(self):
        self._status = "inactive"

def recipes_sub_menu(current_recipe):
    print("\n")
    table = Table(title="New Recipe",
                  title_style="bold",
                  title_justify="left")

    table.add_column(width=3)
    table.add_column("Options", justify="left")
    table.add_column("Details", justify="left", max_width=30)

    table.add_row("A.", "Add Name", f"{current_recipe.get_name()}") # Add a name
    table.add_row("B.", "Add Ingredients", f"{get_count(current_recipe.get_ingredients(), 'Ingredient')}") # Add a name // sub menu)
    table.add_row("C.", "Add Method", f"{get_count(current_recipe.get_methods(), 'Step')}") # Add Methods // sub menu
    table.add_row("D.", "Add Ready In Minutes", f"{current_recipe.get_ready_in_minutes()}") # Add a prepare time
    table.add_row("E.", "Add Serving Size", f"{current_recipe.get_serves()}") # Add a serving size
    table.add_row("F.", "Description", f"{current_recipe.get_description()}") # Add a description
    table.add_row("S.", "Submit") # Submits recipe
    table.add_row("X.", "Exit") # Exit recipe menu

    console.print(table)

    return input("Enter Selection: ").lower()

def method_sub_menu():
    print("\n")

    table = Table(title="Method",
                  title_style="bold",
                  title_justify="left")

    table.add_column(width=3)
    table.add_column("Options", justify="left",width=20)

    table.add_row("A.", "Add Step") # Add a new steps
    table.add_row("B.", "Edit Step") # Edit a step
    table.add_row("S.", "Submit") # Submit method

    console.print(table)

    return input("Enter Selection: ").lower()

# Gets the count to display
def get_count(list, count_type):
    count = len(list)
    
    if count == 1:
        return f"{count} {count_type}"

    return f"{count} {count_type}s"

# Add a new step to the method
def add_step(steps_count, current_recipe):
    next_step = f"Step {steps_count}:"
    print(f"\n{next_step}")

    method_step = input("Enter Step: ")
    current_recipe.set_method(f"{method_step}")

# Allow user to edit method
def edit_step(current_recipe):
    methods = current_recipe.get_methods()

    print("")
    table = Table(title="Edit Step",
                  title_style="bold",
                  title_justify="left")
    
    table.add_column("Step", justify="left")
    table.add_column("Description", justify="left", max_width=50)
    # Set word wrapping for the Description column
    table.columns[1].overflow = "fold"

    # Counts which step to edit
    count = 0
    for method in methods:
        # print("\n")

        # Edit the selected step
        count += 1
        # edit_step = f"Step {count}:"
        # print(f"\n{edit_step}")

        table.add_row(f"Step {count}:",f"{method}")
    
    console.print(table)


    # Find the item index of the method
    while True:
        try:
            removed_step = int(input("Which step would you like to edit (0 to cancel): "))

            if removed_step < 0 or removed_step > len(methods):
                print(f"Error - Step {removed_step} doesn't exist.")
            else:
                break

        except ValueError:
            print("Error - Please enter a number.")

    if removed_step != 0:
        print("\n")

        # Remove leading/trailing whitespace
        current_edit = methods[removed_step - 1]

        # Wrap the line to fit within 50 characters
        wrapped_edit = textwrap.fill(current_edit, width=50)
        method_step = input_with_prefill("Edit Step: \n", f"{wrapped_edit}")

        # Strip extra newline characters
        methods[removed_step - 1] = f"{method_step.strip()}" 

#  Prefill the input with the last text, to allow the user to edit what exists
def input_with_prefill(prompt, text):
    def hook():
        readline.insert_text(text)
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    result = input(prompt)
    readline.set_pre_input_hook()
    return result

def new_method(current_recipe):
    # Init method list
    method_steps = current_recipe.get_methods()
    steps_count = len(current_recipe.get_methods()) # Load from previous method

    # Loop menu until user exits
    choice = ""
    while choice != "s":
        choice = method_sub_menu()

        # Add switch case to decide selection
        match choice:
            # Add a method
            case "a":
                steps_count += 1
                add_step(steps_count, current_recipe)

            # Allow user to edit a step
            case "b":
                edit_step(current_recipe)

            # Submits methods to recipe
            case "s":
                break

            case _:
                print("Error - invalid selection!")

def new_recipe():
    # initialise an empty object
    current_recipe = Recipes()
    ingredients_set = set() # Set of ingredients

    # Loop menu until user exits
    choice = ""
    while choice not in ["s", "x"]:
        choice = recipes_sub_menu(current_recipe)

        # Add switch case to decide selection
        match choice:
            # Add a name
            case "a":
                current_recipe.set_name(input("Name: "))

            # Add ingredients
            case "b":
                current_recipe.clear_ingredients()
                current_recipe.add_ingredients(store_ingredient(True, ingredients_set))
            
            # Add method
            case "c":
                new_method(current_recipe)  

            # Add ready_in_minutes
            case "d":
                current_recipe.set_ready_in_minutes(input("Ready In Minutes: "))

            # Add serving size
            case "e":
                current_recipe.set_serves(input("Serving Size: "))

            # Add description
            case "f":
                current_recipe.set_description(input("Description: "))
            
             # Submits recipe to csv
            case "s":
                # If a name exist than the recipe exist
                if current_recipe.get_name():
                    from csv_functions import write_recipes_to_csv

                    write_recipes_to_csv([current_recipe], "a") 
                else:
                    # Don't exit this menu is it is unable to save
                    choice = -1
                    print("Error - Recipe name is required.") 

            case "x":
                break  

            case _:
                print("Error - invalid selection!")
