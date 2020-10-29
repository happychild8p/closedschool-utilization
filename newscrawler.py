#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 14:13:50 2020
@author: Heedong Yang
@purpose:
    Bigdata Project "Utilize Closed school"
    Crawling newspaper articles for text mining
    Saving text separately
    Keyword = "폐교 활용"
"""

from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import re
##### FUNCTIONS ######
'''
Collecting Korean Text from news company.
Each function collect only one.
Version 1
Will be merged into 1 or so
##############################################
Excpetions are
서울경제 경상일보 경향신문 아시아경제 한국경제 헤럴드경제
국제신문 국제신문 경향신문 서울경제 아시아경제 한국경제
한국일보 헤럴드경제 중부매일
'''
def kbs(urls): ##KBS
    for url in urls:
        try:
            html = requests.get(url).content
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="detail-body font-size", id='cont_newstext').text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('kbs.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"ERROR has been occured @{url}")

def mbc(urls): ##MBC
    for url in urls:
        try:
            html = requests.get(url).content
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="news_txt").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('mbc.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url {url}"); break;

def sbs(urls): ##SBS
    for url in urls:
        try:
            html = requests.get(url).content
            soup = bs(html, 'lxml')
            text = soup.find('div', class_= "text_area").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('sbs.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url {url}"); break;

def obs(urls):  ##OBS
    for url in urls:
        try:
            html = requests.get(url).content
            soup = bs(html, 'lxml')
            text = soup.find('div', id="CmAdContent").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('obs.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url {url}")

def ytn(urls): ##YTN
    for url in urls:
        try:
            html = requests.get(url).text
            soup = bs(html, 'lxml')
            text = soup.find('div', class_= "article_paragraph").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('ytn.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url {url}");

def kwdmib(urls): ##강원도민일보
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content
            soup = bs(html, 'lxml')
            text = soup.find('div', class_= "article-body").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('kwdmib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url {url}");

def kwib(urls): ##강원일보
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).text
            soup = bs(html, 'lxml')
            text = soup.find('div', class_= "nViewBody").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('kwib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def kkib(urls):
    ###경기일보에서 43개 기사 에러 발생(30개만 수집됨)
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content
            soup = bs(html, 'lxml')
            text = soup.find('div', class_= "user-content").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('kkib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def kndmib(urls): ##경남도민일보
    for url in urls:
        try:
            html = requests.get(url).content
            soup = bs(html, 'lxml')
            text = soup.find('div', itemprop="articleBody").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('kndmib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def knsm(urls): #경남신문
    for url in urls:
        try:
            html = requests.get(url).content
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="cont_cont").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('knsm.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def ksib(urls): # 경상일보
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content
            soup = bs(html, 'lxml')
            text = soup.find('div', id='CmAdContent').text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('ksib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def kiib(urls): # 경인일보
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content
            soup = bs(html, 'lxml')
            text = soup.find('div', class_= "view_txt clearfix").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('kiib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def kjmism(urls): # 광주매일신문
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content
            soup = bs(html, 'lxml')
            text = soup.find('font', class_="jul").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('kjmism.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except AttributeError: print(f"Error at url{url}");

def kjib(urls): #광주일보
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="read", id="content").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('kjib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except AttributeError: print(f"Error at url{url}");

def kmib(urls): # 국민일보
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="tx", id="articleBody").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('kmib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except AttributeError: print(f"Error at url{url}");

def nism(urls): # 내일신문
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="article", id="contents").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('nism.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except AttributeError: print(f"Error at url{url}");

def djib(urls): # 대전일보
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', id="CmAdContent").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('djib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except AttributeError: print(f"Error at url{url}");

def daib(urls): # 동아일보
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="article_txt").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('daib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except AttributeError: print(f"Error at url{url}");

def digitaltimes(urls): # 디지털타임스
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="art_txt").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('digitaltimes.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except AttributeError: print(f"Error at url{url}");

def mikj(urls): # 매일경제  ## 16개 기사 크롤링 불가능
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', id="article_body").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('mikj.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except AttributeError: print(f"Error at url{url}");

def mism(urls): # 매일신문 ## 6개 기사 크롤링 불가능
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="article_content").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('mism.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except AttributeError: print(f"Error at url{url}");

def moneytoday(urls): # 머니투데이 ## 2개 기사 크롤링 불가능
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', id="textBody").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('moneytoday.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except AttributeError: print(f"Error at url{url}");

def mdib(urls): # 무등일보 오류 64개
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="newsbody").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('mdib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except AttributeError: print(f"Error at url{url}");

def mwhib(urls): # 문화일보 에러 10개
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', id="NewsAdContent").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('mwhib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except AttributeError: print(f"Error at url{url}");

def bsib(urls): # 부산일보
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="article_content").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('bsib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except AttributeError: print(f"Error at url{url}");

def swsm(urls): # 서울신문 총 35개 에러
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', id="atic_txt1").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('swsm.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def skib(urls): # 세계일보 총 1개 에러
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', id="article_txt").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('skib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except AttributeError: print(f"Error at url{url}");

def ajkj(urls): # 아주경제
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', id="articleBody").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('ajkj.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def ynib(urls): # 영남일보 총 3개 에러
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="news_text").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('ynib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def usmi(urls): # 울산매일
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="cont-body").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('usmi.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def jnib(urls): # 전남일보
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="article_content").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('jnib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def jbdmib(urls): # 전북도민일보
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="user-content").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('jbdmib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def jbib(urls): # 전북일보
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', id="article-view-content-div").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('jbib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def enews(urls): # 전자신문
    for url in urls:
        try:
            #if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('p').text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('enews.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def jmib(urls): # 제민일보
    for url in urls:
        try:
            #if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="article-body").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('jmib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def jsib(urls): # 조선일보
    for url in urls:
        try:
            #if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="news_body").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('jsib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def jdib(urls): # 중도일보
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="view-main").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('jdib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def jbmi(urls): # 중부매일
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', id="article-view-content-div").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('jbmi.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def jungbu(urls): # 중부일보
    for url in urls:
        try:
            if url[0:4] != "http": url = f"http://{url}";
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="article-body").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('jungbu.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def centerib(urls): # 중앙일보
    for url in urls:
        try:
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', id="content").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('centerib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()

        except: print(f"Error at url{url}");

def cbib(urls): # 충북일보
    for url in urls:
        try:
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="article").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('cbib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def ccib(urls): # 충청일보
    for url in urls:
        try:
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('td', class_="view_r").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('ccib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def cctoday(urls): # 충청투데이
    for url in urls:
        try:
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', id="article-view-content-div").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('cctoday.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def financialnews(urls): # 파이낸셜뉴스 1개 에러
    for url in urls:
        try:
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="contents").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('financialnews.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def hkr(urls): # 한겨레
    for url in urls:
        try:
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="text").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('hkr.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

def hrib(urls): # 한라일보 총 23개 오류 발생
    for url in urls:
        try:
            html = requests.get(url).content ## .text 에서 한글깨짐 오류
            soup = bs(html, 'lxml')
            text = soup.find('div', class_="cont_gisa").text
            only_kor = re.sub("[^가-힣0-9\,\.~)(]"," ",text)
            f = open('textfromnews.txt', 'a', encoding='utf-8')
            f.write(only_kor)
            f.write("|")
            f.close
            localF = open('hrib.txt', 'a', encoding='utf-8')
            localF.write(only_kor)
            localF.write("|")
            localF.close()
        except: print(f"Error at url{url}");

if __name__ == "__main__":
    df = pd.read_excel("C:/Users/Heedong/Downloads/NewsResult_20140311-20200901.xlsx")
    # pd.set_option("display.max_columns",30)
    # pd.set_option("display.max_rows",20)
    df = df[["언론사","일자","제목","URL"]]
    df = df.dropna()
    df = df[~df["언론사"].isin(["국제신문", "경향신문", "서울경제", "아시아경제", "한국경제", "한국일보", "헤럴드경제"])]
    newscompany = list(df.groupby("언론사").count().index)

    for corp in newscompany:
        globals()[f'urls_{corp}'] = list(df.loc[df["언론사"] == corp, "URL"])
    kbs(urls_KBS)
    mbc(urls_MBC)
    sbs(urls_SBS)
    obs(urls_OBS)
    ytn(urls_YTN)
    kwdmib(urls_강원도민일보)
    kwib(urls_강원일보)
    kkib(urls_경기일보)
    kndmib(urls_경남도민일보)
    knsm(urls_경남신문)
    ksib(urls_경상일보)
    kiib(urls_경인일보)
    kjmism(urls_광주매일신문)
    kjib(urls_광주일보)
    kmib(urls_국민일보)
    nism(urls_내일신문)
    djib(urls_대전일보)
    daib(urls_동아일보)
    digitaltimes(urls_디지털타임스)
    mikj(urls_매일경제)
    mism(urls_매일신문)
    moneytoday(urls_머니투데이)
    mdib(urls_무등일보)
    mwhib(urls_문화일보)
    bsib(urls_부산일보)
    swsm(urls_서울신문)
    skib(urls_세계일보)
    ajkj(urls_아주경제)
    usmi(urls_울산매일)
    jnib(urls_전남일보)
    jbdmib(urls_전북도민일보)
    jbib(urls_전북일보)
    enews(urls_전자신문)
    jmib(urls_제민일보)
    jsib(urls_조선일보)
    jdib(urls_중도일보)
    jungbu(urls_중부일보)
    centerib(urls_중앙일보)
    cbib(urls_충북일보)
    ccib(urls_충청일보)
    cctoday(urls_충청투데이)
    financialnews(urls_파이낸셜뉴스)
    hkr(urls_한겨레)
    hrib(urls_한라일보)
