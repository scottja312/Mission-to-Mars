# Import dependencies and flask.
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping

# Setup flask.
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection with Python.
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#Setup App routes.
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"

# Updating database.
.update(query_parameter, data, options)

if __name__ == "__main__":
   app.run()