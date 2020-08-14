#!/usr/bin/python3
"""
Created on Sun Aug  9 19:58:48 2020
@author: 남보은 안한성 양희동 이지연
@Usage: 폐교활용방안 마이닝된 텍스트 워드클라우드 생
"""
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
'''
신문사 = 20건 이상 등장한 단어들... 미만에서도 쓸만한게 있어보임
우수사례 = 1~2번 등장한 단어중에서도 쓸만한게 많아보임
논문 = 약 30건 이상 등장한 단어들...
지식인 = 제외
'''

def create_plots(nouns):
    no_use_list = ["폐교","현황","활용","활용", "학교", "그림","목적", "보기", "배포", "및", "무단", "기사"]
    ## 한글자 제거
    for i, v in enumerate(nouns):
        if len(v) == 1: nouns.pop(i)
        if v in no_use_list: nouns.pop(i)
    ## 명사 빈도 카운팅
    count_nouns = Counter(nouns)
    top_list = count_nouns.most_common(30)
    words = []; frequency = []
    for v in top_list:
        words.append(v[0])
        frequency.append(v[1])
    index = list(range(len(top_list)))
    ## 빈도수 막대 그래프
    plt.figure(figsize=(25,16))
    plt.xlabel("단어/명사")
    plt.ylabel("빈도수")
    plt.title("IMSI")
    plt.bar(index, frequency, tick_label=words, align='center' )
    plt.show()

    ## 워드 클라우드
    wc = WordCloud(font_path="C:/Windows/Fonts/H2GTRM.ttf", background_color="white", \
                   width=1000, height=1000, max_words=100, \
                       max_font_size=300).generate(str(nouns))
    plt.figure(figsize=(25,25))
    plt.imshow(wc, interpolation='lanczos')
    plt.axis('off')
    plt.show()

def plotter(text_files):
    response = input("어떤 파일을 플롯팅 하고 싶으신가요?[a/1/2/3]\na-전부\n1-뉴스\n2-사례집\n3-연구자료\n")
    if response == 'a':
        for file in text_files:
            f = open(file, 'r',encoding = 'utf-8')
            text = f.read()
            f.close()
            nouns = okt.nouns(text)
            ## 그래프 함수 호출
            create_plots(nouns)
    elif response in ['1','2','3']:
        f = open(text_files[int(response)-1], 'r',encoding = 'utf-8')
        text = f.read()
        f.close()
        nouns = okt.nouns(text)
        ## 그래프 함수 호출
        create_plots(nouns)
    else: print("Error: Invalid Input")

def checker(file, num):
    f = open(file, 'r',encoding = 'utf-8')
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
    text_files = ['뉴스자료텍스트.txt','우수사례텍스트.txt','폐교연구자료텍스트.txt']
    ## 명사 개수 체크  우수사례텍스트=>2000개, 연구자료텍스트=>6000개, 뉴스텍스트=> 10000ㄱ
    cnt = checker(text_files[0], 10000)
    print(cnt[9900:])
    df = pd.DataFrame(cnt,columns = ['단어','빈도수'])
    print(df)
    df.to_csv(r'C:/Users/Heedong/Desktop/빅데이터_prj/폐교연구자료텍스트.txt', index=False, header=True, encoding='utf-8-sig')
    ## 플롯팅
    #plotter(text_files)



