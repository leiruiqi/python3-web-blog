import jieba
import jieba.analyse
import json
from elasticsearch import Elasticsearch

qq_tech_list=[]
with open('app/QQ_tech_20180128.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        ##print(line.strip())
        data = json.loads(line.strip())
        keywords = jieba.analyse.extract_tags(data['context'], topK=5, withWeight=False, allowPOS=('ns', 'n', 'vn'),withFlag=False)
        ##print(data['title'])
        ##print(data['context'])
        ##print(keywords)
        ##print(data['tags'])

        ##print('~~~~')
        temp = {}
        temp['id']=data['id']
        temp['keywords']=keywords
        temp['tags'] = data['tags']
        temp['title'] = data['title']
        temp['context'] = data['context']
        qq_tech_list.append(temp)
        pass



esclient = Elasticsearch(['localhost:9200'])

for temp in qq_tech_list:
    index='article_tech'
    doc_type='tech_qq'
    doc_id='qq_'+temp['id']
    ##esclient.update
    response = esclient.index(
        index=index,
        doc_type=doc_type,
        id=doc_id,
        body=temp
    )
    print("save one id="+doc_id)
