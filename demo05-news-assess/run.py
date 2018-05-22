#!/user/bin/env python
# -*-coding:utf-8-*-

import commonfunc
import sys, jieba
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.externals import joblib

if len(sys.argv) < 2:
    print 'format:\n\t python run.py "人民日报钟声：不打贸易战，是中美双方共识"'
    sys.exit()

func     = commonfunc.CommonFunc()
classify = ['\xe7\xa7\x91\xe6\x8a\x80\xe6\x96\xb0\xe9\x97\xbb', '\xe6\x94\xbf\xe6\xb2\xbb\xe6\x96\xb0\xe9\x97\xbb']

# 加载模型
tfidftransformer = TfidfTransformer()
clf              = joblib.load('bin/model.pkl')     # 加载分类器
vectorizer       = joblib.load('bin/model.vect')    # 读取适量化


# 使用模型
test_docs  = func.jieba([sys.argv[1]])
test_tfidf = tfidftransformer.fit_transform(vectorizer.transform(test_docs))
predicted  = clf.predict(test_tfidf)
probas     = clf.predict_proba(test_tfidf)

print "标题:", sys.argv[1]
print "分词:", test_docs[0]
print "测试词频:", test_tfidf.shape
print "预测分类:", predicted, classify[predicted[0]]
print "预测评分:", probas[0][predicted[0]]
# print clf.predict_proba(test_tfidf)