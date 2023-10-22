import requests 
import bs4
import csv

# add second list for female names


# Retrieves the search results page
res = requests.get('https://de.wikipedia.org/wiki/Friedrich')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
name_list = soup.find('div', class_='column-multiple').find('ul')

griedrich_names = []
for li in name_list.find_all('li'):
    # split language and names on the semicolon :
    name_parts = li.get_text().split(':')[1:]
    names = name_parts[0].split(',')
    for name in names: 
        cleaned_name = name.strip().replace('\nDiminutiv', '').replace('\nAltgermanisch', '')
        # case 1: Name starts with 'Fr': Friedo -> Griedo
        variant_name = cleaned_name[:]
        if(variant_name[0] == 'F' and variant_name[1] == 'r'):
            griedrich_name = variant_name.replace('F', 'G')
        # case 2: Name starts with 'R': Rico -> Grico
        elif(variant_name[0] == 'R'):
            griedrich_name = variant_name.replace('R', 'G')
        griedrich_names.append([cleaned_name, griedrich_name])
print(griedrich_names)


# Specify the CSV file path
csv_file = 'first_names.csv'

# Open the CSV file for writing
with open(csv_file, 'w', newline='') as file:
    # Define the CSV writer
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['original', 'griedrich'])

    # Write the data
    for item in griedrich_names:
        writer.writerow(item)


