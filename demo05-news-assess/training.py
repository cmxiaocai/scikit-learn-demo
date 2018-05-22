#!/user/bin/env python
# -*-coding:utf-8-*-

import commonfunc
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

func = commonfunc.CommonFunc()

# 载入训练数据
datas_political = func.loadDatas('datas/political.txt')
datas_science   = func.loadDatas('datas/science.txt')
classify, train_data, train_target = func.makeTrainDatas({'政治新闻': datas_political, '科技新闻': datas_science})
print classify
print "政治:%s篇 科技:%s篇" % (len(datas_political), len(datas_science))

# 中文分词
train_data = func.jieba(train_data)

# 将文本中的词语转换为词频矩阵
vectorizer       = CountVectorizer()
tfidftransformer = TfidfTransformer()
tfidf = tfidftransformer.fit_transform(vectorizer.fit_transform(train_data))
print "tfidf词频矩阵:", tfidf.shape

# 训练模型
clf = MultinomialNB().fit(tfidf, train_target)

# 测试模型
test_docs = [
    "中国3月增持110亿美元美债近期收益率持续走高",
]
test_docs  = func.jieba(test_docs)
test_tfidf = tfidftransformer.fit_transform(vectorizer.transform(test_docs))
print "测试词频:", test_tfidf.shape
predicted = clf.predict(test_tfidf)
print "预测:", predicted, classify[predicted[0]], test_docs[0]

# 保存模型
joblib.dump(clf, 'bin/model.pkl') # 保存分类器
joblib.dump(vectorizer, 'bin/model.vect') 