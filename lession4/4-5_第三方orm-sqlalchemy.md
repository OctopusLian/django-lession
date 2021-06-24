<!--
 * @Author: your name
 * @Date: 2021-06-24 10:23:58
 * @LastEditTime: 2021-06-24 11:13:39
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \django-lession\lession4\4-5_第三方orm-sqlalchemy.md
-->
# 第三方orm sqlalchemy  

## 什么是sqlalchemy  

SQLAlchemy 是Python 社区最知名的 ORM 工具之一，为高效和高性能的数据库访问设计，实现了完整的企业级持久模型。  
他可以搭配在任何一个python的web框架上，其中比较出名的是 flask  

## 同步数据库方法  

```
Base = declarative_base()  ->实例化base模块
engine = create_engine(‘mysql+pymysql://root:@localhost:3306/sqlalchemy_test’)  -> 链接数据库引擎
Base.metadata.create_all(engine)
所有的模型需要在create_all 目录下被引用
```
## 依赖  

```
Pip install sqlalchemy
Pip install pymysql

```

