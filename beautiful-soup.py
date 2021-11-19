import requests
import pandas as pd
from bs4 import BeautifulSoup

html = requests.get(
    "https://www.updateurself.com/2018/11/14/the-way-to-challenge/").text
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify)
