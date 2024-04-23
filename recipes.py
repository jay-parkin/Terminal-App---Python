
from ingredients import store_ingredient
import readline

class Recipes():
    def __init__(self, name="", ingredients="", prepare_time="", 
                 cook_time="", serves="", description=""):
        self._name = name
        self._ingredients = ingredients
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
    def get_ingredients(self):
        return [ingredient._name for ingredient in self._ingredients]

    def set_ingredients(self, ingredients):
        self._ingredients = ingredients if ingredients is not None else set()
    
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

    ingredients_list = current_recipe.get_ingredients()
    ingredients_str = ', '.join(ingredients_list)
    print(f"B. Add Ingredients: {ingredients_str}") # Add a name // sub menu

    print("C. Add Method: ") # Add Methods // sub menu
    print(f"D. Add Prep Time: {current_recipe.get_prepare_time()}") # Add a prepare time
    print(f"E. Add Cook Time: {current_recipe.get_cook_time()}") # Add a cook time
    print(f"F. Serving Size: {current_recipe.get_serves()}") # Add a serving size
    print(f"G. Add Description: {current_recipe.get_description()}") # Add a description
    print("S. Submit & Save") # Submits recipe

    return input("Enter Selection: ").lower()

def method_sub_menu():
    print("\n")
    print("*" * 21 + " Method " + "*" * 21)
    print("A. Add Step") # Add a new steps
    print("B. Edit Step") # Edit a step
    print("S. Submit & Save") # Submit method

    return input("Enter Selection: ").lower()

def add_step(steps_count, current_recipe):
    next_step = f"Step: {steps_count}"
    print(f"\n{next_step}")

    method_step = input("Enter Step: ")
    current_recipe.set_method(f"{next_step}\n{method_step}")

# Allow user to edit method
def edit_step(current_recipe):
    methods = current_recipe.get_methods()

    for method in current_recipe.get_methods():
        print("\n")
        print(method)

    # Find the item index of the method
    while True:
        try:
            removed_step = int(input("Which step would you like to edit (Enter 0 to cancel): "))

            if removed_step < 0 or removed_step > len(methods):
                print(f"Error - Step {removed_step} doesn't exist.")
            else:
                break

        except ValueError:
            print("Error - Please enter a number.")

    if removed_step != 0:
        # Add new step as normal
        edit_step = f"Step: {removed_step}"
        print(f"\n{edit_step}")

        current_edit = methods[removed_step - 1].split("\n")[1]
        method_step = input_with_prefill("Enter Step: ", f"{current_edit}")
        methods[removed_step - 1] =  f"{edit_step}{method_step}"



def input_with_prefill(prompt, text):
    def hook():
        readline.insert_text(text)
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    result = input(prompt)
    readline.set_pre_input_hook()
    return result


# def edit_step(current_recipe):
#     for method in current_recipe.get_methods():
#         print("\n")
#         print(method)

#     # Find the item index of the method
#     removed_step = -1
#     # While input if greater than the length, continue to ask to lower the step number
#     while removed_step < 0 or removed_step >= len(current_recipe.get_methods()):
#         print("\n")
#         removed_step = int(input("Which step would like to edit: "))

#         # Input is higher then length of steps
#         if removed_step < 0 or removed_step > len(current_recipe.get_methods()):
#             print(f"Error - This step doesn't exist: {len(current_recipe.get_methods())}")
#         else:
#             # Add new step as normal
#             edit_step = f"Step: {removed_step}"
#             print(f"\n{edit_step}")

#             method_step = input("Enter Step: ")
#             current_recipe.get_methods[removed_step] =  f"{edit_step}\n{method_step}"


def new_method(current_recipe):

    # Init method list
    method_steps = []
    steps_count = 0 # Load from previous method

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
                print("")

            case _:
                print("Error - invalid selection!")


def new_recipe():
    # initialise an empty object
    current_recipe = Recipes()
    ingredients_set = set() # Set of ingredients

    # Loop menu until user exits
    choice = ""
    while choice != "s":
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
                current_recipe.set_description(input("Desctipion: "))
            
             # Submits recipe to csv
            case "s":
                current_recipe.display_recipe()
                # write_to_csv(ingredients_set, file_name)              

            case _:
                print("Error - invalid selection!")
