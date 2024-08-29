from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

#注册
def register(request):
    if request.method == 'GET':
        return render(request, 'basic/register.html')

    elif request.method == 'POST':
        user_name = request.POST.get('username', '')
        email = request.POST.get('email', '')
        pwd = request.POST.get('password', '')

        if User.objects.filter(username=user_name).exists():
            # 用户已存在，返回注册页面并显示提示
            return render(request, 'accounting/login.html', {'exists': True, 'show_register': True})

        user = User.objects.create_user(username=user_name, password=pwd, email=email)
        user.save()

        # 注册成功，返回登录页面并显示提示
        return render(request, 'accounting/login.html', {'success': True, 'show_login': True})

    return JsonResponse({'code': 403, 'msg': '被禁止的请求'})


from .models import *
def index(request):
    all_accounts = Account.objects.all()
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.all()
    currencies = Currency.objects.all()
    ie_types = []
    for t in Category.CATEGORY_TYPES:
        ie_types.append(t)
    context = {
        'accounts': all_accounts,
        'categories': categories,
        'sub_categories': sub_categories,
        'currencies': currencies,
        'ie_types': ie_types
    }
    return render(request, 'accounting/index.html', context)
def retrieve_category(request):
    ie_type = request.POST.get('ie_type')
    categories = Category.objects.filter(category_type=ie_type)
    category_list = []
    for c in categories:
        category_list.append(c.name)
    return JsonResponse({"categories": category_list})
def login(request):
    return  render(request, 'accounting/login.html')