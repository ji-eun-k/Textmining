import konlpy
from konlpy.tag import Kkma
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys
import pandas as pd
import math

query_txt = input('검색하고 싶은 키워드는 무엇인가요? : ')
f_name = "output.txt"

path = ".\\chromedriver\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.naver.com/")

element = driver.find_element_by_id('query')
element.send_keys(query_txt)

driver.find_element_by_id('search_btn').click()

driver.find_element_by_class_name('lnb3').click()


hi = Kkma()
doc = konlpy.corpus.kolaw.open('constitution.txt').read()
nouns = hi.nouns(doc)
print(nouns)
