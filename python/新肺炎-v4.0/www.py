__author__ = '未昔'
__date__ = '2018/11/21 19:47'




from application import app
from web.controllers.index import route_index  # 注册首页路由
from web.controllers.static import route_static  # 注册静态文件

app.config['JSON_AS_ASCII'] = False

app.register_blueprint( route_index, url_prefix="/")# 将路由注入进来

app.register_blueprint( route_static, url_prefix="/static") # 所有的route_static，前缀都是 static，都转移到static.py控制器下面统一处理

