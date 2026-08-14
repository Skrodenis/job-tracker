import requests

URL = "https://www.cvbankas.lt/?keyw=devops&location%5B%5D=606"
response = requests.get(URL)

print(response.status_code)
print(len(response.text))

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")
listings = soup.find_all("a", class_="list_a")

KEYWORDS = ["devops", "cloud", "sysadmin", "sre", "platform", "kubernetes", "administratorius"]

for listing in listings:
    title = listing.find("h3", class_="list_h3")
    title_text = title.text.strip()
    if any(keyword in title_text.lower() for keyword in KEYWORDS):
        print(title_text, "->", listing["href"])
