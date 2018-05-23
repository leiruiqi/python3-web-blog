
import asyncio, logging

from elasticsearch import Elasticsearch
esclient = Elasticsearch(['localhost:9200'])

index='article_tech'
doc_type='tech_qq'
body={
    "query": {
        "match":{
            ##"keywords":['人工智能', '机器', '性能', '精度', '推动']
            ##"keywords":['硬件', '神经网络', '深度', '学习', '运算', '发展', '提高']
            "context":'神经网络'
        }
    }
}
body2 ={
        "query": {
            "term": {
                "_id": 'qq_20180128009567'
            }
        }
    }

id=['20180128009567','20180128009309']
body3={
    "query":{
        "terms":{
            "id":id
        }
    }
}

body4 ={
        "sort": [
            {"_id": {"order": "desc"}}
        ],
        "query":{
            "range": {
                "id": {
                    "lt":"qq_20180128009309",

                }
            }
        },
        "size":5
    }

response = esclient.search(index=index,doc_type=doc_type,body=body4)
##print(response)
top_recodes = response['hits']['hits']

for recode in top_recodes:
    print(recode['_source']['id'])
    ##print(recode['_source']['keywords'])