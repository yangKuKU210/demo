"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from .import views

from . import views
from django.conf.urls import url,include
app_name='yrj'

urlpatterns = [
    # 添加数据
    url(r'add/', views.add, name='add'),
    # 关键字查询数据
    url(r'search/', views.search, name='search'),
    # yrj首页
    url(r'^$', views.index, name='index'),

]
