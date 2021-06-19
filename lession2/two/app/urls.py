#coding:utf-8

from django.urls import path
from .views import Index # 当前路径下有个views

urlpatterns = [
    path('<str:name>/<int:age>',Index.as_view(),name='index')
]