import www.orm
from www.models import User, Blog, Comment
import asyncio,sys
import pymysql
import aiomysql


loop=asyncio.get_event_loop()

async def test():
        await www.orm.create_pool(loop=loop, user='root', password='123654', db='testdb')
        new_user=User(id = 4, name='std', email = '10010@163.com', password='123456')
        await new_user.save()
        r = await User.findAll()
        print(r)

async def test2():
    conn = pymysql.connect(user='root', password='123654',db='testdb')
    cur = conn.cursor()
    print(cur)
loop.run_until_complete(test())
www.orm.__pool.close()
loop.run_until_complete(www.orm.__pool.wait_closed())
loop.close()

