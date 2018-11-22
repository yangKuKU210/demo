from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from yrj import models
import json
from django.db.models import Q
import csv


# Create your views here.
def index(request):
    return HttpResponse('210')


# 向数据库添加数据
def add(request):
    # 读取文件
    file1 = csv.reader(open('C:/Users/admin/Desktop/test/HelloWorld/HelloWorld/NBA.csv', 'r'))
    # 遍历每条数据
    for item in file1:
        # 插入数据
        models.NBA.objects.create(
            **{
                'age': item[0],
                'conference': item[1],
                'date': item[2],
                'date_year': item[3],
                'date_date': item[4],
                'player': item[5],
                'position': item[6],
                'season': item[7],
                'league': item[8],
                'team': item[9],
                'weight': item[10],
                'real_value': item[11]

            }
        )
    return HttpResponse('200')

# 关键字查询
def search(request):
    # 获取关键字
    con = json.loads(request.body)
    # 新建空条件字典
    conditions = {}
    # 对接受条件进行判断，非空条件加入conditions字典中
    if con['player']:
        # 球员姓名
        conditions["player__regex"] = con['player']
    if con['date_year']:
        # 年
        conditions["date_year"] = con['date_year']
    #     多条件查询数据
    data = models.NBA.objects.filter(**conditions).values()
    # 返回数据
    return HttpResponse(json.dumps(list(data)))



