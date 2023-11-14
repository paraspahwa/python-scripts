# Simple web scraping script using BeautifulSoup

import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    print(f"Title of the webpage: {title}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
