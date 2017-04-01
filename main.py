# coding = utf-8
from bs4 import BeautifulSoup
from fetchPage import fetch

init_html_link = 'http://www.mzitu.com/all'
html_link = 'http://www.mzitu.com/page'
html_doc = fetch('http://www.mzitu.com/all')
soup = BeautifulSoup(html_doc, "lxml")

max_pageNumber = soup.find_all(class_='page-numbers')[5].text
