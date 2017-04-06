# coding = utf-8
from bs4 import BeautifulSoup
from fetchPage import fetch
import os

save_location = "D:\meizitu\\"
init_html_link = 'http://www.mzitu.com'
html_link = 'http://www.mzitu.com/page/'

init_html_doc = fetch(init_html_link).text
soup = BeautifulSoup(init_html_doc, "lxml")

max_pageNumber = int(soup.find_all(class_='page-numbers')[5].text)
print "Max PageNumber is {0}".format(max_pageNumber)
for pageNumber in range(1, max_pageNumber+1):
    print "In page {0}".format(pageNumber)
    html_doc = fetch(html_link + str(pageNumber)).text
    soup = BeautifulSoup(html_doc, "lxml")
    cover = soup.find_all(class_='lazy')
    for x in cover:
        cover_name = x.get('alt').replace(' ', '').replace(',', '').replace('?', '')
        if not(os._exists(save_location + cover_name)):
            print cover_name
            cover_url = x.parent.get('href')
            cover_html_doc = fetch(cover_url).text
            cover_soup = BeautifulSoup(cover_html_doc, "lxml")
            cover_max_pageNumber = int(cover_soup.find(class_='pagenavi').find_all()[-3].text)
            os.makedirs(os.path.join(save_location, cover_name))
            os.chdir(save_location + cover_name)
            for cover_pageNumber in range(1, cover_max_pageNumber):
                picture_html_doc = fetch(cover_url+'/'+str(cover_pageNumber)).text
                picture_soup = BeautifulSoup(picture_html_doc, "lxml")
                picture = picture_soup.find('img')
                picture_href = picture.get('src')
                img = fetch(picture_href)
                f = open(str(cover_pageNumber) + '.jpg', 'ab')
                f.write(img.content)
                f.close()
