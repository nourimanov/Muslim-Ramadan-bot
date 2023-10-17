import httpx
from bs4 import BeautifulSoup

response = httpx.get('https://timesprayer.com/en/prayer-times-in-tashkent-m15j1t0.html')
response2 = httpx.get('https://timesprayer.com/en/prayer-times-in-xiva-m15j1t0.html')
response3 = httpx.get('https://timesprayer.com/en/prayer-times-in-samarkand-m15j1t0.html')
response4 = httpx.get('https://timesprayer.com/en/prayer-times-in-bukhara-m15j1t0.html')
response5 = httpx.get('https://timesprayer.com/en/prayer-times-in-%D8%A3%D9%86%D8%AF%D9%8A%D8%AC%D8%A7%D9%86-m15j1t0.html')


toshkent = []
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {"class": "ptTable"})
for i, v in enumerate(table.find_all('td'), 1):
    if not i & 1:
        toshkent.append(v.text)


xorazm = []
soup = BeautifulSoup(response2.text, 'html.parser')
table = soup.find('table', {"class": "ptTable"})
for i, v in enumerate(table.find_all('td'), 1):
    if not i & 1:
        xorazm.append(v.text)


samarqand = []
soup = BeautifulSoup(response3.text, 'html.parser')
table = soup.find('table', {"class": "ptTable"})
for i, v in enumerate(table.find_all('td'), 1):
    if not i & 1:
        samarqand.append(v.text)


buxoro = []
soup = BeautifulSoup(response4.text, 'html.parser')
table = soup.find('table', {"class": "ptTable"})
for i, v in enumerate(table.find_all('td'), 1):
    if not i & 1:
        buxoro.append(v.text)


andijon = []
soup = BeautifulSoup(response5.text, 'html.parser')
table = soup.find('table', {"class": "ptTable"})
for i, v in enumerate(table.find_all('td'), 1):
    if not i & 1:
        andijon.append(v.text)

