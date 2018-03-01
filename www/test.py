

import asyncio
from orm import Model, StringField, IntegerField,create_pool,select


class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()

#以下为测试
loop = asyncio.get_event_loop()
loop.run_until_complete(create_pool(host='127.0.0.1', port=3306,user='test', password='test',db='test', loop=loop))


rs = loop.run_until_complete(select('select * from users where id=? and name=?',(1,'ricky')))
#获取到了数据库返回的数据
print("heh:%s" % rs)