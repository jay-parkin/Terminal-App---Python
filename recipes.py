import readline
import textwrap
import csv
import os

# Local modules
from ingredients import store_ingredient

class Recipes():
    def __init__(self, name="", ingredients="", prepare_time="", 
                 cook_time="", serves="", description=""):
        self._name = name
        self._ingredients = []
        self._methods = []
        self._prepare_time = prepare_time
        self._cook_time = cook_time
        self._serves = serves
        self._description = description
    
    # To print recipe
    def display_recipe(self):
        print("Recipe Details:")
        print(f"Name: {self._name}")
        print("Ingredients:")

        # TODO - Not happy with this, need to fix
        for ingredient in self._ingredients:
            print(f"- {ingredient._name}")

        print(f"Method: {self._methods}")
        print(f"Preparation Time: {self._prepare_time}")
        print(f"Cooking Time: {self._cook_time}")
        print(f"Serves: {self._serves}")
        print(f"Description: {self._description}")

    
    
    # Getter and setter for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

   # Getter and setter for ingredients
    def get_ingredients_csv(self):
        # Join all ingredients data into one string for a single CSV cell
        return "; ".join([ing.store_csv_info() for ing in self._ingredients])
    
    def get_ingredients(self):
        return self._ingredients

    def set_ingredients(self, ingredients):
        if ingredients:
            self._ingredients.extend(ingredients)
    
    # Getter and setter for method
    def get_methods(self):
        return self._methods

    def set_method(self, method):
        if method:
            self._methods.append(method)

    # Getter and setter for prepare time
    def get_prepare_time(self):
        return self._prepare_time

    def set_prepare_time(self, prepare_time):
        self._prepare_time = prepare_time

    # Getter and setter for cook time
    def get_cook_time(self):
        return self._cook_time

    def set_cook_time(self, cook_time):
        self._cook_time = cook_time

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

def recipes_sub_menu(current_recipe):
    print("\n")
    print("*" * 19 + " New Recipe " + "*" * 19)
    print(f"A. Add Name: {current_recipe.get_name()}") # Add a name

    print(f"B. Add Ingredients: {get_count(current_recipe.get_ingredients(), 'Ingredient')}") # Add a name // sub menu

    print(f"C. Add Method: {get_count(current_recipe.get_methods(), 'Step')}") # Add Methods // sub menu
    print(f"D. Add Prep Time: {current_recipe.get_prepare_time()}") # Add a prepare time
    print(f"E. Add Cook Time: {current_recipe.get_cook_time()}") # Add a cook time
    print(f"F. Serving Size: {current_recipe.get_serves()}") # Add a serving size
    print(f"G. Add Description: {current_recipe.get_description()}") # Add a description
    print("S. Submit & Save") # Submits recipe
    print("X. Cancel") # Exit recipe menu

    return input("Enter Selection: ").lower()

def method_sub_menu():
    print("\n")
    print("*" * 21 + " Method " + "*" * 21)
    print("A. Add Step") # Add a new steps
    print("B. Edit Step") # Edit a step
    print("S. Submit") # Submit method

    return input("Enter Selection: ").lower()

# Store recipe into a csv with headers
def write_to_csv(current_recipe, file_name):
    try:
        print("Writing to csv...")
        file_exists = os.path.isfile(file_name)

        with open(file_name, mode="a", newline="") as file:
            writer = csv.writer(file)

            # Write header only if the file doesn't exist
            if not file_exists:
                # Write header
                writer.writerow(["Name", "Ingredients", "Prep Time", 
                                    "Cook Time", "Serving Size", "Description"])

            # Write recipe details
            writer.writerow([
                current_recipe.get_name(),
                current_recipe.get_ingredients_csv(),
                current_recipe.get_prepare_time(),
                current_recipe.get_cook_time(),
                current_recipe.get_serves(),
                current_recipe.get_description()
            ])

    except IOError:
        print(f"Error writing to '{file_name}'")

# Gets the count to display
def get_count(list, count_type):
    count = len(list)
    
    if count == 1:
        return f"{count} {count_type}"

    return f"{count} {count_type}s"

# Wraps the method into 50 chartacters when saved
def wrap_input(prompt, width=50):
    # Display the prompt and get user input
    user_input = input(prompt)

    # Wrap the input text horizontally to the specified width
    wrapped_lines = [user_input[i:i+width] for i in range(0, len(user_input), width)]
    wrapped_input = "\n".join(wrapped_lines)

    return wrapped_input

# Add a new step to the method
def add_step(steps_count, current_recipe):
    next_step = f"Step {steps_count}:"
    print(f"\n{next_step}")

    method_step = wrap_input("Enter Step: ")
    current_recipe.set_method(f"{next_step}\n{method_step}")

# Allow user to edit method
def edit_step(current_recipe):
    methods = current_recipe.get_methods()

    for method in current_recipe.get_methods():
        print("\n")
        print(textwrap.fill(method, width=50))

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
        print("*" * 22 + " Edit " + "*" * 22)
        # Edit the selected step
        edit_step = f"Step {removed_step}:"
        print(f"\n{edit_step}")

        # Remove leading/trailing whitespace
        current_edit = methods[removed_step - 1].split(":")[1].strip()  

        # Wrap the line to fit within 50 characters
        wrapped_edit = textwrap.fill(current_edit, width=50)
        method_step = input_with_prefill("Enter Step: \n", f"{wrapped_edit}")

        # Strip extra newline characters
        methods[removed_step - 1] = f"{edit_step}\n{method_step.strip()}" 

#  Prefill the input with the last text, to allow the user to edit what exists
def input_with_prefill(prompt, text, width=50):
    def hook():
        # Split text into lines and strip leading/trailing whitespace
        lines = [line.strip() for line in text.split("\n")]
        # Wrap each line to specified width
        wrapped_lines = [textwrap.fill(line, width=width) for line in lines]
        # Join wrapped lines
        wrapped_text = "\n".join(wrapped_lines)
        readline.insert_text(wrapped_text)
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
    # Stored locally
    file_name = "my_recipes.csv"

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
                current_recipe.set_ingredients(store_ingredient(True, ingredients_set))

            # Add method
            case "c":
                new_method(current_recipe)  

            # Add prep time
            case "d":
                current_recipe.set_prepare_time(input("Prep time: "))

            # Add cook time
            case "e":
                current_recipe.set_cook_time(input("Cook Time: "))

            # Add serving size
            case "f":
                current_recipe.set_serves(input("Serving Size: "))

            # Add description
            case "g":
                current_recipe.set_description(input("Description: "))
            
             # Submits recipe to csv
            case "s":
                # If a name exist than the recipe exist
                if current_recipe.get_name():
                    write_to_csv(current_recipe, file_name) 
                else:
                    # Don't exit this menu is it is unable to save
                    choice = -1
                    print("Error - Recipe name is required.") 

            case "x":
                break  

            case _:
                print("Error - invalid selection!")
