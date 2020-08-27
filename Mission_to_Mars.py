##### Import Web Scraping tools and dependencies ####

# Import Splinter and BeautifulSoup.
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

##### Initialize web scraping with automated browse

# Set the executable path and initialize automated Chrome browser(Mac OS).
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

# Instruct autoVisit to the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# Parse html data.
html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')

# Look for specific data for a particular 
slide_elem.find("div", class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text.
# Output is the summary of the article.
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


#### Scrape Mars Data: Featured Images ####

# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()

# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')

# Find the relative image url
# Note: when NASA updates its image page, the code will still
# pull the most recent image. This pulls the image from where
# it will be.
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url

# Display web table in DataFrame. 
df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df

# Convert DataFrame back to html-ready code.
df.to_html()

# Ends automated browser from running.
browser.quit()