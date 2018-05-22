#!/user/bin/env python
# -*-coding:utf-8-*-

import sys,requests
from pyquery import PyQuery as pq

reload(sys) 
sys.setdefaultencoding('utf-8')


# fo = open("datas/political.txt", "a+")
# for page in xrange(2, 100):
#     content = requests.get('http://news.qq.com/newsgn/zhxw/shizhengxinwen_'+str(page)+'.htm')
#     dom     = pq(content.text)
#     lists   = dom('.newslist li a')
#     for item in lists.items():
#         print item.text()
#         fo.write(item.text()+"\n")
# fo.close()


# fo = open("datas/science.txt", "a+")
# for page in xrange(211, 230):
#     content = requests.get('http://news.hiapk.com/brands/list_23_'+str(page)+'.html')
#     dom     = pq(content.text)
#     lists   = dom('.main .box strong a')
#     for item in lists.items():
#         print item.text()
#         fo.write(item.text()+"\n")
# fo.close()