import requests 
from bs4 import BeautifulSoup

url = "https://newsapi.org/"

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

print(soup.prettify())

