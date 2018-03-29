# coding: utf-8
from django.shortcuts import render

# Create your views here.


# 进入测试 请求处理  路由： '/testmode'
def testmode(request):
    context = ''

    return render(request, 'testmode/main.html', context=context)
