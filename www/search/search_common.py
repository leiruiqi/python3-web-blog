#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Ricky Lei'

import asyncio, logging

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



def log(indexType,body, params=()):
    logging.info('indexType: %s Querybody: %s',indexType , body)

async def search(index,doc_type, body, params=None):
    log(index+'/'+doc_type, body,params)

    response = esclient.search(index=index,doc_type=doc_type,body=body)

    return getHits(response)

def getHits(response):
    top_recodes = response['hits']['hits']
    return top_recodes