
import asyncio
import orm,orm2
from models import User, Blog, Comment

loop = asyncio.get_event_loop()
async def test():
    await orm.create_pool(user='test', password='test', db='test',loop=loop)

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()

@asyncio.coroutine
def saveTest():
    yield from orm2.create_pool(user='test', password='test', db='test',loop=loop)

    blog = Blog(user_id='001522336605062f401924424d04c0c8106090a3ae87693000', user_name='雷瑞奇', user_image='',
                name='一个好人', summary='这世界变化快', content='不是我不懂，这世界变化快')
    yield from blog.save()

loop.run_until_complete(saveTest())