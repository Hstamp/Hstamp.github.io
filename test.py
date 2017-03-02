# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

html = open("eu_brexit_speech_corbin_2017.html")

soup = BeautifulSoup(html, "lxml")
text = soup.body.get_text("")


with open("strip_brexit_speech.txt", "w") as f:
    f.write(text.encode('utf-8'))
