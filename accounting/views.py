from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return  render(request, 'accounting/index.html')
def login(request):
    return  render(request, 'accounting/login.html')