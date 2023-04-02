<<<<<<< HEAD
# Charlotte Jenny Project OIM3640
 This is a repository for Charlotte Chen and Jenny Ma's Final Project for OIM 3640. 

## 1. The Big Idea

The app is to create a recipe app that is designed specifically for college students and busy employees who are not experienced with culinary and want to try out new recipes. The app will feature easy-to-do recipes that are tailored to the user's head count and personalized ingredient lists according to their preferences. Through talking to a chatbot or searching manually, users will be able to search for recipes, create a shopping list for ingredients, and find what they can do with existing ingredients at hand (users' input) . The minimum viable product (MVP) will be an app that provides basic functionalities, such as recipe search among a existing recipe API, ingredient list creation, search function in list, and chatbot.  To develop the MVP, we will utilize existing APIs for recipes. The stretch goal is to create a web app that allows users to input their data, including their dietary preferences and specialized house recipes into the big recipe database automatically.

## 2. Learning Objectives


## 3. Implementation Plan

Our app has many functions: including chatbot, search engine, create shopping list, find recipes with ingredients at hand (allow user input). It will consist of user interface on web, backend server, database of their saved ingredients and recipes, reciple matching algorithm (Cosine similarity, Jaccard similarity: needs more learning), Chatbox for better searching, and API retrivation. 

We found some existing API:
[Grocery Price for Ingredients](https://www.mealme.ai/?utm_source=google&utm_medium=google+search&utm_campaign=MealMe+API%28Aziz%29&gclid=CjwKCAjw_YShBhAiEiwAMomsEFRvATNS1tZYzWqrq54Nwna2I66WdEtRfPeVY-1DmD4y3hxyFE2cYBoCpxsQAvD_BwE)
[Recipe API](https://spoonacular.com/food-api)

Some libraries we are considering using are:

Flask: to build a web app
Urllib.request: to send HTTP requests to APIs and retrieve data
SQLAlchemy (need more learning): to store and retrieve recipe data to analyze user preference, and provide recommendation
ChatterBot (need more learning): train the recipe bot using the ChatterBotCorpusTrainer through using pre-existing datasets, and generate response accordingly
NTLK: is used with ChatterBot to better tokenize the user input and detect possible cue words to generate responses

## 4. Project Schedule

First week of April (4.3 - 4.9): Find the exact API we are using, learn more about building chatterbot, building simple database in the backend, learn about web building, and create a prototype demo for what our web interface will be like. 

Second week of April (4.10 - 4.16): Start writing code: basics API integration, Flask, start CHATBOX, and search engine within the database. (Also, prepare for mid-project presentation -- subject to date changes)

Third week of April: (4.17 - 4.23): Debugging and try adding new functions beyond our initial MVP, prepare for final demo/ presentation session on 4.25. 

Fourth week of April: (4.24 - 4.29): Finalize codes, create project websites. 

## 5. Collaboration Plan

## 6. Risks and Limitations

## 7. Additional Course Content