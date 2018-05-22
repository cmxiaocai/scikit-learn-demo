#!/user/bin/env python
# -*-coding:utf-8-*-

import jieba
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB


content_train = []
opinion_train = []

# 读取文件，分别存储分类和标题
file = './testdata/article-type.log'
for line in open(file):
    reader = line.split('#')
    content_train.append(reader[1].strip())
    opinion_train.append(reader[0])

# 对标题进行分词
tmp = []
for title in content_train:
    tmp.append(" ".join(list(jieba.cut(title))))
content_train = tmp

# 将文本中的词语转换为词频矩阵
vectorizer       = CountVectorizer()
tfidftransformer = TfidfTransformer()
tfidf = tfidftransformer.fit_transform(vectorizer.fit_transform(content_train))  # 先转换成词频矩阵，再计算TFIDF值;使用TF-IDF,生成特征矩阵
print tfidf.shape   # (100, 676) 100条数据共676个词频

word   = vectorizer.get_feature_names() # 词
weight = tfidf.toarray() # 权重

# 训练模型
clf01 = MultinomialNB().fit(tfidf, opinion_train)
print '----'
print clf01.get_params()
print clf01.score(tfidf, opinion_train)

# 测试
docs = [
    "8道蒸菜做法美味营养下饭",
    "中国3月增持110亿美元美债近期收益率持续走高",
    "XX公司可能会上市",
]
tmp = []
for title in docs:
    tmp.append(" ".join(list(jieba.cut(title))))
docs = tmp

new_tfidf = tfidftransformer.transform(vectorizer.transform(docs))
predicted = clf01.predict(new_tfidf)
print predicted
print clf01.score(new_tfidf, ['1', '2', '2'])

# -------
# 样本与测试
# from sklearn.model_selection import train_test_split
# from sklearn import preprocessing
# train_x, test_x, train_y, test_y = train_test_split(tfidf, opinion_train, test_size=0.3)
# clf02 = MultinomialNB().fit(train_x, train_y)
# print '预测准确率:',clf02.score(test_x, test_y)

# predicted = clf02.predict(test_x)
# print predicted
# print test_y


# ---------
# 保存模型
from sklearn.externals import joblib
joblib.dump(clf01, 'testdata/article-classify.pkl') # 保存分类器
joblib.dump(vectorizer, 'testdata/article-classify.vect') # 保存矢量化，因为需要使用和训练器相同的矢量器，不然会报错，提示ValueError dimension mismatch...


