##### Import Web Scraping tools and dependencies #####

# Import Splinter, BeautifulSoup, and Pandas.
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

# Intialize browser, create data dictionary, end WebDriver, and return scraped data.
def scrape_all()
    # Initiate headless driver for deployment.
    browser = Browser("chrome", executable_path="chromedriver", headless=True)

    # Run all scraping functions and store results in dictionary.
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }
# Ends automated browser from running.
browser.quit()
return data

##### Initialize web scraping with automated browser #####

# Set the executable path and initialize automated Chrome browser(Mac OS).
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

def mars_news(browser)
    # Instruct autoVisit to the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Optional delay for loading the page.
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Parse html data.
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    
    # Add try/except for error handling.
    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')

        # Look for specific data within "slide" as parent element.
        slide_elem.find("div", class_='content_title')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find("div", class_='content_title').get_text()
        news_title

        # Use the parent element to find the paragraph text.
        # Output is the summary of the article.
        news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
        news_p

    except AttributeError:
        return None, None    

    # Complete function with return statement.
    return news_title, news_p


#### Scrape Mars Data: Featured Images ####
def featured_image(brower)

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

# Add try/except for error handling
    try:
        # Find the relative image url
        # Note: when NASA updates its image page, the code will still
        # pull the most recent image. This pulls the image from where
        # it will be.
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")
        img_url_rel
    
    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    img_url

    return img_url

### Scrape Mars Data: Mars Facts ####
def mars_facts()
    # Add try/except for error handling.
    try:
        # Used 'read_html' to scrape the facts table and display into a dataframe. 
        df = pd.read_html('http://space-facts.com/mars/')[0]
    except BaseException:
        return None

# Assign columns and set index of dataframe.
df.columns=['description', 'Mars']
df.set_index('description', inplace=True)
df

# Convert DataFrame back to html-ready code.
return df.to_html(classes="table table-striped")

# Print scraped data.
if __name__ == "__main__":
    # If running as script, print scraped data.
    print(scrape_all())