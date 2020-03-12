__author__ = '未昔'
__date__ = '2018/11/21 18:56'
# 基础配置（公用）
DEBUG = True
SERVER_PORT = 8999  # 运行端口
SQLALCHEMY_ECHO = False   # base 里面默认都是false

AUTH_COOKIE_NAME = "yl_news"

PAGE_SIZE = 5 # 分页每页的大小
PAGE_DISPLAY = 10 # 展示多少页


IGNORE_URLS = [
    "^/user/login",
]

IGNORE_CHECK_LOGIN_URLS = [  # 完全不需要判断的
    "^/static",
    "^/favicon.ico"
]