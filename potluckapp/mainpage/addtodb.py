from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpRequest 


@csrf_exempt
def addtodb(request):
    for key, value in request.POST.items():
        if key == 'item':
            dish = value
        if key == 'val':
            qty = value
    print(dish+ qty)
    return HttpResponse("Function worked")