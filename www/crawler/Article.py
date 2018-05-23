
import requests
import abc
import json
import demjson
from bs4 import BeautifulSoup

class Article:


    def __init__(self, url):
        ##self.soup = soup
        self.url = url
        self.data = ""


    @abc.abstractmethod
    def _soup2Data(self):pass

    def getId(self):
        return self.data["id"]

    def getJsonStr(self):
        return json.dumps(self.data)



class QqArticel(Article):

    def _soup2Data(self):
        articelresp = requests.get(self.url)
        atricelsoup = BeautifulSoup(articelresp.text, "lxml")

        allcontext = atricelsoup.findAll("p", {"class": "text"})

        allstr = ''
        for context in allcontext:
            ##print(context.string)
            if (context.string is not None):
                allstr += context.string

        ##print(allstr)

        scriptStr = atricelsoup.script.string
        print(scriptStr)
        index1 = scriptStr.index('{')
        str1 = scriptStr[index1:]
        ## print(str1)
        str2 = str1.strip()
        str3 = str2.replace("\n", "").replace(" ", "").replace("\t", "").strip()
        ##print(str3)
        abc = demjson.decode(str3)
        ##print(type(abc))
        abc['context'] = allstr
        self.data = abc;