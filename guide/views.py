from django.shortcuts import render

# Create your views here.


# ҽԺ����  ����  ·�ɣ� '/guide'
def guide(request):
    context = {}
    return render(request, 'guide/guide.html', context=context)
