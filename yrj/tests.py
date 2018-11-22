from django.test import TestCase
from yrj import models
# Create your tests here.
from openpyxl import load_workbook
import csv

file1=csv.reader(open('NBA.csv','r'))
print(file1)
for item in file1:
    print(item)
    '''
    models.NBA.objects.create(
        **{
            'age':item[0],
            'conference':item[1],
            'date':item[2],
            'date_year':item[3],
            'date_date':item[4],
            'player':item[5],
            'position':item[6],
            'season':item[7],
            'league':item[8],
            'team':item[9],
            'weight':item[10],
            'real_value':item[11]

        }
    )
    '''

