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
    return render_template("index.html",
                           featured_list=mongo.db.recipes.find().limit(5))


@app.route("/addrecipe")
def addrecipe():
    return render_template("add_recipe.html")


@app.route("/insert_recipe/", methods=["POST"])
def insert_recipe():
    try:
        recipes = mongo.db.recipes
        name = request.form.get("recipe_name")
        added_by = request.form.get("added_by")
        ingredients = zip(request.form.getlist("ingredient"),
                          request.form.getlist("ingredient_quantity"))
        method = request.form.get("method").splitlines()
        difficulty = request.form.get("difficulty")
        cooking_time = request.form.get("cooking_time")
        recipe = {"recipe_name": name,
                  "added_by": added_by.lower(),
                  "method": method,
                  "ingredients": list(ingredients),
                  "difficulty": difficulty,
                  "cooking_time": cooking_time}
        recipes.insert_one(recipe)
        return render_template('recipe.html',
                               recipe=recipe,
                               message='Recipe Successfully Added')
    except Exception as e:
        alert = "Error found:" + str(e)
        return render_template('recipe.html', error=alert)


@app.route("/get_recipe/<recipe_id>")
def get_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    return render_template('recipe.html',
                           recipe=recipe,
                           )


@app.route("/get_loggedinrecipe/<recipe_id>")
def get_loggedinrecipe(recipe_id):
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    return render_template('recipe_loggedin.html',
                           recipe=recipe,
                           user=mongo.db.users.find_one({
                               "username": session["username"]}))


@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    return render_template("edit_recipe_loggedin.html",
                           recipe=mongo.db.recipes.find_one({
                               "_id": ObjectId(recipe_id)}))


@app.route("/remove_recipe/<recipe_id>", methods=["POST"])
def remove_recipe(recipe_id):
    try:
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        msg = "Recipe Deleted"
        return url_for('userhomepage',
                       username=session["username"],
                       message=msg)
    except Exception as e:
        error_message = "Error found:" + str(e)
        return url_for('userhomepage',
                       username=session["username"],
                       message=error_message)


@app.route('/userhomepage/<username>/<message>')
def userhomepage(username, message):
    return render_template('userhome.html', user=mongo.db.users.find_one(
        {"username": username}),
        recipes=mongo.db.recipes.find({
            "added_by": username}),
        message=message,
        featured_list=mongo.db.recipes.find().limit(5))


@app.route("/insertuser_recipe/", methods=["POST"])
def insertuser_recipe():
    try:
        recipes = mongo.db.recipes
        name = request.form.get("recipe_name")
        ingredients = zip(request.form.getlist("ingredient"),
                          request.form.getlist("ingredient_quantity"))
        method = request.form.get("method").splitlines()
        difficulty = request.form.get("difficulty")
        cooking_time = request.form.get("cooking_time")
        recipe_details = {"recipe_name": name,
                          "added_by": session['username'],
                          "method": method,
                          "ingredients": list(ingredients),
                          "difficulty": difficulty,
                          "cooking_time": cooking_time}
        recipes.insert_one(recipe_details)
        return render_template('recipe_loggedin.html',
                               recipe=recipe_details,
                               user=mongo.db.users.find_one({
                                   "username": session["username"]}),
                               message="Recipe successfully added")
    except Exception as e:
        recipes = mongo.db.recipes
        name = request.form.get("recipe_name")
        ingredients = zip(request.form.getlist("ingredient"),
                          request.form.getlist("ingredient_quantity"))
        method = request.form.get("method").splitlines()
        difficulty = request.form.get("difficulty")
        cooking_time = request.form.get("cooking_time")
        recipe_details = {"recipe_name": name,
                          "added_by": session['username'],
                          "method": method,
                          "ingredients": list(ingredients),
                          "difficulty": difficulty,
                          "cooking_time": cooking_time}
        alert = "Error found:" + str(e)
        return render_template('recipe_loggedin.html',
                               recipe=recipe_details,
                               user=mongo.db.users.find_one({
                                   "username": session["username"]}),
                               error=alert)


@app.route('/register')
def register():
    return render_template("register.html", alert='')


