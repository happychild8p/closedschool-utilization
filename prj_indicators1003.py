#!/usr/bin/python3
'''
Closed School Utilization with text mining
Purpose: To extract useful keywords could be assist those who want to utilze closed school
Author: Heedong Yang

After crawling news
Use news, theses and example text to
1. Clean it: 
2. Tokenize
3-1. Create dtm
3-2. Apply tfidf
4. Apply LDA to group words
'''

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from konlpy.tag import Hannanum
import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pyLDAvis.sklearn
from gensim.models import Word2Vec
from apyori import apriori


def get_cleaned_text(file, doc_len=-1):
    f = open(file, 'r', encoding='utf-8')
    newsStr = f.read()
    doclist = list(newsStr.split("|"))[0:doc_len]
    f.close()
    cleaned_docs = []
    for doc in doclist:
        cleaned_doc = re.sub("[^가-힣0-9\,\.~)(]"," ",doc)
        cleaned_doc = re.sub('\s+'," ",cleaned_doc)
        cleaned_docs.append(cleaned_doc)
    return cleaned_docs

def tokenization(cleaned_docs):
    han = Hannanum()
    tokenized_docs = []
    while ' ' in cleaned_docs: cleaned_docs.remove(' ')
    for doc in cleaned_docs:
        nouns_in_doc = []
        for noun in han.nouns(doc):
            if len(noun) > 1: nouns_in_doc.append(noun)
        tokenized_docs.append(nouns_in_doc)
    return tokenized_docs

def create_dtm(tokenized_docs, mindf = 2):
    docs_list = []
    dtm = CountVectorizer(min_df=mindf)
    for each in tokenized_docs:
        docs_list.append(' '.join(each))
    dt_matrix = dtm.fit_transform(docs_list)
    dt_terms = dtm.get_feature_names()
    return dtm, dt_matrix, dt_terms

def tf_idf(tokenized_docs):
    detokenized_docs = []
    for doc in tokenized_docs:
        text = ' '.join(doc)
        detokenized_docs.append(text)

    tfidf = TfidfVectorizer(min_df=1, max_features= 20000)
    tfidf_matrix = tfidf.fit_transform(detokenized_docs)
    tfidf_terms = tfidf.get_feature_names()
    return tfidf, tfidf_matrix, tfidf_terms

def apply_lda(topics, iteration, matrix, terms):
    #### Latent Dirichlet Allocation
    lda_model = LatentDirichletAllocation(n_components=topics , learning_method='online', random_state=777, max_iter=iteration)
    lda_top = lda_model.fit_transform(matrix)

    a = input("Do you want to see the topics and linked words? [y/n]")
    if a == 'y': get_topics(lda_model.components_, terms);
    return lda_model

def get_topics(components, feature_names, n=30):
    for idx, topic in enumerate(components):
        print("Topic %d :" % (idx+1), [(feature_names[i], topic[i].round(2)) for i in topic.argsort()[:-n -1:-1]])

def apply_word2vec(tokenized_docs, keyword, size=100, window=2,min_count=10,iteration=100):
    w2vmodel = Word2Vec(sentences=tokenized_docs, min_count=min_count)
    print(w2vmodel.wv.most_similar(positive=[keyword], topn=20))
    return w2vmodel

if __name__ == "__main__":
    cleaned_docs = get_cleaned_text("뉴스텍스트.txt",5)
    tokenized_docs = tokenization(cleaned_docs)
    #### df matrix로 lda
    #dtm, dt_matrix, dt_terms = create_dtm(tokenized_docs, 3)
    #lda_model = apply_lda(30, 20, dt_matrix, dt_terms)
    #### tf-idf maxrix로 lda 그대로 쓰는것에 비해 오히려 관련도가 떨어짐
    tfidf, tfidf_matrix, tfidf_terms = tf_idf(tokenized_docs)
    lda_model = apply_lda(30, 20, tfidf_matrix, tfidf_terms)

    #### LDA 시각화
    pyLDAvis.enable_notebook()
    vis = pyLDAvis.sklearn.prepare(lda_model, tfidf_matrix)
    #### 벡터화로 비슷한 단어 나타내기 tokenization 이후 Word2Vec
    ## 이걸로 지표별 연관 단어 찾고
    apply_word2vec(tokenized_docs, "")


######## 네트워크 분석 ###########################
    result = list(apriori(tokenized_docs, min_support=0.01))
    df = pd.DataFrame(result)
    df['length'] = df['items'].apply(lambda x: len(x))
    df = df[(df['length'] == 2) & (df['support'] >= 0.01)].sort_values(by='support', ascending=False)

########### 여기서부터
    # tfidf_dict = {}
    # for idx, terms in enumerate(tfidf.get_feature_names()):
    #     tfidf_dict[terms] = idx

    # for i, sent in enumerate(detokenized_docs):
    #     print('====== document[%d] ======' % i)
    #     print( [ (token, sp_matrix[i, tfidf_dict[token]]) for token in sent.split() ] )

    # matrix_array = tfidf_matrix.toarray()
    # print(matrix_array.shape)

########### 이거는 tf-idf가 해결 된 다음
    lda_model = LatentDirichletAllocation(n_components=20 , learning_method='online', random_state=777, max_iter=10)
    lda_top = lda_model.fit_transform(tfidf_matrix)

    #print(lda_model.components_)
    #print(lda_model.components_.shape)

    terms = tfidf.get_feature_names()
    print(terms)
    get_topics(lda_model.components_, terms)

