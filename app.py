from flask import Flask, render_template, request
import json
from recipe_helper import search_recipes, get_recipe_info, search_ingredients, get_restaurant_menu, get_random_recipes, get_wine_pairing_with_description, get_dish_pairing, get_a_random_food_joke


app = Flask(__name__)


@app.route('/')
def index():
    joke_str = get_a_random_food_joke()
    joke_dict = json.loads(joke_str)
    return render_template("index.html", joke=joke_dict)


@app.route('/recipes', methods=["GET", "POST"])
def recipes():
    if request.method == "POST":
        query = str(request.form["recipe"])
        results = search_recipes(query)
        if results:
            return render_template("recipe_result.html", results=results)
        else:
            return render_template("recipes.html", error=True)
    return render_template("recipes.html", error=None)


@app.route('/ingredients_recipes', methods=["GET", "POST"])
def ingredients_recipes():
    if request.method == "POST":
        query = str(request.form["ingredients_recipes"])
        results = search_ingredients(query)
        if results:
            return render_template("ingredient_result.html",  results=results)
        else:
            return render_template("ingredients.html", error=True)
    return render_template("ingredients.html", error=None)


@app.route('/menus', methods=["GET", "POST"])
def menus():
    if request.method == "POST":
        query = str(request.form["menus"])
        results = get_restaurant_menu(query)
        if results:
            return render_template("menu_result.html",  results=results)
        else:
            return render_template("menus.html", error=True)
    return render_template("menus.html", error=None)


@app.route('/random', methods=["GET", "POST"])
def random():
    if request.method == "POST":
        query = str(request.form["random"])
        results = get_random_recipes(query)
        if results:
            return render_template("random_result.html",  results=results)
        else:
            return render_template("random.html", error=True)
    return render_template("random.html", error=None)


@app.route('/winepairing', methods=["GET", "POST"])
def wine():
    if request.method == "POST":
        query = str(request.form["wine"])
        results = get_wine_pairing_with_description(query)
        if results:
            return render_template("wine_result.html",  results=results)
        else:
            return render_template("wine.html", error=True)
    return render_template("wine.html", error=None)


@app.route('/dishpairing', methods=["GET", "POST"])
def dish():
    if request.method == "POST":
        query = str(request.form["dish"])
        results = get_dish_pairing(query)
        if results:
            return render_template("dish_wine_result.html",  results=results)
        else:
            return render_template("dish_wine.html", error=True)
    return render_template("dish_wine.html", error=None)


@app.route('/recipe/<recipe_id>')
def recipe_detail(recipe_id):
    recipe_info = get_recipe_info(recipe_id)
    return render_template('recipe_detail.html', recipe_info=recipe_info)


if __name__ == '__main__':
    app.run(debug=True)
