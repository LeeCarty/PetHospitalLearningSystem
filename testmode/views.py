# coding: utf-8
from django.shortcuts import render, get_object_or_404
from .models import DiseaseType, DiseaseSmallType, Tag, TestPaper, PaperQuestions, UserTestRecords
from django.db.models import Q

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
    search_id = int(type_id)

    import pdb
    pdb.set_trace()
    paper_list = TestPaper.objects.filter(disease_type_id=search_id)
    context['paper_list'] = paper_list

    return render(request, 'testmode/paperChoice.html', context=context)


# 试卷检索  请求处理  路由： '/test_choice/<search_key>'
def paper_search(request, search_key):
    context = {}
    search_key = request.POST['search_key']

    # # TestPaper
    # paper_list1 = TestPaper.objects.filter(Q(name__contains=search_key))
    #
    # # disease_type_id.name
    # dt_list = DiseaseType.objects.filter(Q(name__contains=search_key))
    # paper_list2 = get_paper_list(1, dt_list)
    #
    # # disease_small_type_id.name
    # dst_list = DiseaseSmallType.objects.filter(Q(name__contains=search_key))
    # paper_list3 = get_paper_list(2, dst_list)
    #
    # # tags.name
    # tag_list = Tag.objects.filter(Q(name__contains=search_key))
    # paper_list4 = get_paper_list(3, tag_list)
    #
    # def get_paper_list(tp, source_list):
    #     result_list = []
    #
    #     return result_list


    return render(request, 'testmode/paperChoice.html', context=context)


# 试卷内容 请求处理  路由： '/test_paper/<id>'
def test_paper(request, paper_id):
    context = {}
    question_list = PaperQuestions.objects.filter(paper_id=paper_id)
    context['question_list'] = question_list
    return render(request, 'testmode/test.html', context=context)


# 试卷提交 请求处理   路由： '/test_paper/paper_submit'
def paper_submit(request):
    context = {}
    import pdb
    pdb.set_trace()
    return render(request, 'testmode/testManage.html', context=context)
