from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
books = soup.find_all("article", {"class": "product_pod"})

# print(books)
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", {"class": "price_color"}).text
    print(f"{title} - {price}")