from flask import Flask, request, jsonify
from recipe_helper import search_recipes, search_ingredients, get_restaurant_menu, get_random_recipes

app = Flask(__name__)

@app.route('/recipes/search')
def search_recipe():
    query = request.args.get('query')
    if not query:
        return "Error: No query provided."
    recipes = search_recipes(query)
    if recipes:
        return jsonify(recipes)
    else:
        return "Error: Unable to search for recipes."

@app.route('/recipes/ingredients')
def search_ingredient():
    ingredients = request.args.get('ingredients')
    if not ingredients:
        return "Error: No ingredients provided."
    recipes = search_ingredients(ingredients)
    if recipes:
        return jsonify(recipes)
    else:
        return "Error: Unable to search for recipes."

@app.route('/recipes/menu')
def get_menu():
    query = request.args.get('query')
    if not query:
        return "Error: No query provided."
    menu_items = get_restaurant_menu(query)
    if menu_items:
        return jsonify(menu_items)
    else:
        return "Error: Unable to get menu items."

@app.route('/recipes/random')
def get_random():
    tags = request.args.get('tags')
    random_recipes = get_random_recipes(tags)
    if random_recipes:
        return jsonify(random_recipes)
    else:
        return "Error: Unable to get random recipes."

if __name__ == '__main__':
    app.run(debug=True)
