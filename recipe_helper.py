import requests
from pprint import pprint


def search_recipes(query):
    """
    Given query strings (keyword of recipes), return 10 related recipes, including the corresponding ID, title, cooking time, 
    image.
    """

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

    querystring = {
        "query": query,
        "number": "10",
        "instructionsRequired": "true"
    }

    headers = {
        "X-RapidAPI-Key": "17268cd20amsh963ba9a211d5552p19affdjsn8e9414b5b54b",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()["results"]
        recipes = []
        for recipe in data:
         # Check if "image" key exists in dictionary
            if "image" in recipe:
                image_url = recipe["image"]
            else:
                image_url = None

            recipe_info = {
                "id": recipe["id"],
                "title": recipe["title"],
                "readyInMinutes": recipe["readyInMinutes"],
                "image": image_url
            }
            recipes.append(recipe_info)
        return recipes
    else:
        print("Error: Unable to search for recipes.")
        return None


def search_ingredients(ingredients):
    """
    Given ingredients, return 5 related recipes, including the corresponding title, 
    image, used/missed ingredients.
    """

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

    querystring = {"ingredients": ingredients, "number": "5",
                   "ignorePantry": "true", "ranking": "2"}

    headers = {
        "X-RapidAPI-Key": "17268cd20amsh963ba9a211d5552p19affdjsn8e9414b5b54b",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    data = response.json()
    recipes = []
    for recipe in data:
        recipe_info = {}
        recipe_info['title'] = recipe['title']
        recipe_info['image'] = recipe['image']
        used_ingredients = []
        missed_ingredients = []
        for ingredient in recipe['usedIngredients']:
            used_ingredients.append(ingredient['name'])
        for ingredient in recipe['missedIngredients']:
            missed_ingredients.append(ingredient['name'])
        recipe_info['used_ingredients'] = used_ingredients
        recipe_info['missed_ingredients'] = missed_ingredients
        
        # Call search_recipe with recipe title as query
        recipe_result = search_recipes(recipe['title'])
        if recipe_result:
            recipe_info.update(recipe_result[0])
            
        recipes.append(recipe_info)
    return recipes


def get_restaurant_menu(query):
    """
    Given query of recipe, retrun up to 15 recipes in restaurant menus, incluidng the titles, images, and the restaurant names.
    """

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/menuItems/search"

    querystring = {"query": query, "number": "15", "minCalories": "0",
                   "minProtein": "0", "minFat": "0", "minCarbs": "0"}

    headers = {
        "X-RapidAPI-Key": "17268cd20amsh963ba9a211d5552p19affdjsn8e9414b5b54b",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    data = response.json()

    if len(data["menuItems"]) == 0:
        return "No recipe found"
    else:
        recipes = []
        for recipe in data["menuItems"]:
            recipe_info = {
                "title": recipe["title"],
                "image": recipe["image"],
                "restaurant_chain": recipe.get("restaurantChain", "N/A")
            }
            recipe_result = search_recipes(recipe['title'])
            if recipe_result:
                recipe_info.update(recipe_result[0])
            recipes.append(recipe_info)
    return recipes


def get_random_recipes(tags=""):
    """
    Given the tags, randomly return the title of recipes
    """
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"
    headers = {
        "X-RapidAPI-Key": "17268cd20amsh963ba9a211d5552p19affdjsn8e9414b5b54b",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }
    querystring = {"number": "15"}
    if tags:
        querystring["tags"] = tags
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    data = response.json()
    recipes = []
    for recipe in data["recipes"]:
        title = recipe["title"]
        recipe_results = search_recipes(title)
        for recipe_info in recipe_results:
            recipe_info["title"] = title
            recipes.append(recipe_info)  
    return recipes


def get_nutrition(recipe_id):
    """
    Given the recipe_id, return the nutrients, including calories, carb, protein, and fat, and the corresponding percent of daily needs. 
    """

    url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{recipe_id}/nutritionWidget.json"

    headers = {
        "X-RapidAPI-Key": "17268cd20amsh963ba9a211d5552p19affdjsn8e9414b5b54b",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        nutrition = {}
        nutrition['Calories'] = {
            'amount': data['calories']
        }
        for nutrient in data['nutrients']:
            if nutrient['name'] in ['Carbohydrates', 'Protein', 'Fat']:
                nutrition[nutrient['name']] = {
                    'amount': nutrient['amount'],
                    'percent_of_daily_needs': nutrient['percentOfDailyNeeds']
                }
        return nutrition
    else:
        return f"Error {response.status_code}: {response.text}"


def get_recipe_price_breakdown(recipe_id):

    url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{recipe_id}/priceBreakdownWidget.json"
    headers = {
        "X-RapidAPI-Key": "17268cd20amsh963ba9a211d5552p19affdjsn8e9414b5b54b",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        response.raise_for_status()


def get_steps(recipe_id):

    url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{recipe_id}/analyzedInstructions"
    querystring = {"stepBreakdown": "true"}
    headers = {
        "X-RapidAPI-Key": "17268cd20amsh963ba9a211d5552p19affdjsn8e9414b5b54b",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    data = response.json()

    recipe_name = data[0]['name']

    # list of equipment names
    equipment_names = set()
    for step in data[0]['steps']:
        for equipment in step['equipment']:
            equipment_names.add(equipment['name'])

    # list of ingredient names
    ingredient_names = set()
    for step in data[0]['steps']:
        for ingredient in step['ingredients']:
            ingredient_names.add(ingredient['name'])

    # list of recipe steps
    steps = []
    for i, step in enumerate(data[0]['steps'], start=1):
        step_text = f"{i}. {step['step']}"
        steps.append(step_text)

    return {
        'recipe_name': recipe_name,
        'equipment_names': equipment_names,
        'ingredient_names': ingredient_names,
        'steps': steps
    }


def get_similar_recipe(recipe_id):
    """
    Given the recipe id, return similar recipes, including the corresponding title, 
    image, and url for additional information.
    """

    similar_url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{recipe_id}/similar"

    headers = {
        "X-RapidAPI-Key": "17268cd20amsh963ba9a211d5552p19affdjsn8e9414b5b54b",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    similar_response = requests.request("GET", similar_url, headers=headers)
    data = similar_response.json()

    # Recipe ID not found
    if similar_response.status_code == 404:
        return None
    else:
        similar_recipes = []
        for recipe in data:
            # Check if "image" key exists in dictionary
            if "image" in recipe:
                image_url = recipe["image"]
            else:
                image_url = None

            similar_info = {
                "title": recipe["title"],
                "image": image_url,
            }
            similar_recipes.append(similar_info)
        return similar_recipes


def get_recipe_info(recipe_id):
    """
    Given the recipe id, return nutrition, price breakdown, steps, and similar recipes.
    """
    nutrition = get_nutrition(recipe_id)
    price_breakdown = get_recipe_price_breakdown(recipe_id)
    steps = get_steps(recipe_id)
    similar_recipes = get_similar_recipe(recipe_id)
    
    recipe_info = {
        'nutrition': nutrition,
        'price_breakdown': price_breakdown,
        'steps': steps,
        'similar_recipes': similar_recipes
    }
    return recipe_info
    

def main():
    query = "burger"
    recipes1 = search_recipes(query)
    # pprint(recipes1)
    ingredients = "beef, pepper"
    recipes2 = search_ingredients(ingredients)
    # pprint(recipes2)
    recipe3 = get_restaurant_menu(query)
    pprint(recipe3)
    random_vegan_recipe = get_random_recipes(tags="vegan")
    # pprint(random_vegan_recipe)


    recipe_id = 720738  # Replace with your desired recipe ID
    nutrition_info = get_nutrition(recipe_id)
    price = get_recipe_price_breakdown(recipe_id)
    similar_recipe = get_similar_recipe(recipe_id)
    steps = get_steps(recipe_id)

    # pprint(nutrition_info)
    # pprint(price)
    # pprint(similar_recipe)
    # pprint(steps)
    # pprint(get_recipe_info(recipe_id))


if __name__ == '__main__':
    main()