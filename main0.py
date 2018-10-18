from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd
import webbrowser
import warnings
warnings.filterwarnings('ignore')

def geturl():
    with open('Oreilly.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row[2])
            r0 = requests.get(row[2])
            r0.encoding = r0.apparent_encoding

# geturl()

def openff():
    # This def open firefox browser.
    url = "https://www.oreilly.co.jp/books/9784873118574/"
    browser = webbrowser.get('"/usr/bin/firefox" %s')
    browser.open(url)

# openff()

def getpret():
    r1 = requests.get("https://www.oreilly.co.jp/books/9784873118574/")
    r1.encoding = r1.apparent_encoding

    html_doc = r1.text
    soup = BeautifulSoup(html_doc)
    print(soup.find(itemprop="author").text)
    print(soup.find(itemprop="datePublished"))
    print(soup.find(itemprop = "numberOfPages").text)
    # f1 = open('r1.html', 'w')
    # f1.write(html_doc)

getpret()

"""
('meta', {'itemprop'})

https://qiita.com/hideshis/items/1f556847784434cd815e
import webbrowser
url = row[2]
browser = webbrowser.get('"(chrome.exe までの絶対パス)" %s')
browser.open(url)
"""