# Import dependencies
from flask import Flask, render_template, redirect
import pymongo
import scrape_mars
import bson.json_util as json_util

# Set up Flask App
app = Flask(__name__)

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017')

# Create / route
@app.route('/')
def index():
    # after redirecting, it will access info from the database
    db = client.mars
    mars_data = db.mars_data.find_one()
    return render_template("index.html", mars = mars_data)

@app.route('/scrape')
def scrape():
    # creating a database called Mars 
    db = client.mars
    # call the scrape function in our scrape_mars fil
    marsData = scrape_mars.scrape()
    # drop if exists
    db.mars_data.delete_many({})
    
    # Update 
    db.mars_data.insert_one(marsData)

    # Return to the index route
    return redirect("/")


# Flask app
if __name__ == "__main__":
    app.run(debug=True)
