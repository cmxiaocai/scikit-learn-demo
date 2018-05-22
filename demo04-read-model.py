#!/user/bin/env python
# -*-coding:utf-8-*-

'''
读取模型
'''

import jieba
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib



# 测试
docs = [
    "8道蒸菜做法美味营养下饭",
    "中国3月增持110亿美元美债近期收益率持续走高",
]
tmp = []
for title in docs:
    tmp.append(" ".join(list(jieba.cut(title))))
X_new_counts = tmp


tfidftransformer = TfidfTransformer()
clf              = joblib.load('testdata/article-classify.pkl')     # 加载分类器
vectorizer       = joblib.load('testdata/article-classify.vect')    # 读取适量化



new_tfidf  = tfidftransformer.fit_transform(vectorizer.transform(X_new_counts))
print new_tfidf.shape
predicted  = clf.predict(new_tfidf)
print predicted


for doc, category in zip(docs, predicted):
    print('%r => %s' % (category, doc))