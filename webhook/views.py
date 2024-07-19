from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def home(request):
    return HttpResponse("\U0001F499")

def webhook(request):
    response = request.Post()
    message = response.json()
    print(message)
    return JsonResponse(message)