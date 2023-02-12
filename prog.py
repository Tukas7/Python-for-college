import requests
from bs4 import BeautifulSoup as BS
r= requests.get("https://www.sova72.ru/kupit/kvartira/4-i-bolee-komnatnaya")
soup = BS(r.content, 'html.parser')
site=[]
ref =[]
for link in soup.find_all('a'):
    site.append(link.get("href"))


try:
    for href in site:
        if href[0] == ('h'):
            ref.append(href)

        if href[0] == ("/"):
            new=(str("https://www.sova72.ru") + href)
            ref.append(new)
except:
    pass
word = ["Квартира","квартира"]
full=[]
top = []
big=[]
for i in ref:
    join = requests.get(i)
    last = BS(join.text, 'lxml')
    big = last.find_all('p')
    big = big.split()
    for o in big:
        for g in word:
            if o == g:
                full.append(i)
    print(full)



