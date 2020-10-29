#!/usr/bin/python3
'''
@Authership declaration@
@ Author: Heedong Yang
@ Purpose: Closed school utilization projcet Part1 : Making Indicator using text analysis
@ Date: Oct 22, 2020
@ Usage:
'''
import pandas as pd
import networkx as nx
from konlpy.tag import Hannanum
import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import gensim
from gensim.models import Word2Vec
from apyori import apriori


def get_cleaned_text(file, doc_len=-1):
    f = open(file, 'r', encoding='utf-8')
    newsStr = f.read()
    #doclist = list(newsStr.split("|"))[0:doc_len]
    doclist = list(newsStr.split("|"))
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

def apply_lda(topics, iteration, wrd_per_grp , matrix, terms):
    #### Latent Dirichlet Allocation
    lda_model = LatentDirichletAllocation(n_components=topics , learning_method='online', random_state=777, max_iter=iteration)
    lda_top = lda_model.fit_transform(matrix)

    a = input("Do you want to see the topics and linked words? [y/n]")

    if a == 'y':
        for idx, topic in enumerate(lda_model.components_):
            print("Topic %d :" % (idx+1), [(terms[i], topic[i].round(2)) for i in topic.argsort()[:-wrd_per_grp -1:-1]])

def gensim_lda(tokenized_docs, n_tpic=20, n_wrd=10):
    dictionary = gensim.corpora.Dictionary(tokenized_docs)
    corpus = [dictionary.doc2bow(text) for text in tokenized_docs]
    lda_model = gensim.models.ldamodel.LdaModel(corpus, num_topics = n_tpic, id2word=dictionary)
    topics = lda_model.print_topics(num_words=n_wrd)
    for topic in topics: print(topic);
    #### LDA 시각화
    #a = input("Do you want to visualize result?[y/n] ")
    #if a == 'y':
        #pyLDAvis.enable_notebook()
        #vis = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary)
        #pyLDAvis.show(vis)#This could be done in jupyter notebook

def apply_word2vec(tokenized_docs, keyword, size=100, window=2,min_count=10,iteration=100):
    w2vmodel = Word2Vec(sentences=tokenized_docs, min_count=min_count)
    print(w2vmodel.wv.most_similar(positive=[keyword], topn=20))
    return w2vmodel

if __name__ == "__main__":
    cleaned_docs = get_cleaned_text("통합텍스트.txt",-1)
    tokenized_docs = tokenization(cleaned_docs)
    #### df matrix로 lda
    # dtm, dt_matrix, dt_terms = create_dtm(tokenized_docs, 3)
    #apply_lda(100,50, 10, dt_matrix, dt_terms)

    #### tf-idf maxrix로 lda  #####그대로 쓰는것에 비해 오히려 관련도가 떨어짐
    tfidf, tfidf_matrix, tfidf_terms = tf_idf(tokenized_docs)
    apply_lda(100, 50, 10, tfidf_matrix, tfidf_terms)

    #gensim_lda(tokenized_docs, 500, 10)  #### for lda visualization and results is slightly different than scikitlearn LDA model
    #### 벡터화로 비슷한 단어 나타내기 tokenization 이후 Word2Vec
    apply_word2vec(tokenized_docs, "")

