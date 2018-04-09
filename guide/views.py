from django.shortcuts import render

# Create your views here.


# 医院导览  请求  路由： '/guide'
def guide(request):
    context = {}
    return render(request, 'guide/guide.html', context=context)
