<!--
 * @Author: your name
 * @Date: 2021-06-17 16:39:39
 * @LastEditTime: 2021-06-17 16:56:25
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \django-lession\lession3\3-1_template介绍配置与view的绑定.md
-->
# template介绍，配置，与view的绑定

## Template模版

模版可以动态生成html网页，它包括部分html代码和一些特殊的语法

## template配置方法

一般template模版存放在“templates”目录中
通过在项目settings的TEMPLATES的 DIRS 列表中添加对应的路径即可，如：os.path.join(BASE_DIR, ‘templates’) 

## template与视图的绑定

通过 from django.shortcuts import render 模块
return render(request, template_path, {k:v})   字典中的 key 和 value 就是要向前端渲染出的数据

## Template展示渲染的数据

在html中 以{{}} 为标示，在双大括号中传入视图中传入的数据
