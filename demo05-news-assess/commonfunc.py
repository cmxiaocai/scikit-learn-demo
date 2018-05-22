#!/user/bin/env python
# -*-coding:utf-8-*-

import jieba

class CommonFunc(object):
    
    def loadDatas(self, file):
        datas = []
        for line in open(file):
            datas.append(line.strip())
        return datas

    def makeTrainDatas(self, trainDatas):
        datas   = []
        targets = []
        keys    = trainDatas.keys()
        for index, key in enumerate(keys):
            for line in trainDatas[key]:
                datas.append(line)
                targets.append(index)
        return [keys, datas, targets]

    def jieba(self, datas):
        for index, title in enumerate(datas):
            datas[index] = " ".join(list(jieba.cut(title)))
        return datas
