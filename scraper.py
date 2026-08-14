import requests

URL = "https://www.cvbankas.lt/?keyw=devops&location%5B%5D=606"
response = requests.get(URL)

print(response.status_code)
print(len(response.text))

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")
listings = soup.find_all("a", class_="list_a")

for listing in listings:
    title = listing.find("h3", class_="list_h3")
    print(title.text.strip(), "->", listing["href"])
