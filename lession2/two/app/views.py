#coding:utf-8

from django.views.generic import View
from django.http import HttpResponse

class Index(View):
    def get(self,request,name,age):
        return HttpResponse('hello django2!!! i am {0},age is {1}'.format(name,age))

def index(request,name,age):

    return HttpResponse('hello django2!!! i am {0},age is {1}'.format(name,age))