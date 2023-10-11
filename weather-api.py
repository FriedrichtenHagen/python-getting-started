import requests
from pprint import pprint
# time zone munich: 48.1351° N, 11.5820° E
latitude = 48.13
longitude = 11.58

url = f'https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date=2023-09-22&end_date=2023-10-06&daily=temperature_2m_mean,precipitation_sum&timezone=GMT'

response = requests.get(url).json()

pprint(response)