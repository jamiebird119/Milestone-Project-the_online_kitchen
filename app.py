import os
from os import path
from flask import Flask, render_template, \
                  request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if path.exists('env.py'):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("secret_key")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    if "username" in session:
        username = session["username"]
        user = mongo.db.users.find_one(
            {"username": username})
        print(username)
        if "favourites" in user:
            favourites = []
            for item in user["favourites"]:
                recipe = mongo.db.recipes.find_one({"_id": item})
                favourites.append([recipe["recipe_name"],
                                   recipe["_id"]])
            return render_template('index.html', user=user,
                                   recipes=mongo.db.recipes.find({
                                       "added_by": username}),
                                   favourites=favourites,
                                   featured_list=mongo.db.recipes.find().limit(4))
        else:
            return render_template('index.html', user=user,
                                   recipes=mongo.db.recipes.find({
                                       "added_by": username}),
                                   featured_list=mongo.db.recipes.find().limit(4))
    else:
        return render_template("index.html",
                               featured_list=mongo.db.recipes.find().limit(4))


@app.route("/home_message/<message>")
def home_message(message):
    if "username" in session:
        user = mongo.db.users.find_one(
            {"username": session["username"]})
        if "favourites" in user:
            favourites_list = []
            for item in user["favourites"]:
                recipe = mongo.db.recipes.find_one({"_id": item})
                favourites_list.append([recipe["recipe_name"],
                                        recipe["_id"]])
            return render_template("index.html", user=user,
                                   recipes=mongo.db.recipes.find({
                                       "added_by": session["username"]}),
                                   favourites=favourites_list,
                                   message=message,
                                   featured_list=mongo.db.recipes.find().limit(4))
    else:
        return render_template("index.html",
                               message=message,
                               featured_list=mongo.db.recipes.find().limit(4))


@app.route("/addrecipe")
def addrecipe():
    return render_template("add_recipe.html")


@app.route("/insert_recipe/", methods=["POST"])
def insert_recipe():
    try:
        recipes = mongo.db.recipes
        name = request.form.get("recipe_name")
        ingredients = zip(request.form.getlist("ingredient"),
                          request.form.getlist("ingredient_quantity"))
        method = request.form.get("method").splitlines()
        difficulty = request.form.get("difficulty")
        cooking_time = request.form.get("cooking_time")
        if "username" in session:
            added_by = session["username"]
            recipe_details = {"recipe_name": name,
                              "added_by": added_by.lower(),
                              "method": method,
                              "ingredients": list(ingredients),
                              "difficulty": difficulty.capitalize(),
                              "cooking_time": cooking_time}
            recipes.insert_one(recipe_details)
            return render_template('recipe.html',
                                   recipe=recipe_details,
                                   user=mongo.db.users.find_one({
                                       "username": session["username"]}),
                                   message='Recipe Successfully Added')
        else:
            added_by = request.form.get("added_by")
            recipe_details = {"recipe_name": name,
                              "added_by": added_by.lower(),
                              "method": method,
                              "ingredients": list(ingredients),
                              "difficulty": difficulty.capitalize(),
                              "cooking_time": cooking_time}
            recipes.insert_one(recipe_details)
            return render_template('recipe.html',
                                   recipe=recipe_details,
                                   message='Recipe Successfully Added')
    except Exception as e:
        alert = "Error found:" + str(e)
        return render_template('recipe.html', error=alert)


@ app.route("/get_recipe/<recipe_id>")
def get_recipe(recipe_id):
    if "username" in session:
        recipe = mongo.db.recipes.find_one(
            {"_id": ObjectId(recipe_id)})
        return render_template('recipe.html',
                               recipe=recipe,
                               user=mongo.db.users.find_one({
                                   "username": session["username"]}))
    else:
        recipe = mongo.db.recipes.find_one(
            {"_id": ObjectId(recipe_id)})
        return render_template('recipe.html',
                               recipe=recipe,)


@ app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    return render_template("edit_recipe.html",
                           recipe=mongo.db.recipes.find_one({
                               "_id": ObjectId(recipe_id)}))


@ app.route("/remove_recipe/<recipe_id>", methods=["POST"])
def remove_recipe(recipe_id):
    try:
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        msg = "Recipe Deleted"
        # remove selected recipe from all user favourites
        mongo.db.users.update_many({"favourites": recipe_id},
                                   {'$pull': {"favourites": [recipe_id]}})
        return url_for('home_message',
                       message=msg)
    except Exception as e:
        error_message = "Error found:" + str(e)
        return url_for('home_message',
                       message=error_message)


@ app.route('/register')
def register():
    return render_template("register.html", alert='')


