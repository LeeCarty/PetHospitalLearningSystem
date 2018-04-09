
from django.shortcuts import render, render_to_response
# from django.http import HttpResponse
from .models import Case
import os
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
    case = Case.objects.get(name=name)
    context['name'] = case.name
    context['desc'] = case.desc
    context['image'] = case.img
    return render(request, 'case/study_02.html', context=context)

