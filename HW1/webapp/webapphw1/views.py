from django.shortcuts import render#_to_response
#from django.template import RequestContext
from django.http import HttpResponse
from .models import InputForm
from webapphw1.calculate import calc
import os

def index(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = calc(form2.a, form2.b, form2.c)
            result = result.replace('static/', '')
    else:
        form = InputForm()

    return render(request,'calculate.html',context = {'form': form,'result': result})

