import requests

# Used to pull a random recipe using tags and an amount of recipes
def random_recipe_request(tag_list, request_amount):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

    # "chicken,beef" - tag examples
    querystring = {"tags":tag_list,"number":request_amount}

    headers = {
        "X-RapidAPI-Key": "0bccf89588mshcb9bb8398bc676bp1acf33jsn1a95f7f435b4",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()