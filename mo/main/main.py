import requests
import json

query = input("What type of news are you interested in?")
url = f"https://newsapi.org/v2/everything?q={query}tesla&from=2025-01-23&sortBy=publishedAt&apiKey=034d2f29c72a4b67a732701eb17a736e"

r = requests.get(url)
news = json.loads(r.text)
#print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print(article["content"])
    print("------------------")
    