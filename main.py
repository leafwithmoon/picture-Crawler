# coding = utf-8
from bs4 import BeautifulSoup
from fetchPage import fetch

init_html_link = 'http://www.mzitu.com/all'
html_link = 'http://www.mzitu.com/page'

html_doc = fetch(init_html_link)
soup = BeautifulSoup(html_doc, "lxml")

max_pageNumber = int(soup.find_all(class_='page-numbers')[5].text)

# for pageNumber in range(1, max_pageNumber):
#     html_doc = fetch(html_link + pageNumber)
#     soup = BeautifulSoup(html_doc, "lxml")

html_doc = fetch(html_link + "2")
soup = BeautifulSoup(html_doc, "lxml")
print soup.prettify()