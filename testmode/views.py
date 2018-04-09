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

    paper_list = TestPaper.objects.filter(disease_type_id=search_id)
    context['paper_list'] = paper_list

    return render(request, 'testmode/paperChoice.html', context=context)


# 试卷检索  请求处理  路由： '/test_choice/<search_key>'
def paper_search(request, search_key):
    context = {}
    search_key = request.POST['search_key']
    import pdb
    pdb.set_trace()

    # TestPaperList  仅支持试卷名检索
    paper_list = TestPaper.objects.filter(Q(name__contains=search_key))

    # # disease_type_id.name
    # dt_list = DiseaseType.objects.filter(Q(name__contains=search_key))
    #
    # # disease_small_type_id.name
    # dst_list = DiseaseSmallType.objects.filter(Q(name__contains=search_key))
    #
    # # tags.name
    # tag_list = Tag.objects.filter(Q(name__contains=search_key))

    context['paper_list'] = paper_list
    return render(request, 'testmode/paperChoice.html', context=context)


# 试卷内容 请求处理  路由： '/test_paper/<id>'
def test_paper(request, paper_id):
    context = {}
    question_list = PaperQuestions.objects.filter(paper_id=paper_id).order_by('id')
    context['question_list'] = question_list
    return render(request, 'testmode/test.html', context=context)


# 试卷提交 请求处理   路由： '/test_paper/paper_submit'
def paper_submit(request):
    context = {}
    grade = 0
    for i in range(1, 1000):
        if str(i) in request.POST.keys():
            answer = request.POST[str(i)]
            question_obj = PaperQuestions.objects.filter(id=i, answer=answer)
            if question_obj:
                grade += 1
    grade *= 5

    return render(request, 'testmode/testManage.html', context=context)
