from django.db import models

# Create your models here.
#
class NBA(models.Model):
    age=models.CharField(null=True,max_length=200)
    conference=models.CharField(null=True,max_length=200)
    date=models.CharField(null=True,max_length=200)
    date_year=models.CharField(null=True,max_length=200)
    date_date=models.CharField(null=True,max_length=200)
    player=models.CharField(null=True,max_length=200)
    position=models.CharField(null=True,max_length=200)
    season=models.CharField(null=True,max_length=200)
    season_short=models.CharField(null=True,max_length=200)
    league=models.CharField(null=True,max_length=200)
    team=models.CharField(null=True,max_length=200)
    weight=models.CharField(null=True,max_length=200)
    real_value=models.CharField(null=True,max_length=200)