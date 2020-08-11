# The Online Kitchen

The Online Kitchen is a food blog site created for users to share and explore culinary experiences within an online community. Whether they are looking for instructions on a specific recipe 
or wanting to share a long held secret family recipe the site has something for everyone and is driven by user created content. Aside from this it also contains 
advertising for Global Knives, professional chef knives for use at home.

## Table of Content
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Colour Scheme**](#colour-scheme)
        - [**Wireframes**](#wireframes)
        - [**Icons**](#icons)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features left to implement**](#features-left-to-implement)
    - [**Technologies Used**](#technologies-used)
3. [**Testing**](#testing)

4. [**Deployment**](#deployment)

5. [**Credits**](#credits)

6. [**Content**](#content)

7. [**Media**](#media)

8. [**Acknowledgements**](#acknowledgements)


## UX

The website was mainly aimed at people who like cooking and like food and have experience with the former. However, with the addition of the difficulty rating 
for each recipe, it is hoped that it will also cater to a novice home cook as well. With an easy to use search function there are many ways to search other users content and 
to then add that content to a list of favourites, meaning a user can easily come back to it. Adding a recipe is easy and can be done by guest users and registered users alike hopefully keeping a broad 
range of content available to all. 

## Design

Balsamic IQ was used to create wireframes of different resolutions for each of the pages on the site. See the link below:  
[Wireframes](https://balsamiq.cloud/sseslm8/pk2omam)

## Theme 
Materialize was used to provide general themes on inputs buttons and other features to provide continuity and a consistent style for the site.

## Fonts
The font chosen is the Helvetica Neue which is the default for Materialize to provide a clean professional look for all pages while being relatively 
minimal to ease readability



### User Stories

* As a novice in the kitchen, I want to find a recipe that is easy, so that I can practice and improve my skills. 

* As someone who does not know what to eat tonight, I am looking for a recipe, to provide me with inspiration. 

* As a user with limited time, I want to find a recipe that does not take too long, so that I can make it quickly and save time. 

* As an experienced home cook, I want to share a special take on a classic recipe that noone has tried before, to show everyone a different/ easier way of doing things. 

* As a professional chef, I am looking to share some of my own recipes, so that I become more well known for my skills. 

* As a cooking equipment supplier, I want to increase the outreach of my brand, so that I can boost sales and revenue. 

* As a general user, I want to view the site on many forms of devices including mobile, desktop and tablet.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features
Featured recipes - A selection of up to 10 random recipes are displayed on the user home page.

Recipe Search - The user can search for recipes via their name, the person who added them, the cooking time or the difficulty. 

Register/Log In - A user can choose to become a member of the site by registering and logging in (see favourite recipe). 

Add recipe - A recipe can be added using the form available in an easy to use and responsive way. 

Edit Recipe - A recipe can be editted once a user is logged in to correct any errors. 

Remove recipe - Should a user think better about sharing a recipe and want to remove it this can be completed from the user home page. 

Favourite recipe - For members of the site, recipes can be added to a list of favourites, meaning that the user can come back to them later. They can also remove from this list if they tried a recipe and don't like it. 

### Existing Features
Recipe Search - allows users in search of a recipe to find recipes, by having them fill out the search box and select box on the index.html or userhome.html page. 

Register/Log In - allows users to become members, by having them fill out the registration form by clicking sign-up on any of the base.html versions and filling out the register.html form. 
                - allows users who are members to log in, by having them fill in their username and password in the nav area and clicking login button. 

Add recipe - allows users who want to share recipes to add one to the website content, by clicking add recipe and filling out the form on add_recipe.html or add_recipe_loggedin.html.

Edit recipe - allows user who are logged in to edit any of the recipes they have added, by clicking the edit button on the userhome.html page and adding any changes to the fields for current data. 

Remove recipe - allows users who have previously added a recipe to remove a recipe, by clicking the remove button on the userhome.html page for the recipe they want to delete. 

Favourite Recipe - allows members to save recipes created by others to view later, by clicking the 'Add to favourites' button on the recipe_loggedin.html page for that specific recipe. 
Remove Favourite - allows members who have previously saved a recipe to favourites to remove it from the list, by either clicking remove favourite on the userhome.html page or on the recipe_loggedin.html page. 


### Features Left to Implement
Comment/review section for each recipe - this will boost engagement between users. Could also add a rating system to each recipe. 

Internal contact system where users can message each other about recipes and share ideas as well as contacting the site admins.

Add Image/Video files when adding recipes to provide instruction or show what it should look like. 

Recommended recipes based off members previous searches/ a user rating system. 

Adding preparation time to the recipe information. 

## Technologies Used
In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

### JQuery
The project uses JQuery to simplify DOM manipulation.
[JQUERY](https://jquery.com/)

### Materialize JS and CSS 
The project uses materialize to aid content development
[Materialize](http://materializecss.com/)

### Flask
The project uses the flask micro framework to provide background functionality and routing
[Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))

### Flask PyMongo
The project uses Flask.pymongo to allow flask to interact with the database collection.
[Flask Pymongo](https://flask-pymongo.readthedocs.io/en/latest/)

### Werkzeug
The project uses Werkzeug.security to provide hash and salt for password security 
[Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/utils/)

### BSON
The project uses BSON to interact with cursor ID objects.
[BSON](https://docs.mongodb.com/manual/reference/method/ObjectId/)

### MongoDB
The project uses MongoDB to store user information and recipe information.
[MongoDB](https://cloud.mongodb.com/)

## Testing
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.



You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

## Credits
## Content
The text for section Y was copied from the Wikipedia article Z
## Media
The photos used in this site were obtained from ...
## Acknowledgements
I received inspiration for this project from X



