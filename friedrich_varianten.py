import requests 
import bs4
# Retrieves the search results page
res = requests.get('https://de.wikipedia.org/wiki/Friedrich')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
name_list = soup.find('div', class_='column-multiple').find('ul')

first_names = []
for li in name_list.find_all('li'):
    # split language and names on the semicolon :
    name_parts = li.get_text().split(':')[1:]
    names = name_parts[0].split(',')
    for name in names: 
        first_name = name.strip().replace('\nDiminutiv', '')

        # case 1: Name starts with 'Fr': Friedo -> Griedo
        # case 2: Name starts with 'R': Rico -> Grico
        # if(first_name[0] == 'F' )
        first_names.append(first_name)

print(first_names)
