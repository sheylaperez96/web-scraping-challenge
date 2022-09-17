# Unit 12 Homework: Mission to Mars

## Part 1: Scraping

In this part, I used [Jupyter Notebook](/Mission_to_Mars/mission_to_mars.ipynb) to scrape the following websites:
- [Nasa Mars News](https://redplanetscience.com/)
- [JPL Mars Space Images—Featured Image](https://spaceimages-mars.com/)
- [Mars Facts](https://galaxyfacts-mars.com/)
- [Mars Hemispheres](https://marshemispheres.com/)

 One of the results was saved in the following [html table](/Mission_to_Mars/table.html). The other results were saved as different variables.

## Part 2: MongoDB and Flask Application

In this part, I used MongoDB with Flask to create a new HTML page that displays all of the information that was scraped from the URLs above.

Materials:
- [Scrape_mars.py](/Mission_to_Mars/scrape_mars.py) is the python version of the jupyter notebook code, which uses a function called scrape.
- [app.py](/Mission_to_Mars/app.py) runs the flask app. This stores all of the scraped values into Mongo DB as a dictionary and also passes the data into an [HTML template](/Mission_to_Mars/templates/index.html). 


