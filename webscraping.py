import requests 
from bs4 import BeautifulSoup as bs 

# load the projectpro webpage content 
r = requests.get('https://www.advertace.de') 

# convert to beautiful soup 
soup = bs(r.content) 

# scrapping the links:- 
# For all the 'href' links 

web_links = soup.select('a') 

actual_web_links = [web_link['href'] for web_link in web_links] 

print(soup.title.string) 