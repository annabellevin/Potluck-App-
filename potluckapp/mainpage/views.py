from django.shortcuts import render

from django.template.loader import get_template

from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    t = get_template('curtime.html')
    html = t.render({'current_date': now})
    return HttpResponse(html)

    #return HttpResponse("Hello, world. You're at the main page.")
