import redis
rc = redis.Redis(host = '127.0.0.1')
ps = rc.pubsub()
ps.subscribe(['sub1', 'sub2'])
while True:
    input = raw_input("publish:")
    if input == 'over':
        print '停止发布'
    rc.publish('sub1', input)
    rc.publish('sub2', input)

import redis
rc = redis.Redis(host = '127.0.0.1')
ps = rc.pubsub()
ps.subscribe(['sub1', 'sub2'])
for item in ps.listen():
    if item['type'] == 'message':
        data = item['data']
    if item['data'] == 'over':
        ps.unsubscribe('sub1')
        print ‘sub1已取消订阅’