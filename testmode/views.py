# coding: utf-8
from django.shortcuts import render
from .models import DiseaseType, DiseaseSmallType, Tag, TestPaper, PaperQuestions, UserTestRecords

# Create your views here.


# 进入测试 请求处理  路由： '/test_type'
def test_type(request):
    context = {}
    return render(request, 'testmode/testtype.html', context=context)


# 测试管理 请求处理  路由： '/test_manage'
def test_manage(request):
    context = {}

    return render(request, 'testmode/testManage.html', context=context)


# 病例选择 请求处理 路由： '/test_choice'
def test_choice(request, type_id):
    context = {}
    search_key = ''
    if type_id == 1:
        search_key = 'type_1'
    if type_id == 2:
        search_key = 'type_2'
    if type_id == 3:
        search_key = 'type_3'
    if type_id == 4:
        search_key = 'type_4'
    if type_id == 5:
        search_key = 'type_5'
    if type_id == 6:
        search_key = 'type_6'

    import pdb
    pdb.set_trace()

    paper_list = TestPaper.objects.filter(disease_type_id=search_key)
    context['paper_list'] = paper_list

    return render(request, 'testmode/testChoice.html', context=context)
