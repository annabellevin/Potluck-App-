from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpRequest 
from . import models
from django.http import JsonResponse
import requests
import json


@csrf_exempt
def addtodb(request):
    for key, value in request.POST.items():
        if key == 'item':
            dish = value
        if key == 'val':
            qty = value
    print(dish+ qty)
    potluck = models.PotluckData(dish=dish, qty=qty, takenby='Me')
    potluck.save()
    return HttpResponse("Function worked")

@csrf_exempt
def removefromdb(request):
    for key, value in request.POST.items():
        if key == 'torem1':
            rem1 = value
    print(rem1)
    itemtoremove = models.PotluckData.objects.get(dish=rem1)
    itemtoremove.delete()
    return HttpResponse("Function worked")

@csrf_exempt
def build_url(page):
    return "http://127.0.0.1:8000/home/" + page

@csrf_exempt
def loadfromdb(request):
    allentries = list()
    items = models.PotluckData.objects.all()
    for i in items:
        print(i.dish)
        allentries.extend([i.dish, i.qty, i.takenby])
    print(allentries)
    post_data = json.dumps(allentries)
    response = requests.post(build_url('/loadfromdb'), data=post_data)
    return HttpResponse("Test")