@ app.route('/login', methods=["POST"])
def login():
    try:
        user = mongo.db.users
        user_login = {"username": request.form.get('username')}
        username = request.form.get('username').lower()
        user_details = user.find_one(user_login)
        if user_details is None:
            alert = "Username or password not recognised. Please try again."
            return render_template('index.html',
                                   alert=alert)
        # check password against hash
        else:
            password_check = check_password_hash(
                user_details["hashed_password"],
                request.form.get('password').lower())
            if password_check:
                session["username"] = username
                user = mongo.db.users.find_one({"username": username})
                if user["favourites"]:
                    favourites = []
                    for item in user["favourites"]:
                        recipe = mongo.db.recipes.find_one({"_id": item})
                        favourites.append(
                            [recipe["recipe_name"], recipe["_id"]])
                        return render_template('index.html',
                                               user=mongo.db.users.find_one(
                                                   {"username": username}),
                                               recipes=mongo.db.recipes.find({
                                                   "added_by": username}),
                                               favourites=favourites,
                                               featured_list=mongo.db.recipes.find().limit(4))
                else:
                    return render_template('index.html', user=user,
                                           recipes=mongo.db.recipes.find({
                                               "added_by": username}),
                                           featured_list=mongo.db.recipes.find().limit(4))
            else:
                alert = "Username or password not recognised. Please try again."
                return render_template('index.html',
                                       alert=alert)
    except Exception as e:
        alert = "Error found:" + str(e)
        return render_template('index.html', alert=alert)


@ app.route('/add_favourite/<recipe_id>', methods=["POST"])
def add_favourite(recipe_id):
    username = session["username"]
    # ------------------------------------------------ TEST CODE IN HERE
    # -
    mongo.db.users.find_one_and_update(
        {"username": username.lower()},
        {"$push": {"favourites":  ObjectId(recipe_id)}})
    user = mongo.db.users.find_one({"username": username})
    if "favourites" in user:
        favourites = []
        for item in user["favourites"]:
            recipe = mongo.db.recipes.find_one({"_id": item})
            favourites.append([recipe["recipe_name"],
                               recipe["_id"]])
            return render_template('index.html', user=user,
                                   recipes=mongo.db.recipes.find({
                                       "added_by": username}),
                                   favourites=favourites,
                                   featured_list=mongo.db.recipes.find().limit(4))
    else:
        return render_template('index.html', user=user,
                               recipes=mongo.db.recipes.find({
                                   "added_by": username}),
                               featured_list=mongo.db.recipes.find().limit(4))


@ app.route('/remove_favourite/<recipe_id>', methods=["POST"])
def remove_favourite(recipe_id):
    mongo.db.users.find_one_and_update(
        {"username": session["username"].lower()},
        {"$pull": {"favourites": ObjectId(recipe_id)}})
    return url_for('home_message',
                   message="Recipe removed from favourites")


@ app.route('/adduser', methods=["POST"])
def adduser():
    user = mongo.db.users
    username = request.form.get("username").lower()
    if not user.find_one({"username": username}):
        password = request.form.get("password")
        session["username"] = request.form.get("username").lower()
        details = {"username": username,
                   "hashed_password": generate_password_hash(password.lower()),
                   "first_name": request.form.get("first_name").lower(),
                   "last_name": request.form.get("last_name").lower(),
                   "favourites": []}
        user.insert_one(details)
        return render_template("index.html",
                               user=details,
                               recipes=mongo.db.recipes.find({
                                   "added_by": username}),
                               featured_list=mongo.db.recipes.find().limit(4))
    else:
        exists = "Username already exists. Log in or use another username."
        return render_template('register.html',
                               alert=exists)


@ app.route('/logout')
def logout():
    session.clear()
    return render_template("index.html",
                           featured_list=mongo.db.recipes.find().limit(10))


@ app.route("/updaterecipe/<recipe_id>", methods=["POST"])
def updaterecipe(recipe_id):
    try:
        recipes = mongo.db.recipes
        name = request.form.get("recipe_name")
        added_by = session["username"]
        ingredients = zip(request.form.getlist("ingredient"),
                          request.form.getlist("ingredient_quantity"))
        method = request.form.get("method").splitlines('\r')
        difficulty = request.form.get("difficulty")
        cooking_time = request.form.get("cooking_time")
        recipes.update_one({"_id": ObjectId(recipe_id)},
                           {"$set": {"recipe_name": name,
                                     "added_by": added_by.lower(),
                                     "method": method,
                                     "ingredients": list(ingredients),
                                     "difficulty": difficulty,
                                     "cooking_time": cooking_time}})
        msg = "Recipe successfully updated"
        return render_template('recipe_loggedin.html',
                               recipe=mongo.db.recipes.find_one(
                                   {"_id": ObjectId(recipe_id)}),
                               user=mongo.db.users.find_one({
                                   "username": session["username"]}),
                               message=msg)
    except Exception as e:
        alert = "Error found:" + str(e)
        return render_template('recipe_loggedin.html',
                               recipe=mongo.db.recipes.find_one(
                                   {"_id": ObjectId(id)}),
                               user=mongo.db.users.find_one({
                                   "username": session["username"]}),
                               error=alert)


@ app.route("/search", methods=["POST"])
def search():

    variable = request.form.get("variable")
    search_content = request.form.get("search").lower()
    if variable == "recipe_name":
        search_return = mongo.db.recipes.find(
            {"$text": {"$search": search_content}})
    else:
        search_return = mongo.db.recipes.find({variable: search_content})
    if "username" in session:
        return render_template("index.html",
                               recipes=mongo.db.recipes.find(
                                   {"added_by": session["username"]}),
                               search_content=search_return,
                               user=mongo.db.users.find_one({
                                   "username": session["username"]}),
                               featured_list=mongo.db.recipes.find().limit(4))
    else:
        return render_template("index.html",
                               search_content=search_return,
                               featured_list=mongo.db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
