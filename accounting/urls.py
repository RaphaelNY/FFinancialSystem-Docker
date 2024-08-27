from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #收支记账主页面
    path('login/', views.login, name='login'),
]