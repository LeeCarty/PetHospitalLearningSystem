# coding: utf-8
from django.shortcuts import render, get_object_or_404
from .models import DiseaseType, DiseaseSmallType, Tag, TestPaper, PaperQuestions, UserTestRecords
from accounts.models import Accounts
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.


# 进入测试 请求处理  路由： '/test_type'
def test_type(request):
    context = {}
    return render(request, 'testmode/testtype.html', context=context)


# 测试管理 请求处理  路由： '/test_manage'
def test_manage(request):
    context = {}
    utr_list = UserTestRecords.objects.all().order_by('-finish_time')
    context['utr_list'] = utr_list
    return render(request, 'testmode/testManage.html', context=context)


# 病例选择 请求处理 路由： '/test_choice'
def test_choice(request, type_id):
    context = {}
    search_id = int(type_id)

    paper_list = TestPaper.objects.filter(disease_type_id=search_id)
    context['paper_list'] = paper_list

    return render(request, 'testmode/paperChoice.html', context=context)


# 试卷检索  请求处理  路由： '/test_choice/<search_key>'
def paper_search(request, search_key):
    context = {}
    search_key = request.POST['search_key']

    # TestPaperList  仅支持试卷名检索
    paper_list = TestPaper.objects.filter(Q(name__contains=search_key))

    context['paper_list'] = paper_list
    return render(request, 'testmode/paperChoice.html', context=context)


# 试卷内容 请求处理  路由： '/test_paper/<id>'
def test_paper(request, paper_id):
    context = {}

    question_list = PaperQuestions.objects.filter(paper_id=paper_id).order_by('id')
    paper_obj = TestPaper.objects.get(id=paper_id)

    context['question_list'] = question_list
    context['paper_obj'] = paper_obj

    return render(request, 'testmode/test.html', context=context)


# 试卷提交 请求处理   路由： '/test_paper/paper_submit'
def paper_submit(request):
    context = {}
    grade = 0

    paper_odj = TestPaper.objects.get(name=request.POST['paper_name'])
    question_list = PaperQuestions.objects.filter(paper_id=paper_odj.id).order_by('id')
    for item in question_list:
        answer_id = str(item.id)
        try:
            get_answer = request.POST[answer_id]
        except MultiValueDictKeyError:
            continue
        if item.answer.upper() == get_answer:
            grade += 1

    grade *= 5
    tips = ''
    if grade >= 80:
        tips = 'Good Job!'
    elif grade >= 60:
        tips = 'Keep Trying!'
    else:
        tips = 'Work Harder!'

    # import pdb
    # pdb.set_trace()

    user_odj = Accounts.objects.get(email='111111@qq.com')

    UserTestRecords(user_id=user_odj, paper_id=paper_odj, grade=grade, tips=tips).save()
    utr_list = UserTestRecords.objects.all().order_by('-finish_time')
    context['utr_list'] = utr_list

    return render(request, 'testmode/testManage.html', context=context)
