# import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time 
import os

# creating a new function - that will scrape everything
def scrape():
    # Connecting to chrome
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False) 

    # 1 - CONNECTING TO MARS NEWS
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    time.sleep(3) 
    # creating soup object
    soup = bs(browser.html, 'html.parser') 
    # define title and paragraph
    title = soup.find("div", class_="content_title").text
    paragraph = soup.find("div", class_='article_teaser_body').text

    # 2 - CONNECTING TO FEATURED IMAGES
    url_2 = 'https://spaceimages-mars.com/'
    browser.visit(url_2)
    time.sleep(3)
    # creating soup object
    soup_2 = bs(browser.html, 'html.parser') 
    # get image url
    img_href = soup_2.find('a', class_='showimg fancybox-thumbs')['href']
    featured_image_url = f'{url_2}{img_href}'

    # 3 - IMPORTING HTML TABLE
    filePath = os.path.join('table.html')
    with open(filePath) as file:
        html = file.read()
    
    soup_4 = bs(html, 'html.parser')

    # 4 - CONNECTING TO MARS HEMISPHERES
    url_4 = 'https://marshemispheres.com/'
    browser.visit(url_4)
    # scrape the title and links
    hemispheres = ['Cerberus Hemisphere Enhanced', 'Schiaparelli Hemisphere Enhanced', 'Syrtis Major Hemisphere Enhanced',
    'Valles Marineris Hemisphere Enhanced']
    hemisphere_image_urls = []
    # Create a loop 
    for h in hemispheres:
        browser.links.find_by_partial_text(h).click() # go to each hemisphere link
        time.sleep(3) # allowing data to load
        soup_3 = bs(browser.html, 'html.parser') # creating soup object
        title = soup_3.find("h2", class_="title").text
        link = f"{url_4}{soup_3.find('li').a['href']}"
        hemisphere_info = {}
        hemisphere_info['title'] = title
        hemisphere_info['img_url'] = link
        hemisphere_image_urls.append(hemisphere_info)
        browser.back()

    # Create a dictionary with everything
    marsData = {
        'newsTitle': title,
        'newsParagraph': paragraph,
        'featuredImage': featured_image_url,
        'facts': str(soup_4),
        'hemispheres': hemisphere_image_urls
    }

    # quit session
    browser.quit()

    # display output
    return marsData

