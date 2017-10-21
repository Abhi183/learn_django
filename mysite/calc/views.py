from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here:
def add(request):
    url_params = request.GET
    first_num = url_params['x']
    second_num = url_params['y']
    result = float(first_num) + float(second_num)
    result = {"Add_Result":result}
    return JsonResponse(result)
def multi(request):
    url_params = request.GET
    first_num = url_params['x']
    second_num = url_params['y']
    result = float(first_num) * float(second_num)
    result = {"multi_Result":result}
    return JsonResponse(result)

