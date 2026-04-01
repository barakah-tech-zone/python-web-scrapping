import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://books.toscrape.com/"

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price"])

    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            writer.writerow([title, price])

        # Find next page
        next_btn = soup.find("li", class_="next")
        if next_btn:
            next_url = next_btn.a["href"]
            url = urljoin(url, next_url)
        else:
            url = None

print("Done")