@app.route('/login', methods=["POST"])
def login():
    try:
        user = mongo.db.users
        user_login = {"username": request.form.get('username')}
        username = request.form.get('username').lower()
        user_details = user.find_one(user_login)
        password_check = check_password_hash(
            user_details["hashed_password"],
            request.form.get('password').lower())
        if len(user_details) == 0:
            alert = "Username or password not recognised. Please try again."
            return render_template('index.html',
                                   alert=alert)
        else:
            if password_check:
                session["username"] = request.form.get("username")
                return render_template('userhome.html',
                                       user=user_details,
                                       recipes=mongo.db.recipes.find(
                                           {"added_by": username}),
                                       username=session["username"],
                                       featured_list=mongo.db.recipes.find().limit(5))
            else:
                alert = "Username or password not recognised. Please try again."
                return render_template('index.html',
                                       alert=alert)
    except Exception as e:
        alert = "Error found:" + str(e)
        return render_template('index.html', alert=alert)


@app.route('/add_favourite/<recipe_id>/<recipe_name>', methods=["POST"])
def add_favourite(recipe_id, recipe_name):
    username = session["username"]
    user = mongo.db.users.find_one({"username": username})
    if "favourites" not in user:
        mongo.db.users.update({"username": username}, {
            "$set": {"favourites": [[recipe_name, recipe_id]]}})
        return render_template('userhome.html',
                               user=user,
                               recipes=mongo.db.recipes.find(
                                   {"added_by": username}),
                               username=session["username"],
                               featured_list=mongo.db.recipes.find().limit(5))
    else:
        favourites = user["favourites"]
        favourites.append([recipe_name, recipe_id])
        mongo.db.users.update_one({"username": username}, {
            "$set": {"favourites": favourites}})
    return render_template('userhome.html',
                           user=user,
                           recipes=mongo.db.recipes.find(
                               {"added_by": username}),
                           username=session["username"],
                           featured_list=mongo.db.recipes.find().limit(5))


@app.route('/remove_favourite/<recipe_id>')
def remove_favourite(recipe_id):
    user = mongo.db.users.find_one({"username": session["username"]})
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    favourites = user["favourites"]
    favourites.remove([recipe["recipe_name"], recipe_id])
    mongo.db.users.update_one({"username": session["username"]}, {
                              "$set": {"favourites": favourites}})
    return render_template('userhome.html',
                           user=user,
                           recipes=mongo.db.recipes.find(
                               {"added_by": session["username"]}),
                           username=session["username"],
                           message="Recipe removed from favourites",
                           featured_list=mongo.db.recipes.find().limit(5))


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
                                   "added_by": username}),
                               featured_list=mongo.db.recipes.find().limit(5))
    else:
        exists = "Username already exists. Log in or use another username."
        return render_template('register.html',
                               alert=exists)


@app.route('/logout')
def logout():
    session.clear()
    return render_template("index.html",
                           featured_list=mongo.db.recipes.find().limit(10))


@app.route('/userhome/<username>')
def userhome(username):
    return render_template("userhome.html",
                           user=mongo.db.users.find_one(
                               {"username": username}),
                           recipes=mongo.db.recipes.find({
                               "added_by": username}),
                           featured_list=mongo.db.recipes.find().limit(5))


@app.route('/adduserrecipe')
def adduserrecipe():
    return render_template("add_recipe_loggedin.html")


@app.route("/updaterecipe/<recipe_id>", methods=["POST"])
def updaterecipe(recipe_id):
    try:
        recipes = mongo.db.recipes
        name = request.form.get("recipe_name")
        added_by = session["username"]
        ingredients = zip(request.form.getlist("ingredient"),
                          request.form.getlist("ingredient_quantity"))
        method = request.form.get("method").splitlines()
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


@app.route("/search_loggedin", methods=["POST"])
def search_loggedin():
    variable = request.form.get("variable")
    search_content = request.form.get("search").lower()
    if variable == "recipe_name":
        search_return = mongo.db.recipes.find(
            {"$text": {"$search": search_content}})
    else:
        search_return = mongo.db.recipes.find({variable: search_content})
    return render_template("userhome.html",
                           recipes=mongo.db.recipes.find(
                               {"added_by": session["username"]}),
                           search_content=search_return,
                           user=mongo.db.users.find_one({
                               "username": session["username"]}),
                           featured_list=mongo.db.recipes.find().limit(5))


@app.route("/search", methods=["POST"])
def search():
    variable = request.form.get("variable")
    search_content = request.form.get("search").lower()
    if variable == "recipe_name":
        search_return = mongo.db.recipes.find(
            {"$text": {"$search": search_content}})
    else:
        search_return = mongo.db.recipes.find({variable: search_content})
    return render_template("index.html",
                           search_content=search_return,
                           featured_list=mongo.db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
