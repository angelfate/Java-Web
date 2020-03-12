__author__ = '未昔'
__date__ = '2018/11/27 10:35'

from flask import render_template,g
import datetime



def ops_render( context = {}):
    return  render_template( **context )



def getCurrentData( format = "%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.now().strftime( format )


'''
根据某个字段获取一个dic出来
'''
def getDictFilterField( db_model,select_filed,key_field,id_list ):  # 数据表。希望查询的字段。希望作为字典里面key的字段。希望的字段值
    ret = {}
    query = db_model.query
    if id_list and len( id_list ) > 0:
        query = query.filter( select_filed.in_( id_list ) )

    list = query.all()
    if not list:
        return ret
    for item in list:
        if not hasattr( item,key_field ):
            break

        ret[ getattr( item,key_field ) ] = item
    return ret

"""
    从一个对象里面取出结果
"""
def selectFilterObj( obj,field ):
    ret = []
    for item in obj:
        if not hasattr(item, field ):
            break
        if getattr( item,field )  in ret:
            continue
        ret.append( getattr( item,field ) ) # 添加结果，统一返回
    return ret

