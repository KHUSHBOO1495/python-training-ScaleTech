import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

print(len(books))

# book = books[0]
# print(book)

# title = book.find("h3").find("a").get("title")
# price = book.find("p", class_="price_color").text.strip()

# print(title)
# print(price)

books_data = []
for book in books:
    title = book.find("h3").find("a").get("title")
    price = book.find("p", class_="price_color").text.strip()
    avail = book.find("p", class_="availability").text.strip()
    link = book.find("h3").find("a").get("href")

    book_data = {
        "title": title,
        "price": price,
        "availability": avail,
        "url" : link
    }
    books_data.append(book_data)

print(books_data)