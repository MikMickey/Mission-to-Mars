# ## Module 10 Challenge
# ### Scrape Full-Resolution Mars Hemisphere Images and Titles

# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import requests


# In[62]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[11]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[14]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[15]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[44]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[49]:


html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[53]:


images = img_soup.findAll('img')
images


# In[58]:


images1 = img_soup.select(".item")
len(images1)


# In[68]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
# 3. Write code to retrieve the image urls and titles for each hemisphere.
# 4. Print the list that holds the dictionary of each image url and title.
# hemisphere_image_urls

image_names = ['Cerberus','Schiaparelli', 'Syrtis_major','Valles_marineris']

for n in image_names:
    scrape_url = f"https://astrogeology.usgs.gov/search/map/Mars/Viking/{n}_enhanced"
    print (scrape_url)
    browser.visit(scrape_url)
    html = browser.html
    scrape_img_soup = soup(html, 'html.parser')
    img_url_rel = scrape_img_soup.select(".downloads a")[0].get('href')
    print(img_url_rel)
    title = scrape_img_soup.select("h2.title")[0].text
    print(title)
    hemisphere = {"img_url":img_url_rel, "title":title}
    hemisphere_image_urls.append(hemisphere)
    

hemisphere_image_urls
    
    


# 4. Print the list that holds the dictionary of each image url and title.



# hemisphere_image_urls

img_url_rel

# 5. Quit the browser
browser.quit()
