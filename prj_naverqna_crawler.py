#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 18:33:50 2020

@author: Heedong Yang
@purpose:
    Bigdata Project "Utilize Closed school"
    Crawling naver qna answers for text mining
    keyword = "폐교 활용"
    총 2100 개 정도의 Q&A 존재 (210)
"""

import re
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

def crawl_question(page):
    link_list = []
    q_list = []
    for i in range(1, page+1):
        # i is current page # search term is "폐교 활용" in unicode
        s_link = f"https://kin.naver.com/search/list.nhn?query=%ED%8F%90%EA%B5%90%20%ED%99%9C%EC%9A%A9&page={i}"
        html = requests.get(s_link).content
        soup = bs(html, 'lxml')
        for i in range(1, 11):
            # i is current question number
            elem = f"#s_content > div.section > ul > li:nth-of-type({i}) > dl > dt > a"
            tags = soup.select(elem)
            for tag in tags:
                link_list.append(tag.attrs['href'])
                q_list.append(tag.text)
    q_and_link = dict(zip(q_list, link_list))
    return q_and_link

def answer_collector(urls):
    for url in urls:
        try:
            html = requests.get(url).content
            soup = bs(html, 'lxml')
            n_ans = soup.select("#answerArea > div > div.c-classify.c-classify--sorting > div.c-classify__title-part > h3 > em")
            n_ans = int(n_ans[0].string)
            for i in range(n_ans):
                text = soup.find('div', class_="answer-content__list _answerList").text
                only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
                f = open('prj_naver_qna.txt', 'a', encoding='utf-8')
                f.write(only_kor)
                f.close
        except IndexError: print(f"Index Error occured at {url}")

if __name__ == "__main__":
    page_n = int(input("How many pages you need to lookup?: "))
    q_and_link = crawl_question(page_n)
    df = pd.DataFrame(list(q_and_link.items()), columns = ['Questions', 'URLs'])
    answer_collector(list(df["URLs"]))

