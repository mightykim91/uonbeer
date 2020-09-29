from django.db import models
from django.core.files.images.ImageFile

#Last Modified 2020.09.16(Modified Name Field - Divide name to Korean and English)
class Beer(models.Model):

    #Override table name from beer_beer to beer
    class Meta:
        db_table = "beer"

    #맥주이름(영문)
    name = models.CharField(max_length=100)
    #맥주이름(한글)
    name_kr = models.CharField(max_length=100, null=True)
    #양조장 이름
    brew_name = models.CharField(max_length=100, null=True)
    #유형
    style = models.CharField(max_length=50)
    #생산국
    country = models.CharField(max_length=50)
    #도수
    abv = models.FloatField(default=0, null=True)
    #맥주 이미지
    image_url = models.URLField(max_length=200, null=True)
    
    