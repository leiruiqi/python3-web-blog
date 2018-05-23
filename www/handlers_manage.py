

import re, time, json, logging, hashlib, base64, asyncio,markdown2
from coroweb import get, post
from apis import Page,APIError,APIValueError,APIPermissionError,APIResourceNotFoundError
from bizauth import COOKIE_NAME,user2cookie,_RE_EMAIL,_RE_SHA1,check_admin
from utils import get_page_index
from models import User,Blog,Comment,Category, next_id
from aiohttp import web
from config import categorys

@get('/manage/blogs')
def manage_blogs(*, page='1'):
    return {
        '__template__': 'manage_blogs.html',
        'page_index': get_page_index(page)
    }



@get('/manage/blogs/create')
def manage_create_blog():
    ##categorys = categorys
    return {
        '__template__': 'manage_blog_edit.html',
        'id': '',
        'action': '/api/blogs',
        'categorys':categorys
    }

@get('/manage/blogs/edit')
def manage_edit_blog(*, id):
    return {
        '__template__': 'manage_blog_edit.html',
        'id': id,
        'action': '/api/blogs/%s' % id,
        'categorys': categorys
    }

@get('/api/blogs/{id}')
async def api_get_blog(*, id):
    blog = await Blog.find(id)
    return blog

@post('/api/blogs')
async def api_create_blog(request, *, name, summary, content,category_id):
    check_admin(request)
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty.')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty.')
    if not category_id or not category_id.strip():
        raise APIValueError('category_id', 'category_id cannot be empty.')
    blog = Blog(user_id=request.__user__.id, user_name=request.__user__.name, user_image=request.__user__.image, name=name.strip(), summary=summary.strip(), content=content.strip(),category_id=category_id.strip())
    await blog.save()
    return blog


@post('/api/blogs/{id}')
async def api_edit_blog(request, *, id,name, summary, content,category_id):
    check_admin(request)
    oldblog = await Blog.find(id)
    if not oldblog:
        raise APIValueError('id', 'id cannot be effect.')
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty.')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty.')
    if not category_id or not category_id.strip():
        raise APIValueError('category_id', 'category_id cannot be empty.')
    blog = Blog(id=id,user_id=request.__user__.id, user_name=request.__user__.name, user_image=request.__user__.image,
                name=name.strip(), summary=summary.strip(), content=content.strip(), category_id=category_id.strip(),created_at=oldblog.created_at)
    await blog.update()
    return blog
