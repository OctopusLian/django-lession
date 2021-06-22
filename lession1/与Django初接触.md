<!--
 * @Author: your name
 * @Date: 2021-06-17 14:54:24
 * @LastEditTime: 2021-06-17 15:12:32
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \django-lession\doc\与Django初接触.md
-->
## Django介绍  

- Django是一个开源的Web应用框架，
- 由Python编写，他拥有者非常齐备的官方文档，
- 提供一站式的解决方案，包括缓存，数据ORM，后台管理，验证，表单处理等多项功能，
- 它可以快速搭建高性能的优雅的网站

### Django中的模块  

- 模型 Model：数据层，处理与数据相关的所有事物
- 视图 View：视图层，用来处理用户发出的请求
- 模版 Template：模版层，通过视图函数渲染html模版，得到动态的前端页面
- 路由 Url： 网站的入口，关联到对应的视图函数，访问网址就对应一个函数
- 表单 Forms：表单，用在在浏览器输入数据提交，并对这些数据进行验证。
- 后台 Admin： Django自带一个管理后台，对你提交的数据进行管理
- 配置 Settings：Django的设置，配置文件。

### Django的基础命令  

django-admin startproject 项目名->创建一个django项目
python manage.py startapp 应用名->项目中创建一个应用
Python manage.py shell -> 进入调试代码的调试模式
python manage.py makemigrations -> 数据库创建更改文件
python manage.py migrate -> 同步到数据库进行更新
python manage.py flush -> 清空数据库
python manage.py runserver 0.0.0.0:8000 -> 启动开发服务器
python manage.py + 回车 可查看更多命令
