from flask import Flask, render_template, request
from recipe_helper import search_recipes, get_recipe_info

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recipes', methods=["GET", "POST"])
def recipes():
    if request.method == "POST":
        query = str(request.form["recipe"])
        results = search_recipes(query)
        print (results)
        if results:
            return render_template("recipe_result.html",  results=results)
        else:
            return render_template("recipes.html", error=True)
    return render_template("recipes.html", error=None)

@app.route('/recipe/<recipe_id>')
def recipe_detail(recipe_id):
    recipe_info = get_recipe_info(recipe_id)
    return render_template('recipe_detail.html', recipe_info=recipe_info)

@app.route('/ingredients')
def ingredients():
    pass

@app.route('/menus')
def menus():
    pass

@app.route('/random')
def random():
    pass

if __name__ == '__main__':
    app.run(debug=True)