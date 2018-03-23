# coding: utf-8
from django.shortcuts import render, render_to_response
# from django.http import HttpResponse
from .models import Accounts

# Create your views here.


# 处理登录界面请求
def login(request):
    request.encoding = 'utf-8'
    context = {}
    error_msg = ''
    if request.method == "POST":
        email = request.POST['account_email']
        psd = request.POST['account_password']
        try:
            account_id = Accounts.objects.get(email=email)
            if account_id and account_id.password == psd:
                # 跳转到系统主页
                context['account'] = account_id
                return render(request, 'base.html', context=context)
            else:
                # 用户密码不匹配
                error_msg = '用户邮箱或密码错误！'
        except Accounts.DoesNotExist:
            error_msg = '用户不存在！请注册后重试！'

    context['error_msg'] = error_msg
    return render(request, 'accounts/index2.html', context=context)


# 处理用户注册请求
def register(request):
    context = {}
    error_msg = ''
    if request.method == 'POST':
        user_name = request.POST['account_name']
        email = request.POST['account_email']
        psd = request.POST['account_password']
        psd2 = request.POST['account_password2']
        try:
            Accounts.objects.get(email=email)
            # 如果没有查找到数据，会报 DoesNotExist 错误
            error_msg = '该邮箱已被使用！请重新输入！'
        except Accounts.DoesNotExist:
            # 判断两次密码是否一致
            if psd == psd2:
                Accounts(name=user_name, email=email, password=psd).save()
                return render(request, 'accounts/index2.html', context=context)
            else:
                error_msg = '两次输入的密码不匹配！'

    context['error_msg'] = error_msg
    return render(request, 'accounts/sign-up2.html', context=context)


# 找回密码前邮箱确认请求处理
def email_confirm(request):
    context = {}
    error_msg = ''
    if request.method == 'POST':
        email = request.POST['account_email']
        try:
            account_id = Accounts.objects.get(email=email)
            context['account_email'] = account_id.email
            return render(request, 'accounts/passwordmodify.html', context=context)
        except Accounts.DoesNotExist:
            error_msg = '该邮箱未注册！请确认后重试！'

    context['error_msg'] = error_msg
    return render(request, 'accounts/forgot2.html', context=context)


# 密码修改请求处理
def password_modify(request):
    context = {}
    error_msg = ''
    if request.method == 'POST':
        email = request.POST['account_email']
        psd = request.POST['account_password']
        psd2 = request.POST['account_password2']
        account_id = Accounts.objects.get(email=email)
        # 判断两次密码是否一致
        if psd == psd2:
            account_id.password = psd
            account_id.save()
            context['account'] = account_id
            return render(request, 'accounts/login.html', context=context)
        else:
            error_msg = '两次输入的密码不一致！请重新输入！'

    context['error_msg'] = error_msg
    return render(request, 'accounts/passwordmodify.html', context=context)
