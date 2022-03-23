import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('/Users/omarjandali/Desktop/chromedriver')

# setup the web driver that will run the browser
driver = webdriver.Chrome(service=s)

# set the url that is going to be scraped
driver.get('https://en.wikipedia.org/wiki/John_D._Rockefeller')

# set the object that is going to be storing the data
results = []

# add the page source that is gonig to be scraped
content = driver.page_source

# soup is going to be parsing the data
soup = BeautifulSoup(content, features="lxml")

# start looping through the data that was scalped
for element in soup.findAll(attrs={'class': 'mw-headline'}):
  sectionHeading = element.string
  results.append(sectionHeading)

for x in results:
   print(x)

df = pd.DataFrame({'Names': results})
df.to_csv('Headings.csv', index=False, encoding='utf-8')