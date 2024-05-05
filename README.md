# Digital Dish created by Python

- [Description](#description)
- [Key Features](#key-features)
- [Source Control](#source-control)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisties](#prerequisties)
  - [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
  - [Description](#description-1)
  - [Get Recipe Information](#get-recipe-information)
  - [Get Random Recipes](#get-random-recipes)
  - [Get Search Recipes by Ingredients](#get-search-recipes-by-ingredients)
- [Credits](#credits)

## Description

Digital Dish is like having a personal assistant for food lovers and home cooks. It’s designed in Python to be user-friendly and packed with great features that make managing, finding, and cooking amazing recipes a breeze.

### Key Features

- <b>Create Recipe:</b> Input details recipe information including: Name, Ingredients, Methods, Ready in Minutes, Serving Size, Description.
- <b>Random Recipe Generator:</b> Explore new culinary adventures by fetching random recipes from an external API, sparking creativity in the kitchen.
- <b>Ingredients Management:</b> Add and manage ingredients to create personalised recipe collections or generate recipes based on available ingredients.
- <b>View and Delete:</b> Seamlessly view your saved recipes and easily delete any recipes no longer needed, keeping your collection organised.
- <b>User-Friendly Interface:</b> The app is designed to be really easy to use. Simple menus listed with selection options only consisting of a single letter or number.

<p align="center">
<img src="docs/screenshots/welcome.JPG"/>
</p>

## Source Control

- GitHub Repository - [https://github.com/jay-parkin/Terminal-App-Python](https://github.com/jay-parkin/Terminal-App-Python)
- Clone Repository - `git clone https://github.com/jay-parkin/Terminal-App-Python.git`
  <br>

## Code Style Guide

### Style Guide

This project sticks to the `PEP 8` style guide for Python code, which sets standards for writing neat, easy-to-read, and consistent Python code.<br>
This can be found at https://peps.python.org/pep-0008/

Here are the guidelines as bullet points:

- Indentation: I used a 1 tab indentation to stay consistent with code that is already indented with tabs.
- Line Length: I limit lines to a maximum of 79 characters to make sure they're easy to read without scrolling horizontally.
- Imports: Each module is imported on a separate line, and each import stands on its own line.
- Whitespace: I use whitespace thoughtfully for readability, such as separating functions and classes with two blank lines.
- Naming Conventions:
  - Variables, functions, and methods use lowercase with underscores (snake_case).
  - Classes use CamelCase (capitalising the first letter of each word) without underscores.
  - Constants use all uppercase with underscores (ALL_CAPS).
  - Comments: I used clear and concise comments to explain complex code or document function purposes. <br>Our comment formatting and placement follow PEP 8 guidelines.
- Function and Method Definitions: I use descriptive names for functions and methods.<br>Detailed explanations of their behavior and parameters are provided using docstrings.
- File Encoding: I default to using UTF-8 as the encoding for Python source files.

Through out the entire application I was adhering to the PEP 8 style guide as closely as I can.

## Getting Started

### Prerequisties

- Python 3.10.12 or [higher](https://www.python.org/downloads/)

### Installation

Follow the instructions below to install the Digital Dish application.<br>
This application is run via the terminal and requires the correct Python3 version and project folder structure.<br>
<b>Please copy the follow instructions(where applicable) and paste directly into your linux terminal.</b>

<details>
<summary><b>Unix based Systems - Linux & macOS</b></summary>

1.  Open a Terminal
2.  Clone the GitHub repository:</br>
    via SSH

    ```bash
    git clone git@github.com:jay-parkin/Terminal-App-Python.git
    ```

    via HTTPS

    ```bash
    git clone https://github.com/jay-parkin/Terminal-App-Python.git
    ```

3.  Navigate to `/src` directory in the cloned repository:

    ```bash
    cd Terminal-App-Python/src
    ```

4.  Created an executable from the `run.sh` shell script:

    ```bash
    chmod +x run.sh
    ```

5.  Run the `run.sh` script to start the application

    ```bash
    ./run.sh
    ```

</details>
</br>

<details>
<summary><b>Windows</b></summary>

1.  Install WSL via [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install)

2.  Open a WSL terminal
3.  Clone the GitHub repository (select only 1 method):</br>
    via SSH

    ```bash
    git clone git@github.com:jay-parkin/Terminal-App-Python.git
    ```

    via HTTPS

    ```bash
    git clone https://github.com/jay-parkin/Terminal-App-Python.git
    ```

4.  Navigate to `/src` directory in the cloned repository:

    ```bash
    cd Terminal-App-Python/src
    ```

5.  Created an executable from the `run.sh` shell script:

    ```bash
    chmod +x run.sh
    ```

6.  Run the `run.sh` script to start the application

    ```bash
    ./run.sh
    ```

</details>
</br>

<details>
<summary><b>Failed to Install</b></summary>

If at any point the installation fails, A common issue is `pip` wasn't installed correctly when Python3 was installed.
The following instructions should help get pip installed correctly.

<details>
<summary><b>Show crash log</b></summary>

```
Current Python installed satisfies the required version: 3.10.12.
Proceeding to install required dependencies....
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: /home/{username}/Github/Terminal-App-Python/src/myapp/.venv/bin/python3

Virtual environment created successfully.
./scripts/init_venv.sh: line 17: ./myapp/.venv/bin/activate: No such file or directory
./scripts/init_dependencies.sh: line 20: pip: command not found
Failed to install requirements.
Please try removing .venv and try again.
```

</details>

### Solution

This solution is following the instructions at https://pip.pypa.io/en/stable/installation/

1. Navigate to /scripts directory

   ```bash
   cd scripts
   ```

2. Run the follow command
   ```bash
   python3 get-pip.py
   ```

This will result in pip being downloaded correctly

```bash
Defaulting to user installation because normal site-packages is not writeable
Collecting pip
  Downloading pip-24.0-py3-none-any.whl.metadata (3.6 kB)
Downloading pip-24.0-py3-none-any.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 6.9 MB/s eta 0:00:00
Installing collected packages: pip
Successfully installed pip-24.0
```

</details>

## Dependencies

This application uses the following Python libraries:

- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/): Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.
- [markdown-it-py](https://pypi.org/project/markdown-it-py/): Python port of markdown-it. Markdown parsing, done right!
- [pyreadline3](https://pypi.org/project/pyreadline3/): The pyreadline package is a python implementation of GNU readline functionality it is based on the ctypes based UNC readline package by Gary Bishop.
- [requests](https://pypi.org/project/requests/): Requests is a simple, yet elegant, HTTP library.
- [rich](https://rich.readthedocs.io/en/stable/introduction.html): Rich is a Python library for writing rich text (with color and style) to the terminal, and for displaying advanced content such as tables, markdown, and syntax highlighted code.

These can be found in the `requirements.txt` and will be installed upon running the run.sh shell script.

## Features

The main menu is the main feature of the application which holds most of the operations.

<p align="center">
<img src="docs/screenshots/main.JPG">
</p>

<details>
<summary>Click to expand code</summary>

```python
# Loop menu until user exits
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
            recipe = Recipes()
            #  Find the id from a random reicpe and pass it
            #  into a function to pull the rest of the info
            recipe = get_recipe_from_api(get_recipe_id(random_recipe_request()))

            write_recipes_to_csv([recipe], "a")

        # Generate recipe using my ingredients
        case "c":
            recipe_by_ingredient()

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

```

</details>
<br>

### <b>Recipe Creation:</b>

_<b>New Recipe</b>_

- Input and refine details such as the recipe's name, ingredients, preparation steps, cooking time, servings, and a descriptive narrative.
- Each element of the user's recipe can be independently modified, ensuring the recipe is captured exactly as envisioned. Changes are saved into a structured Recipe object, which neatly collects alongside previously crafted recipes.
- I choice to have this feature perform using a `match case` as I find these very friendly when dealing with predetermined selections. (You will find this has been done through out the application where a menu is needed.)
- Choose from a list of options.
  Selections are handled efficiently through a match case structure.
- Continual interaction is encouraged, except when exiting options ('s' & 'x' are to submit or exit respectively) which trigger specific functions like `A` for adding a recipe name or `F` for the description.

<p align="center">
    <img src="docs/screenshots/new_recipe.JPG"/>
</p>

</br>

_<b>Add Method</b>_

Moving beyond simple ingredient lists, the `Add Method` feature allows for detailed, step-by-step documentation of the recipe creation process:

- `Add Method` allows the user to insert detailed instructions into a mutable `List[]`, a perfect choice for an ordered and adaptable set of directions.

```python
# Add a new step to the method
def add_step(steps_count, current_recipe):
    next_step = f"Step {steps_count}:"
    print(f"\n{next_step}")

    method_step = input("Enter Step: ")
    current_recipe.set_method(f"{method_step}")
```

- Input() will be asked of the user to `Enter Step:` and then stored into a local `method_step` variable.

- This will then append each step into a list which is given to the Recipe object using a setter method.
- This allows the user to add as many steps to a method as they wish.

```python
def set_method(self, method):
    if method:
        self._methods.append(method)
```

- Steps are editable, enabling ongoing refinement and perfecting of the recipe.

<p align="center">
    <img src="docs/screenshots/add_method.JPG"/>
</p>

_<b>Submit Recipe</b>_

- Submitting the recipes stores all the information provided (the name, ingredients, method, ready in minutes, serving size and description) into a Recipe() object.
- Upon filling out the recipe `S. Submit` will become available.

<p align="center">
    <img src="docs/screenshots/new_recipe_filled.JPG"/>
</p>

- The submission process then passes the Recipe object to a file writer, systematically storing each attribute into a CSV file

<details>
<summary>Click to expand code</summary>

```python
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

```

</details>
</br>

### <b>Csv Functions:</b>

The function write_recipes_to_csv(recipes, mode) is all about saving a list of recipes into a CSV file, complete with headers if they're not already there. Let's walk through what happens when you call this function:

- Initiating the save displays "Saving..." to let the user know that it's started the process of writing the recipes to a CSV file.
- The function checks if the CSV file already exists using `os.path.isfile(recipes_file)`. This is crucial because it determines whether the headers need to be added to the file.
- It opens the CSV file specified by recipes_file. The mode parameter can be set to `"w" to write` (which will overwrite any existing file) or `"a" to append` (which adds new data to the existing file). The newline="" parameter is there to make sure that newlines are handled correctly no matter what operating system you're on.
- It sets up a `csv.writer` object, which makes it easy to write rows into the file.
- If the file doesn't exist yet, or if the function overwrites it with mode "w", the function will add a header row first. The headers will be fields like `"Name", "Ingredients", "Ready In Minutes", "Serving Size", "Steps", "Description", and "Status"`.
- The function goes through each recipe in the list provided. It only includes a recipe if its status is marked as "active".
- Before writing out a recipe, if any of the method steps are lists, they are combined into one string, with each step separated by ";". If a step includes a list within it (like nested lists), those are joined by ",". This ensures all the steps are neatly formatted in one cell of the CSV.
- For every active recipe, it writes a row in the CSV file with the recipe’s details such as name, ingredients, ready in minutes, serving size, method, description, and its status.
- If there's any issue opening or writing to the file, an error message will pop up, indicating what went wrong with the file path.

<details>
<summary>Click to expand code</summary>

```python
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
                                             else method for method in
                                             current_recipe.get_methods()])

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
```

</details>
<br>

### <b>Add Random Recipe:</b>

<p align="center">
    <img src="docs/screenshots/random_recipe.JPG"/>
</p>

- Users can retrieve a random recipe from a vast database.
- Provides comprehensive details about a recipe, such as ingredients, cooking methods, and nutritional information.
- Robust error management to ensure the application handles API limits, network issues, and more gracefully.
- Import the following modules:
  - `import json`
  - https://pypi.org/project/requests/
  ```bash
  pip install requests
  ```

#### Usage `get_recipe_from_api(get_recipe_id(random_recipe_request()))`

This feature consists of a few functions which work together to pull api requests and supports the DRY principal

1. <b>random_recipe_request()</b>:

   - Purpose: Fetches a random recipe from Spoonacular.
   - Inputs: None.
   - Outputs: A JSON object containing recipe details.
   - Error Handling: Captures and logs errors related to network issues or API limitations.

   <details>
   <summary>Click to expand code</summary>

   ```python
    import requests

    # Used to pull a random recipe using tags and an amount of recipes
    def random_recipe_request():
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

        # "chicken,beef" - tag examples
        # querystring = {"tags":tag_list,"number":request_amount}
        querystring = {"number":1}

        headers = {
            "X-RapidAPI-Key": "{YOUR-API-KEY}",
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
   ```

   </details>

2. <b>get_recipe_id(data)</b>:

   - Purpose: Extracts the recipe ID from the API response.
   - Inputs: JSON data from `random_recipe_request()`.
   - Outputs: A string representing the recipe ID or None if no recipes are found.

   <details>
   <summary>Click to expand code</summary>

   ```python
    # Find recipes id from the api > https://rapidapi.com/spoonacular/api/recipe-food-nutrition
    def get_recipe_id(data):
        response_data = data

        # Extract title from the first recipe in the response
        if "recipes" in response_data and len(response_data["recipes"]) > 0:
            for recipe_data in response_data["recipes"]:
                id = recipe_data.get("id", "n/a")

            return id
   ```

   </details>

3. <b>get_recipe_by_id(recipe_id)</b>:

   - Purpose: Retrieves detailed information for a specific recipe ID.
   - Inputs: Recipe ID as a string.
   - Outputs: JSON object containing the full recipe information.

   <details>
   <summary>Click to expand code</summary>

   ```python
    def get_recipe_by_id(id):
    url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/information"

    headers = {
        "X-RapidAPI-Key": "{YOUR-API-KEY}",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    return response.json()
   ```

   </details>

4. <b>get_recipe_from_api(id)</b>:

   - Purpose: Constructs a complete recipe object from the recipe ID.
   - Inputs: Recipe ID.
   - Outputs: A Recipe object filled with all relevant data, such as ingredients and instructions.

    <details>
    <summary>Click to expand code</summary>

   ```python
    # Create a recipes from id > pull https://rapidapi.com/spoonacular/api/recipe-food-nutrition
    def get_recipe_from_api(id):

        recipe_data = get_recipe_by_id(id)

        found_recipe = []
        # Extract title from the first recipe in the response
        if recipe_data:
            # recipe name
            title = recipe_data.get("title", "n/a")
            print(f"Adding: {title}")

            # add ingredients
            ingredients = []
            name = ""
            amount = ""
            unit = ""
            extendedIngredients = recipe_data.get("extendedIngredients", [])

            for ingredient in extendedIngredients:
                name = ingredient.get("nameClean")
                amount = ingredient.get("amount")
                unit = ingredient.get("unit")

                ingredients.append(Ingredients(name, amount, unit))

            # method > steps
            methods = []
            length = 0 # Length of each step
            ready_in_minutes = 0
            analyzed_instructions = recipe_data.get("analyzedInstructions", [])

            # move through get instuction and add to step
            for instruction in analyzed_instructions:
                steps = instruction.get("steps", [])
                for step in steps:
                    methods.append(word_wrap(step["step"]))
                    # collect length as well
                    # get ready time from the length of each step
                    # ready_time = recipe_data.get("readyInMinutes", "n/a")
                    length = step["length"]["number"] if "length" in step else 0
                    ready_in_minutes += length

            serves = recipe_data.get("servings", "n/a")

            description = remove_html_tags(recipe_data.get("summary", title))

            # #  Create a Recipes object
            found_recipe = Recipes(title, ready_in_minutes, serves, description)
            found_recipe.add_ingredients(ingredients)
            found_recipe.read_csv_method(methods)

            return found_recipe
        else:
            print("No recipes found..")
   ```

   </details>
   <br>

### <b>Generate Recipe Using My Ingredients:</b>

<p align="center">
    <img src="docs/screenshots/recipe_by_ingredient.JPG"/>
</p>

- This project utilises the Spoonacular Recipe API(details found at [API Reference](#api-reference)) to fetch recipes based on a list of ingredients provided by the user.
- Users can then select recipes to view more details and save them for later reference.

- Import the following modules:
  - `import json`
  - https://pypi.org/project/requests/
    ```bash
    pip install requests
    ```

1. <b>recipe_by_ingredient_request(ingredients)</b>

   - Purpose: Makes an API request to fetch recipes based on the provided ingredients.
   - Parameters:
     - ingredients: A string containing comma-separated ingredient names.
   - Returns: JSON response containing recipe data.

    <details>
   <summary>Click to expand code</summary>

   ```python
   import requests

    def recipe_by_ingredient_request(ingredients):
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

        querystring = {
            "ingredients": ingredients,
            "number":"5",
            "ignorePantry":"true",
            "ranking":"1"
        }

        headers = {
            "X-RapidAPI-Key": "{YOUR-API-KEY}",
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        return response.json()
   ```

    </details>

2. <b>recipe_by_ingredient()</b>

   - Purpose: Allows users to select recipes from the fetched data and save them.
   - Workflow:
     - Reads ingredients from a CSV file.
     - Calls recipe_by_ingredient_request() to fetch recipes.
     - Displays a list of available recipes and prompts the user to select one.
     - Saves the selected recipe to a CSV file for later reference.

    <details>
    <summary>Click to expand code</summary>

   ```python
   # Loads stored ingredients and pulls 5 random recipes from api
   def recipe_by_ingredient():
       # list of 5 recipe titles. + cancel = 0
       # which recipe would you like to view?
           # get id and search in api
           # save recipe
       # remove from list of 5

       # Load ingredients
       ingredients_set = set() # Set of ingredients
       ingredients_set = read_ingredients_from_csv(ingredients_set)

       ingredients = ""
       # Extract name from ingredients
       for ingredient_name in ingredients_set:
           ingredients += ingredient_name.get_name() +","

       response_data = recipe_by_ingredient_request(ingredients)
       # response_data = load_recipe_data("new.json") # used for testing

       # Extract title from all recipes in the response

       removed_recipe = []
       count = []
       choice = ""


       while True:
           print("")
           table = Table(title="Recipe By Ingredients",
                   title_justify="left",
                   title_style="bold")

           table.add_column(width=3)
           table.add_column("Options",justify="left",width=50)

           # Add all recipes from api to a list
           available_recipes = []
           for recipe in response_data:
               if recipe.get("title") not in removed_recipe:
                   available_recipes.append(recipe)

           # create a range starting 1 to the length of recipes
           count = list(range(1, len(available_recipes) + 1))

           for i, recipe in enumerate(available_recipes):
               table.add_row(f"{count[i]}.",f"{recipe['title']}")

           table.add_row("0.","Back")
           console.print(table)

           choice = input("Enter which Recipe to Add: ")

           if choice == "0":
               break

           # append choice
           # Make sure the choice is a number and more than 0 and less then count length
           if choice.isdigit() and 0 < int(choice) <= len(count):
               index = int(choice) - 1 # started at 1

               if 0 <= index < len(available_recipes):
                   selected_title = available_recipes[index]["title"]
                   removed_recipe.append(selected_title)

                   # add recipe to stored list
                   id = available_recipes[index]["id"]


                   # save to csv file
                   recipe = Recipes()
                   recipe = get_recipe_from_api(id)

                   write_recipes_to_csv([recipe], "a")
               else:
                   print("Invalid input. Please try again.")
           else:
               print("Invalid input. Please try again.")

           # Clear init values
           choice = ""
   ```

    </details>

#### Dependencies:

- `read_ingredients_from_csv()`: Reads ingredients from a CSV file.
- `write_recipes_to_csv()`: Writes recipes to a CSV file.
- `get_recipe_from_api()`: Fetches detailed recipe data from the API

<br>

### <b>My Ingredients:</b>

<p align="center">
    <img src="docs/screenshots/add_ingredient.JPG"/>
    <img src="docs/screenshots/my_ingredients.JPG"/>
</p>

This feature allows users to add new ingredients, view existing ingredients, and save ingredients to a CSV file.

- These ingredients are stored locally to `data/my_ingredients.csv`
- All stored ingredients are reference when the user accesses the previous feature `Generate Recipe Using My Ingredient`.

<b>Ingredients Class</b>:
Represents ingredients with attributes for name, amount, and unit.<br>
<b>Menu System</b>:
Provides a menu-driven interface for users to interact with ingredient management functions.<br>
<b>Functionality</b>:

- Add Ingredient: Allows users to input ingredient details and creates an Ingredients object.
- View Ingredients: Displays a table of ingredients with their details.
- Store Ingredients: Saves ingredients to a CSV file for future reference.

<details>
<summary>Click to expand code</summary>

```python
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
```

</details>
<br>

### <b>View & Delete Recipes:</b>

<p align="center">
    <img src="docs/screenshots/view_recipe.JPG"/>
</p>

This feature manages recipes stored in a CSV file. <br>It provides functionality to view all recipes, view a specific recipe, and delete a recipe from the collection.

- Import the following modules:
  - https://pypi.org/project/rich/
    ```bash
    pip install rich
    ```
  - `from rich.console import Console`
  - `from rich.table import Table`

<br>
<b>view_recipes(action)</b><br>
This function acts as the entry point for interacting with recipes.<br>It first reads all recipes from a CSV file using `read_recipes_from_csv()`.<br>Then it calls `display_all_recipes()` to present a table of all recipes to the user, along with the specified action (view or delete). After displaying the recipes, it prompts the user to choose a recipe by number and then performs the appropriate action based on the user's input.

- Purpose: Manage the process of viewing or deleting recipes based on user input.
- Steps:
  - Read recipes from CSV file.
  - Display all recipes with a table.
  - Prompt user for choice and validate input.
  - Perform the selected action (view or delete).

<details>
<summary>Click to expand code</summary>

```python
def view_recipes(action):
    all_recipes = read_recipes_from_csv()

    display_all_recipes(all_recipes, action)

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
```

</details>
<br>

<br>
<b>display_all_recipes(all_recipes, action)</b><br>
This function displays a summary of all recipes available in your system.<br>It formats the recipes into a table, showing their numbers, names, and brief descriptions.<br>The action parameter is used to customise the table's title (e.g., "View Recipes" or "Delete Recipes").

- Purpose: Provide an overview of all available recipes.
- Steps:
  - Format recipes into a table.
  - Display the table with appropriate headers and data.

<details>
<summary>Click to expand code</summary>

```python
# Allow the user to view all recipes on the console
def display_all_recipes(all_recipes, action):
    print("")
    # Display recipes in a table format
    table = Table(title=f"{action} Recipes",
                        title_style="bold",
                        title_justify="left")
    table.add_column("No.", justify="left", min_width=3)
    table.add_column("Name", justify="left", width=30)
    table.add_column("Description", justify="left", width=65)

    count = 0
    for recipe in all_recipes:
        count += 1

        name = get_first_sentence(recipe.get_name())
        description = get_first_sentence(recipe.get_description())

        table.add_row(f"{count}", f"{name}", f"{description}")

    console.print(table)
```

</details>
<br>

<br>
<b>display_recipe(choice, all_recipes)</b><br>
This function is responsible for showing detailed information about a specific recipe chosen by the user.<br>It formats and displays the recipe's name, ingredients, preparation method, and description in a structured manner using the Table class from your environment.

- Purpose: Show detailed information about a selected recipe.
- Steps:
  - Format and display the recipe's basic information (name, serves, etc.).
  - Display ingredients in a table format.
  - Display cooking method (steps and descriptions) in a table format.
  - Display recipe description.

<p align="center">
    <img src="docs/screenshots/view_recipe_details.JPG"/>
</p>

<details>
<summary>Click to expand code</summary>

```python
# Display a single recipe after being selcted
def display_recipe(choice, all_recipes):
    print("")
    # name, ingredients, prep_time, cook_time, serves, steps, description
    # layout a nice display of the recipe selected

    # Title of the entire recipe
    table_title = Table(title=f"{all_recipes[choice - 1].get_name()}",
                        title_style="bold",
                        title_justify="left")
    table_title.add_column("Ready In Minutes")
    table_title.add_column("Servings")
    table_title.add_row(f"{all_recipes[choice - 1].get_ready_in_minutes()}",
                        f"{all_recipes[choice - 1].get_serves()}")

    console.print(table_title)

    # start of the ingredients table
    print("")
    table_ingredient = Table(title="Ingredients",
                        title_style="bold",
                        title_justify="left")
    table_ingredient.add_column("Name", justify="left")
    table_ingredient.add_column("Amount", justify="left")
    table_ingredient.add_column("Unit / Sizing", justify="left")

    all_recipes[choice - 1].display_ingredient_info(table_ingredient, console)

    # Start of the method table
    print("")
    table_method = Table(title="Method",
                        title_style="bold",
                        title_justify="left")

    table_method.add_column("Steps", justify="left")
    table_method.add_column("Description", justify="left")
    # Pass itselfs through a display method
    all_recipes[choice - 1].display_methods(all_recipes[choice - 1].get_methods(), table_method, console)

    print("")
    table_description = Table()
    table_description.add_column("Description",justify="left",style="bold",width=100)

    table_description.add_row(f"{all_recipes[choice - 1].get_description()}")

    console.print(table_description)
```

</details>
<br>

<br>
<b>delete_recipe(choice, all_recipes)</b><br>
When the user chooses to delete a recipe, this function handles the confirmation process and updates the recipe's status accordingly.<br>It confirms the user's choice and then marks the selected recipe as inactive in the system (typically by setting a status flag).

- Purpose: Handle the deletion of a recipe from the system.
- Steps:
  - Confirm user's intention to delete.
  - Mark the selected recipe as inactive or delete it from the system.
  - Update the CSV file to reflect the changes(excluding all recipes with an inactive status).

<details>
<summary>Click to expand code</summary>

```python
# Remove a recipe from the list
def delete_recipe(choice, all_recipes):
    print(f"\nDeleting Recipe: {all_recipes[choice - 1].get_name()}")

    print("1: Yes")
    print("2: No")

    # Confirm the choice to delete
    choice_yes = input("Are you sure? ")

    if choice_yes == "1":
        # Confirmed to delete
        print(f"Deleting...")
        # Set recipe inactive
        all_recipes[choice - 1].set_status_inactive()

        # Write list of recipes without the inacive recipe selected
        write_recipes_to_csv(all_recipes, "w")
```

</details>
<br>

These functions work together to provide a user-friendly interface for managing recipes, displaying information in a structured format, and ensuring data integrity by handling deletions appropriately.

## API Reference

###### Full Attribution: _I didn't write this api, it comes from the amazing source found below_

- https://rapidapi.com/spoonacular/api/recipe-food-nutrition - Recipe - Food - Nutrition By David

#### Description

The spoonacular Recipe - Food - Nutrition API gives you to access to thousands of recipes, storebought packaged foods, and chain restaurant menu items. Our food ontology and semantic recipe search engine makes it possible to search for recipes using natural language queries, such as “gluten free brownies without sugar” or “low fat vegan cupcakes.” You can automatically calculate the nutritional information for any recipe, estimate recipe costs, visualize ingredient lists, find recipes for what’s in your fridge, find recipes based on special diets, nutritional requirements, or favorite ingredients, classify recipes into types and cuisines, convert ingredient amounts, or even compute an entire meal plan. With our powerful API, you can create many kinds of food and nutrition apps.

<p align="center">
    <img src="docs/api/api_title.JPG"/>
</p>

Special diets/dietary requirements currently available include: vegan, vegetarian, pescetarian, gluten free, grain free, dairy free, high protein, low sodium, low carb, Paleo, Primal, ketogenic, and more.

#### Get Recipe Information

```https
  GET url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/information"
```

| Parameter | Type     | Description                         |
| :-------- | :------- | :---------------------------------- |
| `api_key` | `string` | **Required**. Your API key          |
| `id`      | `string` | **Required**. Id of recipe to fetch |

#### Get Random Recipes

```https
  GET url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get Search Recipes by Ingredients

```https
  GET url: 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients'
```

| Parameter | Type     | Description                                |
| :-------- | :------- | :----------------------------------------- |
| `api_key` | `string` | **Required**. Your API key                 |
| `list`    | `string` | **Required**. List of Ingredients to fetch |

<p align="center">
    <img src="docs/api/api_stats.JPG"/>
</p>
