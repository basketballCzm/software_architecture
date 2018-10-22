# software_architecture
软件体系结构大作业

# websocket server
websocket server采用gevent,python的一个网络库https://github.com/jgelens/gevent-websocket，使用上面的例子。

# websocket client
websocket client采用websocket-client,要使用pip install websocket-client来安装该库 
threadpool: pip install threadpool

# 错误记录
1. python从redis里面取出的单个数据为byte，要手动转化为字典类型。网上说json格式要使用json.dumps(jsonType)，转化为了字符串，然后才能提交给前端，直接提交bytes类型，前端不能进行解析。
2. 对于websocket改天进行总结。
