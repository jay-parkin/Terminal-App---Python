# Digital Dish created by Python

## Description

Digital Dish is like having a personal assistant for food lovers and home cooks. It’s designed in Python to be user-friendly and packed with great features that make managing, finding, and cooking amazing recipes a breeze.

#### Key Features

- <b>Create Recipe:</b> Input details recipe information including: Name, Ingredients, Methods, Ready in Minutes, Serving Size, Description.
- <b>Random Recipe Generator:</b> Explore new culinary adventures by fetching random recipes from an external API, sparking creativity in the kitchen.
- <b>Ingredients Management:</b> Add and manage ingredients to create personalised recipe collections or generate recipes based on available ingredients.
- <b>View and Delete:</b> Seamlessly view your saved recipes and easily delete any recipes no longer needed, keeping your collection organised.
- <b>User-Friendly Interface:</b> The app is designed to be really easy to use. Simple menus listed with selection options only consisting of a single letter or number.

<p align="center">
<img src="docs/Screenshots/welcome.JPG"/>
</p>

#### Source Control

- GitHub Repository - [https://github.com/jay-parkin/Terminal-App-Python](https://github.com/jay-parkin/Terminal-App-Python)
- Clone Repository - git clone https://github.com/jay-parkin/Terminal-App-Python.git

## Getting Started

### Prerequisties

- Python 3.10.12 or [higher](https://www.python.org/downloads/)

### Configuration

## Usage

## API Reference

- https://rapidapi.com/spoonacular/api/recipe-food-nutrition - Recipe - Food - Nutrition By David

##### Description

The spoonacular Recipe - Food - Nutrition API gives you to access to thousands of recipes, storebought packaged foods, and chain restaurant menu items. Our food ontology and semantic recipe search engine makes it possible to search for recipes using natural language queries, such as “gluten free brownies without sugar” or “low fat vegan cupcakes.” You can automatically calculate the nutritional information for any recipe, estimate recipe costs, visualize ingredient lists, find recipes for what’s in your fridge, find recipes based on special diets, nutritional requirements, or favorite ingredients, classify recipes into types and cuisines, convert ingredient amounts, or even compute an entire meal plan. With our powerful API, you can create many kinds of food and nutrition apps.

Special diets/dietary requirements currently available include: vegan, vegetarian, pescetarian, gluten free, grain free, dairy free, high protein, low sodium, low carb, Paleo, Primal, ketogenic, and more.

#### Get Recipe Information

```https
  GET url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/information"
```

| Parameter | Type     | Description                         |
| :-------- | :------- | :---------------------------------- |
| `id`      | `string` | **Required**. Id of recipe to fetch |

####SS Get Random Recipes

```http
  GET Get Random Recipes
  url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"
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
| `list`    | `string` | **Required**. List of Ingredients to fetch |

## Credits
