#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Ricky Lei'

import markdown2
from coroweb import get, post
from apis import Page,APIError,APIValueError,APIPermissionError,APIResourceNotFoundError
from utils import get_page_index
from search import search_article_tech


@get('/new_tech')
async def index(*,fromId=None,pageSize=10):
    # summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    # blogs = [
    #     Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
    #     Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
    #     Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
    # ]
    # return {
    #     '__template__': 'blogs.html',
    #     'blogs': blogs
    # }
    #page_index = get_page_index(page)


    news = await search_article_tech.searchAll4Page(fromId=fromId,pageSize=pageSize)
    return {
        '__template__': 'news.html',
        'news': news
    }

def text2html(text):
    lines = map(lambda s: '<p>%s</p>' % s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'), filter(lambda s: s.strip() != '', text.split('\n')))
    return ''.join(lines)

@get('/new_tech/{id}')
async def get_new(id):
    new = await search_article_tech.getById(id)

    return {
        '__template__': 'new.html',
        'new': new,
    }




@get('/api/new_tech')
async def api_news(*,fromId=20190128009309,pageSize=10):

    news = await search_article_tech.searchAll4Page(fromId)
    return news