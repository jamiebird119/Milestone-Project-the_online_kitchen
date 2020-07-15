import os
from os import path
from flask import Flask, render_template, redirect, request, url_for, session
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
    return render_template("index.html")


@app.route("/addrecipe")
def addrecipe():
    return render_template("add_recipe.html")


@app.route("/insert_recipe/", methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    name = request.form.get("recipe_name")
    added_by = request.form.get("added_by")
    ingredients = zip(request.form.getlist("ingredient"),
                      request.form.getlist("ingredient_quantity"))
    method = request.form.get("method")
    difficulty = request.form.get("difficulty")
    cooking_time = request.form.get("cooking_time")
    recipe = {"recipe_name": name, "added_by": added_by.lower(),
              "method": method,
              "ingredients": list(ingredients),
              "difficulty": difficulty,
              "cooking_time": cooking_time}
    # recipes.insert_one(recipe)
    return render_template('recipe.html', recipe=recipe, user=mongo.db.users.find_one({"username": session["username"]}))


@app.route("/insertuser_recipe/", methods=["POST"])
def insertuser_recipe():
    recipes = mongo.db.recipes
    name = request.form.get("recipe_name")
    added_by = request.form.get("added_by")
    ingredients = zip(request.form.getlist("ingredient"),
                      request.form.getlist("ingredient_quantity"))
    method = request.form.get("method")
    difficulty = request.form.get("difficulty")
    cooking_time = request.form.get("cooking_time")
    recipe = {"recipe_name": name, "added_by": added_by.lower(),
              "method": method,
              "ingredients": list(ingredients),
              "difficulty": difficulty,
              "cooking_time": cooking_time}
    # recipes.insert_one(recipe)
    return render_template('recipe_loggedin.html', recipe=recipe, user=mongo.db.users.find_one({"username": session["username"]}))


@app.route('/register')
def register():
    return render_template("register.html", alert='')


@app.route('/login', methods=["POST"])
def login():
    user = mongo.db.users
    user_login = {"username": request.form.get('username')}
    username = request.form.get('username').lower()
    user_details = user.find_one(user_login)
    password_check = check_password_hash(
        user_details["hashed_password"], request.form.get('password').lower())
    if password_check:
        session["username"] = request.form.get("username")
        return render_template('userhome.html',
                               user=user_details,
                               recipes=mongo.db.recipes.find(
                                   {"added_by": username}),
                               username=session["username"])
    else:
        return render_template('index.html',
                               alert="Username or password not recognised. Please try again.")


@app.route('/add_favourite/<recipe_name>', methods=["POST"])
def add_favourite(recipe_name):
    username = session["username"]
    user = mongo.db.users.find_one({"username": username})
    if "favourites" not in user:
        mongo.db.users.update({"username": username}, {
            "$set": {"favourites": recipe_name}})
        return render_template('userhome.html',
                               user=user,
                               recipes=mongo.db.recipes.find(
                                   {"added_by": username}),
                               username=session["username"])
    else:
        favourites = user["favourites"]
        favourites.append(recipe_name.lower())
        mongo.db.users.update_one({"username": username}, {
            "$set": {"favourites": favourites}})
    return render_template('userhome.html',
                           user=user,
                           recipes=mongo.db.recipes.find(
                               {"added_by": username}),
                           username=session["username"])


@app.route('/remove_favourite/<recipe_name>', methods=["POST"])
def remove_favourite(recipe_name):
    user = mongo.db.users.find_one({"username": session["username"]})
    favourites = user["favourites"]
    favourites.remove(recipe_name.lower())
    mongo.db.users.update_one({"username": session["username"]}, {
                              "$set": {"favourites": favourites}})
    return render_template('userhome.html',
                           user=user,
                           recipes=mongo.db.recipes.find(
                               {"added_by": session["username"]}),
                           username=session["username"])


@app.route('/adduser', methods=["POST"])
def adduser():
    user = mongo.db.users
    username = request.form.get("username").lower()
    print(mongo.db.recipes.find({"added_by": username}))
    if not user.find_one({"username": username}):
        password = request.form.get("password")
        session["username"] = request.form.get("username")
        details = {"username": username,
                   "hashed_password": generate_password_hash(password.lower()),
                   "first_name": request.form.get("first_name").lower(),
                   "last_name": request.form.get("last_name").lower()}
        user.insert_one(details)
        return render_template("userhome.html",
                               user=details,
                               recipes=mongo.db.recipes.find({
                                   "added_by": username}))
    else:
        exists = "Username already exists. Log in or use another username."
        return render_template('register.html',
                               alert=exists)


@app.route('/logout')
def logout():
    session.clear()
    return render_template("index.html")


@app.route('/userhome/<username>')
def userhome(username):
    return render_template("userhome.html",
                           user=mongo.db.users.find_one(
                               {"username": username}),
                           recipes=mongo.db.recipes.find({
                               "added_by": username}))


@app.route('/adduserrecipe')
def adduserrecipe():
    return render_template("add_recipe_loggedin.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
