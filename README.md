# Charlotte Jenny Project OIM3640
 This is a repository for Charlotte Chen and Jenny Ma's Final Project for OIM 3640. 

## 1. The Big Idea

 This project's primary objective is to provide college students with easy-to-prepare recipes and shopping lists based on raw materials, enabling users to construct a weekly menu plan to facilitate ingredient preparation planning.

 The app is to create a recipe app that is designed specifically for college students and busy employees who are not experienced with culinary and want to try out new recipes. The app will feature easy-to-do recipes that are tailored to the user's personalized ingredient lists according to their choice. Through talking to a chatbot or searching manually, users will be able to search for recipes under certain category, and create a shopping list for ingredients with total price. The minimum viable product (MVP) will be an app that provides basic functionalities, such as recipe search among a existing recipe API, ingredient list creation, search function in list, and chatbot.  To develop the MVP, we will utilize existing APIs for recipes. The stretch goal is to create a web app that allows users to input their data, including their dietary preferences and specialized house recipes into the big recipe database automatically.

## 2. Learning Objectives

 **1. Shared Learning Goals**
 a. To construct a Minimum Viable Product (MVP), it will be necessary to comprehend the fundamentals of software development, including programming languages, software architecture, and software development processes.
 b. We will learn how to collaborate with other team members, effectively communicate, and share responsibilities.
 c. As we develop our MVP of app using flask, we will learn how to manage the product, including defining and prioritizing product features and comprehending user requirements.

 **2. Individual Learning Goals**
 a. We will learn how to develop software using Python and other tools, especially on API, CHATBOT, and FLASK. 
 b. To guarantee the successful deliverance of the software, we will acquire project management skills such as task management, time management, risk management etc. 


## 3. Implementation Plan

O ur app has many functions: including chatbot, search engine according to category, and shopping list with price generator. It will consist of user interface on web, backend server, reciple matching algorithm (Cosine similarity, Jaccard similarity: needs more learning), Chatbot for better searching, and API retrivation. 

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

 We will firstly start brainstorming the structure of the codes, and divide the work according to parts. For example, when Jenny is more proficient in using Flask, Charlotte can explore more upon Chatbox and NTLK topic detections. We will work on making the website and the presentation together. In optimal scenarios, we will try to meet in person three times a week, 2-3 hours each time when we write the codes and update each other on our progress. We will mainly use agile development. The three functions of the app is separated and independent to each other. We can start three at the same time. This software development method offers us a chance to always start small, debug, and make quick changes according to professor and peers' feedbacks. Through the iterations of "Plan, Collaborate, and Deliver (Feedback)" on a daily basis, we can improve efficiency in coding and especially debugging because we only need to debug small amount of codes at one time. It is much easier for us as beginners. 

## 6. Risks and Limitations

 One huge risk is the Chatbot response. While we are ambitious in providing more diverse responses for different triggers (without implementing self-generated ML response), we are afraid that we may not be able to accurately identify the user's keywords and provide accurate answers, as this requires a vast quantity of data and an entirely new skill set.

 Although we have some experience with the API, we are not yet proficient in categorizing information and converting it to a web application with Flask. We are concerned that we will not be able to categorize it effectively or provide accurate results based on the terms entered by users. Simultaneously, we desired to acquire additional skills to make our web pages more dynamic and aesthetically pleasing. However, this meant that we had to acquire a large number of new skills, which presented a time-related challenge for us.

## 7. Additional Course Content

 One very useful Course Content will be Natural Language Processing, which will tokenize the users' input, delete stop words, meaningless words, repetitive words.etc. Some popular NLP libraries that you can use in Python include NLTK, spaCy, and TextBlob.

 We also need Chatterbot Library that provides an easy way to generate automated responses to user inputs and a corpus, which is a collection of data used to train the chatterbot.