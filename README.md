<<<<<<< HEAD>>>>>>>>
# Charlotte Jenny Project OIM3640
 This is a repository for Charlotte Chen and Jenny Ma's Final Project for OIM 3640. 

## 1. The Big Idea
This project's primary objective is to provide college students with easy-to-prepare recipes and shopping lists based on raw materials, enabling users to construct a weekly menu plan to facilitate ingredient preparation planning.

The app is to create a recipe app that is designed specifically for college students and busy employees who are not experienced with culinary and want to try out new recipes. The app will feature easy-to-do recipes that are tailored to the user's personalized ingredient lists according to their choice. Through talking to a chatbot or searching manually, users will be able to search for recipes under certain category, and create a shopping list for ingredients with total price. The minimum viable product (MVP) will be an app that provides basic functionalities, such as recipe search among a existing recipe API, ingredient list creation, search function in list, and chatbot.  To develop the MVP, we will utilize existing APIs for recipes. The stretch goal is to create a web app that allows users to input their data, including their dietary preferences and specialized house recipes into the big recipe database automatically.

## 2. Learning Objectives
**1. Shared Learning Goals**
a. To construct a Minimum Viable Product (MVP), it will be necessary to comprehend the fundamentals of software development, including programming languages, software architecture, and software development processes.
b. We will learn how to collaborate with other team members, effectively communicate, and share responsibilities.
c. As we develop our MVP, we will learn how to manage the product, including defining and prioritizing product features and comprehending user requirements.

**2. Individual Learning Goals**
a. We will learn how to develop software using Python and other tools.
b. To guarantee the successful deliverance of the software, we will acquire project management skills such as task management, time management, risk management etc.


## 3. Implementation Plan

Our app has many functions: including chatbot, search engine according to category, and shopping list with price generator. It will consist of user interface on web, backend server, reciple matching algorithm (Cosine similarity, Jaccard similarity: needs more learning), Chatbot for better searching, and API retrivation. 

We found some existing API:
1. [Grocery Price for Ingredients](https://www.mealme.ai/?utm_source=google&utm_medium=google+search&utm_campaign=MealMe+API%28Aziz%29&gclid=CjwKCAjw_YShBhAiEiwAMomsEFRvATNS1tZYzWqrq54Nwna2I66WdEtRfPeVY-1DmD4y3hxyFE2cYBoCpxsQAvD_BwE)
2. [Recipe API](https://spoonacular.com/food-api)

Some libraries we are considering using are:

1. Flask: to build a web app
2. Urllib.request: to send HTTP requests to APIs and retrieve data
3. ChatterBot (need more learning): train the recipe bot using the ChatterBotCorpusTrainer through using pre-existing datasets, and generate response accordingly
4. NTLK: is used with ChatterBot to better tokenize the user input and detect possible cue words to generate responses

## 4. Project Schedule

First week of April (4.3 - 4.9): Find the exact API we are using, learn more about building chatterbot, building simple database in the backend, learn about web building, and create a prototype demo for what our web interface will be like. 

Second week of April (4.10 - 4.16): Start writing code: basics API integration, Flask, start CHATBOX, and search engine within the database. (Also, prepare for mid-project presentation -- subject to date changes)

Third week of April: (4.17 - 4.23): Debugging and try adding new functions beyond our initial MVP, prepare for final demo/ presentation session on 4.25. 

Fourth week of April: (4.24 - 4.29): Finalize codes, create project websites. 

## 5. Collaboration Plan

## 6. Risks and Limitations

## 7. Additional Course Content