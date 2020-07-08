import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

MONGODB_URI = os.environ.get("MONGO_URI")
MONGO_DBNAME = os.environ.get("MONGO_DBNAME")

app.config["MONGO_DBNAME"] = MONGO_DBNAME
app.config["MONGO_URI"] = MONGODB_URI

mongo = PyMongo(app)


@app.route("/")



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
