import requests
from bs4 import BeautifulSoup

def fetch_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    print(response) 
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    data = []
    
    for quote, author in zip(quotes, authors):
        data.append({
            "quote": quote.text,
            "author": author.text
        });
        
    return data

fetch_quotes()