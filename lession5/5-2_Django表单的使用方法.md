<!--
 * @Author: your name
 * @Date: 2021-06-24 15:26:32
 * @LastEditTime: 2021-06-24 15:45:17
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \django-lession\lession5\5-2_Django表单的使用方法.md
-->
# Django表单的使用方法  

## 处理方法  

表单只处理 get 和 post  
在get中，实例化表单对象，将form表单渲染到模版  
在post中，实例化表单对象，并将request.POST对象传给表单  

Get ->  form = Auth()  
Post -> form = Auth(request.POST)，通过is_valid() 对数据进行验证，当验证通过后，可以通过 cleaned_data[subject]获取输入的值  


