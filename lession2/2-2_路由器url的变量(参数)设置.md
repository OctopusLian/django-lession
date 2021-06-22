<!--
 * @Author: your name
 * @Date: 2021-06-17 15:19:26
 * @LastEditTime: 2021-06-17 16:16:17
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \django-lession\src\lession2\2-2_路由器url的变量(参数)设置.md
-->
# 路由器url的变量(参数)设置

## url中的参数  

在url后边用?开始，键与值用等号连接，每对键值用&号区分，如: http://127.0.0.1:8000/app?name=dewei&age=30

在路由的参数中用分隔符分开，如: http://127.0.0.1:8000/app/dewei/30

## django2的url变量类型  

字符串类型：匹配任何非空字符串，但不包含斜杠，在不指定类型的前提下，默认字符串类型 <str:name>
整型：匹配0和正整数 <int:age>
slug:   可理解为注释，后缀或附属等概念 <slug: day>
uuid：匹配一个uuid格式的对象 <uuid: uid> 类似xxx-xx-xx

## 支持url类型的方法

from django.urls import path 2.0以后新方法

from django.conf.urls import url 2.0以前方法，不支持参数中的类型，只能通过正则表达的方式进行基本的匹配

## 为url设置别名

path(‘add’, view_function, name=’add’) 

别名可以在重定向和模版定义的时候直接用别名替代，具体使用方法会在template模版课程中具体讲解

## 视图读取参数

?形式的参数 -> request.GET.get(参数名)
以分隔符形式的参数

def index(request, 参数名, 参数名):
           print(参数名)
