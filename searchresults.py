import requests 
import bs4

# This is what your program does:

# Gets search keywords from the command line arguments
print('Please enter your search term.')
input = input()
# Retrieves the search results page
res = requests.get(f'https://pypi.org/search/?q={input}&o=')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

for link in soup.select('.package-snippet__name'):
    print(link.getText())

# Opens a browser tab for each result
# This means your code will need to do the following:
# Read the command line arguments from sys.argv.
# Fetch the search result page with the requests module.
# Find the links to each search result.
# Call the webbrowser.open() function to open the web browser.
# Open a new file editor tab and save it as searchpypi.py.

