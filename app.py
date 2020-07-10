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
    name = request.form.get("recipe_name")
    added_by = request.form.get("added_by")
    ingredients = {request.form.get("ingredients_name"), request.form.get("ingredients_quantity")}
    method = request.form.get("method")
    difficulty = request.form.get("difficulty")
    cooking_time = request.form.get("cooking_time")
    recipe = request.form.to_dict()
    print(recipe)
    return render_template('recipe.html', recipes=recipe)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
