from django.db import models
from django.conf import settings

# Create your models here.
class ReviewModel(models.Model):
    
    #title
    title = models.CharField(max_length=100)

    #content
    content = models.CharField(max_length=500)
    
    #author
    author = models.ForeignKey('auth.User', related_name="reviews", on_delete=models.CASCADE, null=True)

    #image
    image_url = models.URLField(max_length=200)
    
    #created date
    created_date = models.DateField(auto_now_add=True, null=True)
    
    #edited date
    last_edit_date = models.DateField(auto_now=True, null=True)

    #toString method
    def __str__(self):
        result = {
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "created_date": self.created_date,
            "last_edit_date": self.last_edit.date,
        }
        return result
