from bs4 import BeautifulSoup
import requests
import re
import csv
from main0 import getpret, add_info
import warnings
warnings.filterwarnings('ignore')
r = requests.get("https://www.oreilly.co.jp/catalog/")
r.encoding = r.apparent_encoding

html_doc = r.text
soup = BeautifulSoup(html_doc)
std_lnk = "https://www.oreilly.co.jp/"

f1 = open('r.html', 'w')
f1.write(html_doc)

with open('Oreilly.csv', 'w+',newline='',encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["No","Title","Link"])
    n = 1
    for link in soup.find_all('a', {'href': re.compile(r'/books/\d')}):
        title = link.get_text()
        strip_l = link.get('href')
        strip_l = strip_l.lstrip("../")
        h_link = std_lnk + strip_l
        writer.writerow([n, title, h_link])
        n += 1

getpret()
add_info()