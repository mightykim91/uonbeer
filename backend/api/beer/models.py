from django.db import models

#Last Modified 2020.09.16(Modified Name Field - Divide name to Korean and English)
class Beer(models.Model):

    #Override table name from beer_beer to beer
    class Meta:
        db_table = "beer"

    #맥주이름(영문)
    name = models.CharField(max_length=100)
    #맥주이름(한글)
    name_kr = models.CharField(max_length=100, null=True)
    #유형
    style = models.CharField(max_length=50)
    #생산국
    country = models.CharField(max_length=50)
    #도수
    abv = models.FloatField(default=0, null=True)
    
    