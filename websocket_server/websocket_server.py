from geventwebsocket import WebSocketServer, WebSocketApplication, Resource
from collections import OrderedDict
import time
import json
import redis

class EchoApplication(WebSocketApplication):
    def insertRedis(self, keyName, jsonStr):
        self.r.zadd("mydata",keyName, jsonStr)

    def on_open(self):
        print("Connection opened")
        #这里要这样写
        self.pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
        self.r = redis.StrictRedis(connection_pool=self.pool)


    def on_message(self, message):
    	# 最后一个None关闭控制包，服务端将None发送给已经关闭的客户端将会抛出异常
        if message is not None:
        	#print('********'+str(message))
        	#self.ws.send(message)
            #json对象实质就是str
        	machine_data = json.loads(message)
        	#if(self.r.zremrangebyscore("mydata",machine_data[''])):
        	self.r.zremrangebyscore("mydata",machine_data["ID"],machine_data["ID"])
        	self.insertRedis(machine_data["ID"], message)


    def on_close(self, reason):
        print(reason)
        self.ws.close()

WebSocketServer(
    ('0.0.0.0', 8000),
    Resource(OrderedDict([('/', EchoApplication)]))
).serve_forever()