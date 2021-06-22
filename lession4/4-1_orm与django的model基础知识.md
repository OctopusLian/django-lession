<!--
 * @Author: your name
 * @Date: 2021-06-21 13:49:42
 * @LastEditTime: 2021-06-22 18:06:38
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \django-lession\lession4\4-1_orm与django的model基础知识.md
-->
# orm与django的model基础知识  

## 什么是orm  

全称：object relational mapping，通过使用它，我们可以直接使用python的方法去使用数据库。  

通过把表映射成类，把行作为实例，把字段作为属性，orm在执行对象操作的时候会把对应的操作转换成数据库原生语句的方式来完成数据库开发工作  

## orm的优点  

使用简单，通过将数据库语法进行封装，直接使用方法即可操作数据库  

性能好，在通过orm转换成sql的时候是会有一些消耗，但这个消耗其实非常低，在对整体业务提升的角度说，这点消耗可以忽略不计，除非你对于io操作的要求非常的极端。  

兼容性好，支持目前市面上多数的关系型数据库，如mysql prestresql salite等  

## django的orm  

django中虚拟对象数据库也叫模型，通过模型实现对目标数据库的读写进行操作，实现如下：  

- 在settings.py 中设置数据库信息（需提前在数据库中创建库）  
- 在应用app的models.py中以类的形式定义模型  
- 通过模型在目标数据库中创建对应的表  
- 在视图函数中通过对模型的操作实现目标数据库的读写操作  

## settings中的数据库配置  


## models层的书写  

## 同步数据库  

Python mange.py makemigrateions 在migrate文件夹下生成 initialpy脚本文件  
Python manage.py migrate 将initialpy脚本中的代码执行，生成相对应的数据表  
