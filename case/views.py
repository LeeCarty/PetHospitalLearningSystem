
from django.shortcuts import render, render_to_response
# from django.http import HttpResponse
from .models import Case
import base64
# Create your views here.

def list(request):
    import pdb
    pdb.set_trace()
    request.encoding = 'utf-8'
    context = {'desc':'dsflsalfjdlsafjsldncnfefonfrlsanfvlsdnvnnefnwqlgfnsldanlsnvlenronasnb'}
    list = []
    list.insert(context)
    ids = Case.objects.get(id != 0)
    for i in (0, len(ids)):
        desc = Case.objects.get(id = ids[i])
        list[i].insert({'id':ids[i],'desc':desc})

    return render(request, 'case/list.html', context=context)

def choosecase(request):
    context = {}

    cases1 = Case.objects.filter(belongs='1') or []
    cases2 = Case.objects.filter(belongs='2') or []
    cases3 = Case.objects.filter(belongs='3') or []
    cases4 = Case.objects.filter(belongs='4') or []
    cases5 = Case.objects.filter(belongs='5') or []
    cases6 = Case.objects.filter(belongs='6') or []

    context['cases1'] = cases1
    context['cases2'] = cases2
    context['cases3'] = cases3
    context['cases4'] = cases4
    context['cases5'] = cases5
    context['cases6'] = cases6


    return render(request, 'case/choosecase.html', context=context)


def study_02(request, name):
    context = {}
    case = Case.objects.get(name = name)
    context['name'] = case.name
    context['desc'] = case.desc
    context['imgcode'] = base64.b64encode(case.img.read())
    return render(request, 'case/study_02.html', context=context)

def study_01(request, name):
    context = {}
    content = ''
    if name == '前台':
        content = '前台主要负责客户来访与登记，接听客户电话，接受客户询问、预定等事务，引导客户了解宠物医院主要服务'
    elif name == '医助':
        content = '''医助负责注射工作包括：静脉注射、皮下注射、肌肉注射、局部封闭注射的操作流程，常见问题的处理方法，输液泵、加热垫的使用方法，注射室的消毒流程。 \n
                   医助负责手术前准备工作包括：术前对宠物进行麻前给药、注射麻醉、吸入麻醉的流程，保定、剃毛、消毒的流程，常见手术器械的介绍，手术器械包的准备、灭菌流程，手术人员的消毒、穿戴手术衣流程等。'''
    elif name == '兽医':
        content = '兽医负责手术工作包括：手术无菌要求，常规手术、特殊手等的操作规范，进入虚拟宠物医院，点击手术操作台，可以进行相关操作。'
    context['content'] = content
    context['name'] = name

    return render(request, 'case/study_01.html', context=context)

def choosecareer(request):
    context = {}
    return render(request, 'case/choosecareer.html', context=context)

