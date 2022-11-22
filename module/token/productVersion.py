import requests
from bs4 import BeautifulSoup
import re


def ProductVarsion() -> str:
    url = "https://www.nintendo.co.jp/support/app/nintendo_switch_online_app/index.html"
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, features="lxml")
    elements = soup.find_all("h3")
    for i in range(len(elements)):
        text = elements[i].get_text()
        regex = re.search(r"Ver. \d.\d.\d", text)
        if regex:
            return regex.group().replace("Ver. ", "")
