from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse



# Create your views here.
def registerform(request):
    tfo=TopicForm()
    wfo=WebpageForm()
    afo=AccessForm()
    d={'tfo':tfo,'wfo':wfo,'afo':afo}
    if request.method=='POST' and request.FILES:
        tfd=TopicForm(request.POST)
        wfd=WebpageForm(request.POST)
        afd=AccessForm(request.POST)
        if tfd.is_valid() and wfd.is_valid() and afd.is_valid():
            T=tfd.save()
            nswo=wfd.save(commit=False)
            nswo.topic_name=T
            nswo.save()
            nsao=afd.save(commit=False)
            nsao.name=nswo
            nsao.save()
            return HttpResponse('register successfully')
        else:
            return HttpResponse('Not valid')
    return render(request,'registerform.html',d)
