#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import requests
from bs4 import BeautifulSoup 
from splinter import broswer
import pymongo 
import pandas as pd


# In[7]:


#Scraping Mars Website
mars_url = "https://redplanetscience.com"
browser = "google_chrome.exe"
broswer.visit(mars_url)
html = browser.html
#Titles
news_title_one = mars_url_soup.find("How NASA's Mars Helicopter Will Reach the Red Planet's Surface")
print(news_title_one)
news_title_two = mars_url_soup.find("Mars Helicopter Attached to NASA's Perseverance Rover")
print(news_title_two)
newst_title_three = mars_url_soup.find("NASA's Curiosity Keeps Rolling As Team Operates Rover From Home")
print(news_title_three)
#Paragraph (use inspect element)
paragraph_one = mars_url_soup.find
print(paragraph_one)
paragraph_two
print(parahraph_two)
paragraph_three
print(paragraph_three)


# In[ ]:


#Mars Images
mars_photo_url = "https://spaceimages-mars.com"
browser = "google_chrome.exe"
broswer.visit(mars_photo_url)
html = browser.html
soup = bs(html.parser)
#Featured Image 
featured_imagage_url = soup.find(class ="image/featured/mars2.jpg")
#Complete String
featured_image_url = "https://spaceimages-mars.com/image/news/mars2.jpg"


# In[ ]:


#Mars Facts
mars_fact_url = "https://galaxyfacts-mars.com"
read_html(https://galaxyfacts-mars.com)
df = pd.read_html(https://galaxyfacts-mars.com)
print(df[0]["Equatorial Diamter"])
print(df[0]["Polar Diamter"])
print(df[0]["Mass"])
print(df[0]["Moons"])
print(df[0]["Orbit Distance"])
print(df[0]["Orbit Period"])
print(df[0]["Surface Temperature"])
print(df[0]["First Record"])
print(df[0]["Recorded By"])


# In[ ]:


#Mars Hemisphere
hemi_url = "https://marshemispheres.com"
main_url = soup.find_all("div", class_="item")
titles=[]
hemisphere_image_urls=[]
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg": "..."},
    {"title": "Cerberus Hemisphere", "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg": "..."},
    {"title": "Schiaparelli Hemisphere", "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg": "..."},
    {"title": "Syrtis Major Hemisphere", "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg": "..."},
]

