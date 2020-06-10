from konlpy.tag import Okt
import pytagcloud
import webbrowser
from collections import Counter
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException


okt = Okt()

query_txt = input('검색하고 싶은 키워드는 무엇인가요? : ')
page_num = int(input('몇 개의 페이지를 검색하겠습니까?'))

# 검색 자동화
path = ".\\chromedriver\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=")

element = driver.find_element_by_id('nx_query')
element.send_keys(query_txt)

driver.find_element_by_class_name('bt_search').click()

title_list = []

while True:
    try:
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        driver.find_element_by_id('notfound')
        re_query = input('검색 결과가 없습니다 다시 입력해주세요')

    except NoSuchElementException:
        break

for i in range(page_num):
    try :
        time.sleep(1)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        each_title = soup.select('a._sp_each_title')
        for j in each_title:
            title_list.append(j)

        driver.find_element_by_class_name('next').click()
    except NoSuchElementException:
        break

news_tag = []

for j in title_list:
    news_tag.append(okt.pos(j.text))

news_noun_adj = []

for noun_adj in news_tag:
    for word, tag in noun_adj:
        if tag in ['Noun', 'Adjective']:
            if word == query_txt: #검색어 제외
                continue
            news_noun_adj.append(word)

counts = Counter(news_noun_adj)
news_count = counts.most_common(30)

taglist = pytagcloud.make_tags(news_count, maxsize=70)

pytagcloud.create_tag_image(taglist, 'word_noun.png', fontname='BMDOHYEON_ttf', size=(900, 600), rectangular=False)
webbrowser.open('word_noun.png')
