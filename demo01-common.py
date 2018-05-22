#!/user/bin/env python
# -*-coding:utf-8-*-

import sys
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


iris   = datasets.load_iris()
iris_x = iris.data
iris_y = iris.target
train_x, test_x, train_y, test_y = train_test_split(iris_x, iris_y, test_size=0.2)

print len(iris_x), len(iris_y)

knn = KNeighborsClassifier()
knn.fit(train_x, train_y)

print '预测准确率:',knn.score(test_x, test_y)
res = knn.predict(test_x)
print res
print test_y
