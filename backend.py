from flask import Flask, request
import requests
import random

app = Flask(__name__)

# Create a global variable to store the Spoonacular API key
API_KEY = "<17268cd20amsh963ba9a211d5552p19affdjsn8e9414b5b54b>"

# Create a function to search for recipes based on ingredients
def search_recipes(ingredients):
    # Define the API endpoint and parameters
    endpoint = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
    params = {
        "apiKey": API_KEY,
        "query": ",".join(ingredients),
        "number": 10,
    }
    
    # Send a GET request to the API endpoint
    response = requests.get(endpoint, params=params)
    
    # Parse the JSON response and return the list of recipes
    data = response.json()
    return data["results"]

# Create a function to generate a response to the user's message
def generate_response(message):
    # Split the message into individual words and remove any unnecessary words
    words = message.lower().split()
    words = [word for word in words if word not in ["search", "for", "recipe", "recipes", "with", "and"]]
    
    # Search for recipes based on the remaining words
    recipes = search_recipes(words)
    
    # If no recipes were found, return an appropriate message to the user
    if len(recipes) == 0:
        return "Sorry, I couldn't find any recipes with those ingredients. Please try again."
    
    # Otherwise, return a random selection of 5 recipes
    else:
        random.shuffle(recipes)
        recipes = recipes[:5]
        message = "Here are some recipes you can try:\n\n"
        for recipe in recipes:
            message += f"{recipe['title']} (ID: {recipe['id']})\n\n"
        message += "Enjoy!"
        return message

# Create a route to handle incoming messages from the user
@app.route("/", methods=["POST"])
def handle_message():
    # Parse the message from the request body
    data = request.get_json()
    message = data["message"]
    
    # Generate a response to the message
    response = generate_response(message)
    
    # Return the response as a JSON object
    return {"message": response}

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
