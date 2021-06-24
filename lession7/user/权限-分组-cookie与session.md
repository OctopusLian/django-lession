<!--
 * @Author: your name
 * @Date: 2021-06-24 15:41:53
 * @LastEditTime: 2021-06-24 15:42:38
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \django-lession\lession7\user\权限-分组-cookie与session.md
-->
# 权限，分组 cookie与session

## 权限permission  

权限是指为了保证职责的有效履行，任职者必须具备的，对某事项进行决策的范围和程度  
权限与用户是一种多对多的关系  

## Cookies  

指某些网站为了辨别用户身份、进行 session 跟踪而储存在用户本地终端上的数据  
我们的http协议是一种无状态的连接，当请求结束后，下一次在请求，服务并不知道是否和上一次的请求是同一台机器或人，所以为了保证确认每次请求的都是谁，就通过cookie进行在浏览器端的保存，每次请求，服务端通过获取浏览器上的cookie确认来访者是谁  
cookie的存储方式 是类似字典的方式 以key value的形式存储，不同的服务会存储在浏览器端不同的域名下  

## session  

使用情景与cookie相同，但不同的是，session的值存在服务器端，而通过在浏览器端存储一个cookie（cookie中存储一个能对应服务器端session的value）而达到获取制定session值的目的
