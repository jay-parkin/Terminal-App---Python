class Ingredients:
    def __init__(self, name, amount, unit):
        self._name = name
        self._amount = amount
        self._unit = unit

    def display_info(self):
        if self._name == "":
            self._name = "n/a"

        if self._amount == "":
            self._amount = "n/a"

        if self._unit == "":
            self._unit = "n/a"

        return f"Name:\t{self._name}\nAmount:\t{self._amount}\nUnit:\t{self._unit}\n"
    
    def store_csv_info(self):
        return f"{self._name},{self._amount},{self._unit}"
    
    def get_name(self):
        return self._name
    
    def get_amount(self):
        return self._amount
    
    def get_unit(self):
        return self._unit

def ingredients_sub_menu():
    print("\n")
    print("*" * 17 + " My Ingredients " + "*" * 17)
    print("A. Add New Ingredient") # Add a new ingredient to the list
    print("B. View Ingredients") # View ingredients
    print("S. Submit & Save") # Submits ingredients

    return input("Enter Selection: ").lower()

# Add ingredient to set object
def add_ingredient(count):
    print(f"\nIngredient {count}:")
    name = input("Enter Name: ") # Name
    amount = input("Enter Amount: ") # Quantity
    unit = input("Enter Unit: ") # Unit Size g, kg, ml, l

    # Return ingredients class
    return Ingredients(name, amount, unit)

def view_ingredients(ingredient):
    return ingredient.display_info()

def store_ingredient(in_recipe, current_recipe_ingredients=""):
    # Stored locally
    file_name = "my_ingredients.csv"
    
    # Load ingredients
    ingredients_set = set() # Set of ingredients

    # Load local import
    from csv_functions import read_ingredients_from_csv
    ingredients_set = read_ingredients_from_csv(ingredients_set, file_name)

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
                print("\n")
                print("*" * 21 + " Stored " + "*" * 21)
                # If true, print current recipe ingredient, else print stored
                if in_recipe:
                    for ingredient in current_recipe_ingredients:
                        print(view_ingredients(ingredient))
                    
                    print(f"Total: {current_ingredient_count}")
                else:
                    for ingredient in ingredients_set:
                        print(view_ingredients(ingredient))
                    
                    print(f"Total: {stored_ingredient_count}")
                
                

            # Submits ingredients to csv
            case "s":
                # Import local module
                from csv_functions import write_ingredients_to_csv
                write_ingredients_to_csv(ingredients_set, file_name)              

            case _:
                print("Error - Invalid selection!")
    
    return current_recipe_ingredients