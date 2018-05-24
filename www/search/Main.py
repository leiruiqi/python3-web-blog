#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 23:40:36 2018

@author: macbook
"""
import time
import app.model.ArticleTitleList as al
import app.model.Article as article
import jieba
import jieba.analyse

url = "http://tech.qq.com/l/201804/scroll_20.htm"

qqTitleList = al.ArticelTitleList(url);
dateStr = qqTitleList.findDateFromUrl();
print(dateStr)
titleInfoList = qqTitleList.getAllTitles();
articleInfoList =[]
for titleInfo in titleInfoList:
    ##print(titleInfo.id)
    ##print(titleInfo.title)
    qqArticle = article.QqArticel(titleInfo.url)
    try:
        qqArticle._soup2Data()
    except Exception:
        qqArticle = None
    ##print(qqArticle.data)
    if qqArticle is not None:
        articleInfoList.append(qqArticle)
        ##titleKeywords = jieba.analyse.extract_tags(qqArticle.data['title'], topK=3, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
        ##print(titleKeywords)
        keywords = jieba.analyse.extract_tags(qqArticle.data['context'], topK=3, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
        print(qqArticle.data["title"])
    ##print(keywords)
    ##print(qqArticle.data['tags'])
    time.sleep(1)


with open('QQ_tech_'+dateStr+'.txt','w+') as fw:
    for article in articleInfoList:
        fw.write(article.getJsonStr()+'\n');