# coding: utf-8
from django.shortcuts import render, render_to_response
# from django.http import HttpResponse
from .models import Accounts

# Create your views here.


# 处理登录界面请求
def login(request):
    request.encoding = 'utf-8'
    context = {}
    error_msg = ""
    if request.method == "POST":
        email = request.POST['account_email']
        psd = request.POST['account_password']
        account_id = Accounts.objects.get(email=email)
        if account_id and account_id.password == psd:
            # 跳转到系统主页
            context = {'account': account_id}
            return render(request, 'base.html', context=context)
        else:
            # 用户密码不匹配
            error_msg = '用户邮箱或密码错误！'
    context = {'error_msg': error_msg}
    return render(request, 'accounts/login.html', context=context)


# 处理用户注册请求
def register(request):
    content = {}
    error_msg = ""
    if request.method == 'POST':
        user_name = request.POST['account_name']
        email = request.POST['account_email']
        psd = request.POST['account_password']

        try:
            account_id2 = Accounts.objects.get(email=email)
            # 如果没有查找到数据，会报 DoesNotExist 错误
            error_msg = '该邮箱已被使用！请重新输入！'
        except Accounts.DoesNotExist:
            Accounts(name=user_name, email=email, password=psd).save()
            return render(request, 'accounts/login.html', context=content)

    content = {'error_msg': error_msg}
    return render(request, 'accounts/register.html', context=content)
