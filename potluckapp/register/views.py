from django.shortcuts import render

from django.template.loader import get_template

from django.http import HttpResponse
import datetime

def index(request):
   # now = datetime.datetime.now()
    t = get_template('register.html')
    html = t.render()
    return HttpResponse(html)

    #return HttpResponse("Hello, world. You're at the register page.")