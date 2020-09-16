#!/usr/bin/python3
"""
Created on Sun Aug  9 19:58:48 2020
@author: Heedong Yang
@Usage: 폐교활용방안 마이닝된 텍스트 워드클라우드
"""
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
#import pdb

def create_plots(nouns):
    no_use_list = ["폐교","현황","활용","활용", "학교", "그림","목적", "보기", "배포", "및", "무단", "기사"]
    ## 한글자 제거
    for i, v in enumerate(nouns):
        if len(v) == 1: nouns.pop(i)
        if v in no_use_list: nouns.pop(i)
    ## 명사 빈도 카운팅
    count_nouns = Counter(nouns)
    top_list = count_nouns.most_common(20)
    words = []; frequency = []
    for v in top_list:
        words.append(v[0])
        frequency.append(v[1])
    index = list(range(len(top_list)))
    ## 빈도수 막대 그래프
    plt.figure(figsize=(25,16))
    plt.xlabel("단어/명사")
    plt.ylabel("빈도수")
    plt.title("최tfidf")
    plt.bar(index, frequency, tick_label=words, align='center' )
    plt.show()

    ## 워드 클라우드
    wc = WordCloud(font_path="C:/Windows/Fonts/H2GTRM.ttf", background_color="black", \
                   width=1000, height=1000, max_words=100, collocations = False, \
                       max_font_size=300).generate(str(nouns))
    #pdb.set_trace()
    plt.figure(figsize=(25,25))
    plt.imshow(wc, interpolation='lanczos')
    plt.axis('off')
    plt.show()

def plotter(file):
    f = open(file, 'r',encoding = 'utf-8-sig')
    text = f.read()
    f.close()
    nouns = okt.nouns(text)
    ## 그래프 함수 호출
    create_plots(nouns)

def checker(file, num):
    f = open(file, 'r',encoding = 'utf-8-sig')
    text = f.read()
    f.close()
    nouns = okt.nouns(text)
    ## 명사 빈도 카운팅
    count_nouns = Counter(nouns)
    top_list = count_nouns.most_common(num)
    return top_list

if __name__ == "__main__":
    ## 한글 폰트 설정
    path_to_font = "C:/Windows/Fonts/H2GTRM.ttf"
    font_name = fm.FontProperties(fname=path_to_font).get_name()
    plt.rc('font', family=font_name)
    ## okt 객체들 생성
    okt = Okt()
    ## 파일명 리스트
    #cnt = checker("기존지표_termstext_forWC.txt", 1000)
    #print(cnt)
    #df = pd.DataFrame(cnt,columns = ['단어','빈도수'])
    #print(df)
    #df.to_csv(r'C:/Users/Heedong/Desktop/빅데이터_prj/폐교연구자료텍스트.txt', index=False, header=True, encoding='utf-8-sig')
    ## 플롯팅
    plotter("C:/Users/Heedong/지표와우수사례_termstext_forWC.txt")

