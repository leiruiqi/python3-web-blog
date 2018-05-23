

import requests
import time
import urllib.parse as parse
from bs4 import BeautifulSoup

class ArticelTitleList:
    def __init__(self,url):
        self.url =url
        
    def getAllTitles(self):

        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "lxml")

        newsList = soup.findAll("div", "mod newslist")

        newstitles =  []
        for x in newsList[0].findAll("a", {"target": "_blank"}):
            articleUrl = (x["href"])
            path = parse.urlparse(articleUrl).path
            index1 = path.index('/', 3);

            index2 = path.index('.');
            id=self.dateStr+path[index1+1:index2]
            title = x.string
            newstitles.append(ArticleTitle(title,id,articleUrl))
        return newstitles;

    def findDateFromUrl(self):
        url = parse.urlparse(self.url)
        path = url.path
        index1 = path.index('/',1);
        index2 = path.index('_');
        index3 = path.index('.');
        month = path[index1+1:index1+7]
        day = path[index2+1:index3]
        dateStr =month+day
        self.dateStr = dateStr
        return dateStr

class ArticleTitle:

    def __init__(self,title,id,url):
        self.title = title
        self.id = id
        self.url= url
    pass