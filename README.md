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


7. [**Media**](#media)

8. [**Acknowledgements**](#acknowledgements)


## UX

The website was mainly aimed at people who like cooking and like food and have experience with the former. However, with the addition of the difficulty rating 
for each recipe, it is hoped that it will also cater to a novice home cook as well. With an easy to use search function there are many ways to search other users content and 
to then add that content to a list of favourites, meaning a user can easily come back to it. Adding a recipe is easy and can be done by guest users and registered users alike hopefully keeping a broad 
range of content available to all. 

### Design

Balsamic IQ was used to create wireframes of different resolutions for each of the pages on the site. See the link below:  
[Wireframes](https://balsamiq.cloud/sseslm8/pk2omam)

### Theme 
Materialize was used to provide general themes on inputs buttons and other features to provide continuity and a consistent style for the site.

### Fonts
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

### Registration 
- Go to 'registration' page.
- Try to submit empty form and confirmed alert message for fields required
- Submit the form with previously used details and confirmed message saying 'Username exists already'.
- Entered unique username and password and confirmed success message and successful loading of index page with session variable. 

### Logout/Login
- Click 'logout' button and confirm removal of session variable.
- Rentered details incorrectly and confirmed error message prompting user to enter correct details
- Enter correct username and password and confirm loading of index with session username. 

### Add Recipe
- Go to 'add recipe' page confirming if user logged in then addedby field is prepopulated by session variable.
- Attempt to submit blank form and confirm required user prompt.
- Complete form and confirm success message and loading of recipe page. 

### Edit Recipe
- Go to home page and click edit button on test recipe.
- Confirm edit form correctly loading with current data in each field.
- Alter form accordingly and click submit, confirming success message and changes applied.

### Delete Recipe 
- Go to home page and click delete button next to test recipe. 
- Confirm that pop-up modal appears with query asking user if they are sure they want to delete said recipe.
- Click no to confirm closing of modal. 
- Attempt above again clicking 'yes' to confirm deletion of test recipe. 
- Confirm success message and recipe no longer appearing on user page.

### Recipe Search 
- Go to home page.
- Enter select variable of name and enter 'Eggs'.
- Confirm on clicking search that a text index search of database occurs and loads any recipe with Eggs in the title.
- Index page is reloaded with results shown. 

### Favourite Recipe
- Go to specific recipe page (in this case Eggs Benedict) from search function.
- With no session variable attempt to click 'add to favourites'. Confirm error message prompting user to log in.
- Log in and navigate to same page. 
- Click add to favourites and confirm success message. On returning to home page confirm recipe in favourites section.

### Remove Favourite
- Go to specific recipe page (again Eggs Benedict) and confirm that button now shows as remove from favourites.
- Click remove from favourites on recipe page and confirm success message.
- (re-added to favourites to test second method) Return to user home page and click 'remove' button in favourites section and confirm success message and home page reload without recipe in favourites.

### Nav Elements
- During the above testing each nav element was attempting to ensure routing successful.
- Mobile resolution was then used and the collapsible side nav was confirmed to correctly toggle on user click.
- Each nav link was then attempted to ensure correct routing. 

### Responsiveness
- The site was tested on various mobile, tablet and desktop resolutions to ensure no horizontal scrolling and correct loading of features.
- Mobile and vertical tablet views use a collapsible navbar in order to effectively utilise space.
- Advertising elements are also altered from vertical to a horizontal version when changing between desktop to tablet, with both vertical and horizontal elements being shown on tablet view due to excess space.
- Generally input fields were editted so as to be of larger width on mobile to increase readability of contents and easy user data entry. 
- The site was designed using a mobile first approach. 

### Bugs
- A bug with the method containing blank lines of whitespace was found and fixed. Instructions were also added for the user to ensure information is entered in the correct format to avoid the issue further.
- An error found when inserting a recipe when not logged in (as no session variable). Altered routing to fix. 
- Login error found when entering an incorrect username, got an exception of NoneType error. Easily fixed by altering app routing. 
- Side Nav not working originally due to incorrect loading of external libraries. Rearranged ordering and working correctly. 

## Deployment
The Project was deployed to [*Heroku*](https://the-online-cookbookjb.herokuapp.com/) using the following stages.
- A requirements.txt file was created using:
    pip3 freeze --local > requirements.txt 
- A Procfile was created using:
    echo web: puthon app.py > Procfile
- Heroku login was completed and the app was linked:
    heroku login
    heroku git : remote -a the-online-cookbookjb
- A git commit was then completed with the push to heroku. The branch was different to the origin master branch used for development.
    git commit -m "heroku deployment"
    git push heroku master
- Heroku Confi Vars were then set up on the heroku page. The values for :
    - MONGO_URI
    - MONGO_DBNAME
    - Secret key 
    - Port 
    - IP 
Were all added the same as in the developmental version. 

To run the code locally use the following command line block:
    python3 app.py

### Credits
## Media
The Photos used for advertising were found from  [Global Knives](https://globalknives.uk/)
## Acknowledgements
I received inspiration for this project from Tim and Susan



