__author__ = '未昔'
__date__ = '2018/11/22 12:20'
import datetime

from flask import Blueprint,request

from common.libs.Helper import ops_render,getCurrentData
from common.models.chinaTotal import Chinatotal  # 累计数据表
from common.models.chinaToday import Chinatoday  # 新增数据表
from common.models.everyday_data import EverydayDatum # 折现图数据表
from common.models.user_ip import UserIp # 存储用户信息表
from common.models.table_data import TableDatum # 表格数据
from common.models.broadcast import Broadcast # 实时播报

from application import db

route_index = Blueprint('index_page',__name__ )  # 入口文件



@route_index.route("/")
def index():
    resp_data = {}  # 空list


    # 折线图的日期，新增确诊，疑似，治愈，死亡
    every_day_list,confirm_list,suspect_list,heal_list,dead_list = [],[],[],[],[]


    # 首页 六个累计及现有数据
    resp_data['china_total'] =china_total
    resp_data['china_today'] = china_today

    # 折线图数据
    resp_data['every_day_list'] = every_day_list
    resp_data['confirm_list'] = confirm_list
    resp_data['suspect_list'] = suspect_list
    resp_data['heal_list'] = heal_list
    resp_data['dead_list'] = dead_list
    resp_data['table_data'] = table_data # 表格数据
    resp_data['len_user'] = len_user # 访问次数
    resp_data['broadcast'] = broadcast  # 实时播报

    resp_data['choice'] = 'index'  # 当前激活页面

    return ops_render('index.html',resp_data)


@route_index.route("/map")
def map():
    resp_data = {}  # 空list


    # 首页 六个累计及现有数据
    resp_data['china_total'] = china_total
    resp_data['china_today'] = china_today
    resp_data['len_user'] = len_user # 访问次数
    resp_data['table_data'] = table_data # 地图数据

    resp_data['choice'] = 'map'  # 当前激活页面

    return ops_render('china_map.html',resp_data)