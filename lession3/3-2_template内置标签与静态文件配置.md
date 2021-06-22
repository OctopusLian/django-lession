<!--
 * @Author: your name
 * @Date: 2021-06-17 16:56:34
 * @LastEditTime: 2021-06-22 13:44:34
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \django-lession\lession3\3-2_template内置标签与静态文件配置.md
-->
# template内置标签与静态文件配置

## 变量与标签  

变量用 {{}} 双大括号包裹 比如我们后端渲染过来的数据，用双大括号来包裹  例如 {{name}}  
内置标签类型，用 {% %} 大括号 左右各一个百分号包裹  

## 内置标签  


## for标签模版  

## 静态文件配置  

项目根目录创建 ‘static’ 与 ‘templates’文件夹同级  
```py
STATICFILES_DIRS = (os.path.join(BASE_DIR, ‘static’), )  
```


