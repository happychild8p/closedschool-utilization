####Disclamer: This script only works in R version 3.6.1


install.packages("Sejong")
install.packages("RColorBrewer")
install.packages("wordcloud")
install.packages("multilinguer")
install_jdk()
## Dependencies pac

#kages
install.packages(c('stringr', 'hash', 'tau', 'Sejong', 'RSQLite', 'devtools'), type = "binary")
install.packages("remotes")
remotes::install_github('haven-jeon/KoNLP', upgrade = "never", INSTALL_opts=c("--no-multiarch"))
###불러오기

library(wordcloud)
library(RColorBrewer)
library(multilinguer)
library(rJava) # 에러발생 dependencies 해결을 위해 설치
library(KoNLP) #최종적으로 "KoNLP" 패키지를 불러옵니다

#devtools::install_github('haven-jeon/NIADic/NIADic', build_vignettes = TRUE)
Sys.setenv(JAVA_HOME='C:/Program Files/Java/jre1.8.0_251')  # 설치한 JAVA version에 따라 달라집니다
buildDictionary(ext_dic = "woorimalsam")  # "woorimalsam" dic을 불러옵니다
useNIADic()  # "NIADic" dic을 불러옵니다
###까지 TROUBLE SHOOTING

##### Set environment
setwd("F:/")

text <- readLines("폐교연구자료텍스트.txt", encoding="UTF-8")
buildDictionary(ext_dic="woorimalsam")
pal2 <- brewer.pal(8, "Dark2")
noun <- sapply(text, extractNoun, USE.NAMES = F)
noun

noun2 <- unlist(noun)
noun2

wordcount <- table(noun2)

### 빈도 수 높은 명사 체크 
temp <- sort(wordcount, decreasing=T)[1:10]
temp
barplot(temp, names.arg = names(temp), main="빈도수 높은 명사 체크", ylab= "단어 빈도수")

## 무의미한 단어 제거!!
noun2
### 1글자 제거
noun_re <- noun2[nchar(noun2) > 1]
noun_re
### 문자열 바꾸기 ""로 없애기

for (i in 0:9){
  a <- as.character(i)
  noun_re <- gsub(a,"", noun_re)
}
### . 이랑 , ㅈㅔ거
noun_re <- gsub("\\.","", noun_re) ## . 제거
noun_re <- gsub("\\,","", noun_re) ## , 제거
noun_re <- gsub("[[:digit:]]","", noun_re)  ## 숫자 제거
noun_re <- gsub("m","", noun_re) ## m 및 km에서의 m 제거
noun_re <- gsub("www","", noun_re) ## www 하이퍼링크 텍스트 제거
noun_re <- gsub("[[:punct:]]","", noun_re) ## 기타 특수문자 제거
noun_re <- gsub("폐교","", noun_re)
noun_re <- gsub("활용","", noun_re)
wordcount_re <- table(noun_re)
head(wordcount_re)

sort(wordcount_re, decreasing=T)
### 1번째 인덱스는 "" 이므로 제거
temp_re <- sort(wordcount_re, decreasing=T)[6:26]
temp_re
barplot(temp_re, names.arg = names(temp_re), main="빈도수 높은 명사 체크", ylab= "단어 빈도수")


wordcloud(names(wordcount_re), freq = wordcount_re, scale = c(12,0.7),
          min.freq = 20, random.order=F, rot.per = .1, color=pal2)



