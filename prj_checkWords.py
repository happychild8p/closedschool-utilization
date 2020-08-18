
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created: Tue Aug 18 08:26:31 EDT 2020
@author: 남보은 안한성 양희동 이지연

"""
from konlpy.tag import Okt
from collections import Counter
import pandas as pd
    
if __name__ == "__main__":
    ## 지표 단어 리스트
    B1 = ["지역경제", "소득증대", "관광객", "수익성", "일자리", "관광거점", "평생교육", "문화창출", "복지증대", "지역발전"]
    B3 = ["활용성", "기능성", "가변성", "활용도", "리모델링", "공간구성", "공공시설", "공간효율", "공간설계"]
    B4 = ["편의시설", "편의공간", "휴식공간", "편리성"]
    B5 = ["자연생태", "친환경", "생태공간"]
    B9 = ["유관기관", "연계활용", "네트워크"]
    B10 = ["지역문화", "역사도시", "관광지", "특성화", "정체성", "역사성", "관광자원"]
    B11 = ["지역주민", "주민투표", "공동체", "주민자치위원회", "의견수렴"]  
    B12 = ["사업비", "지원사업", "투자성", "활용률", "활용가치", "미활용", "방치", "사업계획서", "경제성"]
    B13 = ["농어촌", "도서벽지", "도심지역", "산간벽지", "자연환경", "보호구역", "구도심"]
    ## okt 객체 생성
    okt = Okt()
    ## 파일명 리스트
    text_files = ['뉴스자료텍스트.txt','우수사례텍스트.txt','폐교연구자료텍스트.txt']
    newslist = ["kbs.txt","mbc.txt","sbs.txt","obs.txt", "ytn.txt", "kwdmib.txt", "kwib.txt", "kkib.txt", "kndmib.txt","knsm.txt", "ksib.txt", "kiib.txt","kjmism.txt","kjib.txt","kmib.txt","nism.txt","djib.txt","daib.txt","digitaltimes.txt","mikj.txt","mism.txt","moneytoday.txt","mdib.txt","mwhib.txt","bsib.txt","swsm.txt","skib.txt","ajkj.txt","usmi.txt","jnib.txt","jbdmib.txt","jbib.txt","enews.txt","jmib.txt","jsib.txt","jdib.txt","jungbu.txt","centerib.txt","cbib.txt","ccib.txt","cctoday.txt","financialnews.txt","hkr.txt","hrib.txt"]     

    ## 명사 개수 체크
    ############################### 여기 두줄만 바꾸세요 ##############################
    file = text_files[2]
    num = 1000
    ##################################################################################
    f = open(file, 'r',encoding = 'utf-8')
    text = f.read()
    f.close()
    nouns = okt.nouns(text)
    ## 명사 빈도 카운팅     
    count_nouns = Counter(nouns)
    top_list = count_nouns.most_common(num)
    print(len(top_list))
    ## 저장
    total = [];b1t=[]; b3t=[]; b4t=[]; b5t=[]; b9t=[]; b10t=[]; b11t=[]; b12t=[]; b13t=[]
    for ele in top_list:
        if ele[0] in B1: 
            print("단어:", ele[0],"  등장빈도: ",ele[1])
            total.append(ele)
            b1t.append(ele)  
        elif ele[0] in B3: 
            print("단어:", ele[0],"  등장빈도: ",ele[1])
            total.append(ele)
            b3t.append(ele)
        elif ele[0] in B4: 
            print("단어:", ele[0],"  등장빈도: ",ele[1])
            total.append(ele)
            b4t.append(ele)
        elif ele[0] in B5: 
            print("단어:", ele[0],"  등장빈도: ",ele[1])
            total.append(ele)
            b5t.append(ele)
        elif ele[0] in B9: 
            print("단어:", ele[0],"  등장빈도: ",ele[1])
            total.append(ele)
            b9t.append(ele)
        elif ele[0] in B10: 
            print("단어:", ele[0],"  등장빈도: ",ele[1])
            total.append(ele)
            b10t.append(ele)
        elif ele[0] in B11: 
            print("단어:", ele[0],"  등장빈도: ",ele[1])
            total.append(ele)
            b11t.append(ele)
        elif ele[0] in B12: 
            print("단어:", ele[0],"  등장빈도: ",ele[1])
            total.append(ele)
            b12t.append(ele)
        elif ele[0] in B13: 
            print("단어:", ele[0],"  등장빈도: ",ele[1])
            total.append(ele)
            b13t.append(ele)
    
    df = pd.DataFrame(total, columns = ['단어','빈도수'])
    print(df)
    df.to_csv(r'C:/Users/Heedong/Desktop/빅데이터_prj/타겟단어_연구자료.csv', index=False, header=True, encoding='utf-8-sig')
    
    print(b1t)
    print(b3t)
    print(b4t)
    print(b5t)
    print(b9t)
    print(b10t)
    print(b11t)
    print(b12t)
    print(b13t)
    print(total)
