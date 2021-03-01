from django.db import models


# Create your models here.
class Topheadline_detail(models.Model):
    id = models.DecimalField(max_digits=5,primary_key=True,decimal_places=2)
    source = models.CharField(max_length=100,null=True,blank=True)
    author = models.CharField(max_length=100,null=True,blank=True)
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(max_length=500,null=True,blank=True)
    url = models.URLField(max_length=1000,null=True,blank=True)
    UrlToImage = models.ImageField(max_length=1000,null=True,blank=True)
    PublishedAt = models.DateField()
    content = models.TextField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.title


import requests, json


def extract_news():
    url = 'http://newsapi.org/v2/top-headlines?''country=in&''apiKey=4edd10e4067c48eabfbebdf072f6d9ad&pageSize=100'
    response = requests.get(url)
    news_list = []
    json_output = json.dumps(response.json(), indent=4)
    Topheadline_detail.objects.all().delete()
    # print(json_output)
    news_data = json.loads(json_output)
    c=1.
    for u in news_data['articles']:
        if u['author']=='NULL':
            u['author']='not found'
        Topheadline_detail.objects.create(id=c,source=u['source']['name'],author=u['author'],title=u['title'],description=u['description'],url=u['url'],UrlToImage=u['urlToImage'],PublishedAt=u['publishedAt'][:10],content=u['content'])
        c+=1.

