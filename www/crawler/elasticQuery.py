from elasticsearch import Elasticsearch

esclient = Elasticsearch(['localhost:9200'])

# _index_mappings = {
#   "mappings": {
#     "tech_qq": {
#       "properties": {
#         "title":{"type":"keyword"},
#         "id":{"type":"keyword"},
#         "context":{"type":"text"},
#         "tags":{"type":"keyword"},
#         "keywords":{"type":"keyword"}
#
#       }
#     }
#   }
# }
# if esclient.indices.exists(index='article_tech') is not True:
#     esclient.indices.create(index='article_tech',body=_index_mappings)


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
response = esclient.search(index='article_tech',body=body)

top_recodes = response['hits']['hits']

for recode in top_recodes:
    print(recode['_source']['context'])
    print(recode['_source']['keywords'])



