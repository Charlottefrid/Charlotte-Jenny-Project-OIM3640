import requests
from pprint import pprint

# # search recipe

# url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

# querystring = {"query":"burger","diet":"vegetarian","excludeIngredients":"coconut","intolerances":"egg, gluten","number":"10","offset":"0","type":"main course"}

# headers = {
# 	"X-RapidAPI-Key": "17268cd20amsh963ba9a211d5552p19affdjsn8e9414b5b54b",
# 	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# pprint(response.text)

# # get recipe info

# url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/479101/information"

# headers = {
# 	"X-RapidAPI-Key": "17268cd20amsh963ba9a211d5552p19affdjsn8e9414b5b54b",
# 	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers)

# pprint(response.text)

# search by ingredients

# url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

# querystring = {"ingredients":"apples,flour,sugar","number":"5","ignorePantry":"true","ranking":"2"}

# headers = {
# 	"X-RapidAPI-Key": "17268cd20amsh963ba9a211d5552p19affdjsn8e9414b5b54b",
# 	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# pprint(response.text)

# similar

# url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/156992/similar"

# headers = {
# 	"X-RapidAPI-Key": "17268cd20amsh963ba9a211d5552p19affdjsn8e9414b5b54b",
# 	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers)

# pprint(response.text)

# random

# url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/156992/similar"

# headers = {
# 	"X-RapidAPI-Key": "17268cd20amsh963ba9a211d5552p19affdjsn8e9414b5b54b",
# 	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers)

# pprint(response.text)

# restaurant menu

# url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/menuItems/search"

# querystring = {"query":"burger","offset":"0","number":"10","minCalories":"0","maxCalories":"5000","minProtein":"0","maxProtein":"100","minFat":"0","maxFat":"100","minCarbs":"0","maxCarbs":"100"}

# headers = {
# 	"X-RapidAPI-Key": "17268cd20amsh963ba9a211d5552p19affdjsn8e9414b5b54b",
# 	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# pprint(response.text)

# price breakdown

# url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/1003464/priceBreakdownWidget.json"

# headers = {
# 	"X-RapidAPI-Key": "17268cd20amsh963ba9a211d5552p19affdjsn8e9414b5b54b",
# 	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers)

# pprint(response.text)

# steps

# url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/324694/analyzedInstructions"

# querystring = {"stepBreakdown":"true"}

# headers = {
# 	"X-RapidAPI-Key": "17268cd20amsh963ba9a211d5552p19affdjsn8e9414b5b54b",
# 	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# pprint(response.text)

# wine pairin
