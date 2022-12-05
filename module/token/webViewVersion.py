import requests
from bs4 import BeautifulSoup
import re
from urllib import request


def WebViewViersion() -> str:
    url = "https://www.nintendo.co.jp/support/switch/software_support/av5ja/index.html"
    response = requests.get(url=url)
    regex = re.search(r"\d*.html", response.text).group()
    redirectUrl = (
        f"https://www.nintendo.co.jp/support/switch/software_support/av5ja/{regex}"
    )
    response = requests.get(url=redirectUrl)
    soup = BeautifulSoup(response.text, features="lxml")
    elements = soup.find_all("p")
    for i in range(len(elements)):
        text = elements[i].get_text()
        regex = re.search(r"Ver. \d.\d.\d", text)
        if regex:
            return regex.group().replace("Ver. ", "")
