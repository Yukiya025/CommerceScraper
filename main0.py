from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd
import webbrowser
import warnings
warnings.filterwarnings('ignore')

def openff():
    # This def open firefox browser.
    url = "https://www.oreilly.co.jp/books/9784873118574/"
    browser = webbrowser.get('"/usr/bin/firefox" %s')
    browser.open(url)

def getpret():
    csv_oreilly = pd.read_csv('Oreilly.csv', sep=",")

    with open('bk_info.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow(["Auth", "Date", "Pages"])

        for index, row in csv_oreilly.iterrows():
            r1 = csv_oreilly['Link'][index]
            r1 = requests.get(r1)
            r1.encoding = r1.apparent_encoding

            html_doc = r1.text
            soup = BeautifulSoup(html_doc)
            auth = soup.find(itemprop="author").text
            date = soup.find(itemprop="datePublished")["content"] # .parent.text
            pages = soup.find(itemprop = "numberOfPages").text
            writer.writerow([auth, date, pages])

def add_info():
    info1 = pd.read_csv('bk_info.csv')
    title_csv = pd.read_csv('Oreilly.csv')
    title_csv.join(info1).to_csv('out.csv', index=False)