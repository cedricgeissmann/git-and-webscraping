from bs4 import BeautifulSoup
from requests import get
from random import choice
import wget

url = "https://xkcd.com/archive/"
res = get(url)

soup = BeautifulSoup(res.content, "html.parser")

hrefs = [elem['href'] for elem in soup.select(r"a[title]")]

for num in hrefs[0:10]:

    url = f"https://xkcd.com/{num}/"
    res = get(url)

    soup = BeautifulSoup(res.content, "html.parser")
    img = soup.select("div#comic > img")[0]
    wget.download(f"https:{img['src']}", out="img/")