#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Ricky Lei'

import search.search_common as search_common

index='article_tech'
doc_type='tech_qq'



async def getById(id):
    body ={
        "query": {
            "term": {"id": id}
        }
    }
    result = await search_common.search(index,doc_type,body)

    if(len(result)==0):
        return None
    else:
        return result[0]

async def getByIds(ids):
    body = {
        "query": {
            "terms": {
                "id": id
            }
        }
    }
    result = await search_common.search(index,doc_type,body)
    return result


async def searchAll4Page(fromid,pageSize=5):
    query = None
    if fromid is not None and fromid >0:
        query= {
            "range": {
                "id": {
                    "lt":"1"
                }
            }
        }

    body ={
        "sort": [
            {"id": {"order": "desc"}}
        ],

        "size":5
    }

    if query:
        body.setdefault("query", query)

    result = await search_common.search(index,doc_type,body)
    return result


