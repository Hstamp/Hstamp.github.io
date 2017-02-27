# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

html = open("eu_brexit_speech_corbin_2017.html")

soup = BeautifulSoup(html)
text = soup.body.get_text("")


print(text.encode('ascii', 'ignore'))
