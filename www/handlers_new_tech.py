#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Ricky Lei'

import markdown2
from coroweb import get, post
from apis import Page,APIError,APIValueError,APIPermissionError,APIResourceNotFoundError
from utils import get_page_index
from search import search_article_tech


@get('/new_tech')
async def index(*,page='1',category='1'):
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
    page_index = get_page_index(page)
    num = await Blog.findNumber('count(id)','category_id='+category)
    page = Page(num,page_index)

    if num == 0:
        blogs = []
    else:
        blogs = await search_article_tech.getById()
    return {
        '__template__': 'blogs.html',
        'page': page,
        'blogs': blogs
    }

def text2html(text):
    lines = map(lambda s: '<p>%s</p>' % s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'), filter(lambda s: s.strip() != '', text.split('\n')))
    return ''.join(lines)

@get('/new_tech/{id}')
async def get_blog(id):
    blog = await Blog.find(id)
    comments = await Comment.findAll('blog_id=?', [id], orderBy='created_at desc')
    for c in comments:
        c.html_content = text2html(c.content)
    blog.html_content = markdown2.markdown(blog.content)
    return {
        '__template__': 'blog.html',
        'blog': blog,
        'comments': comments
    }




@get('/api/new_tech')
async def api_blogs(*, page='1'):
    page_index = get_page_index(page)
    num = await Blog.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, blogs=())
    blogs = await Blog.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    return dict(page=p, blogs=blogs)