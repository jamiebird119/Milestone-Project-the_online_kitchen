import os
from os import path
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if path.exists('env.py'):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

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
    ingredients = request.form.getlist("ingredient")
    print(ingredients)
    ingredients_quantity = request.form.getlist("ingredient_quantity")
    print(ingredients_quantity)
    method = request.form.get("method")
    difficulty = request.form.get("difficulty")
    cooking_time = request.form.get("cooking_time")
    recipe = {"recipe_name": name, "added_by": added_by,
              "method": method,
              "ingredients": ingredients,
              "ingredients_quantity": ingredients_quantity,
              "difficulty": difficulty,
              "cooking_time": cooking_time}
    return render_template('recipe.html', recipe=recipe)


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/adduser', methods=["POST"])
def adduser():
    user = mongo.db.users
    user.insert_one(request.form.to_dict())
    return render_template("loggedin.html", user=request.form.to_dict())




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
