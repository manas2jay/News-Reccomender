from django.db import models


# Create your models here.
class user_news(models.Model):
    user = models.IntegerField(primary_key=False)
    description = models.TextField(max_length=1000)

def store(userid,desc):
    a = user_news.objects.create(user=userid,description=desc)