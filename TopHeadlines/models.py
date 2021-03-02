from django.db import models


# Create your models here.
class Topheadline_detail(models.Model):
    id = models.AutoField(verbose_name='ID',serialize=False,auto_created=True,primary_key=True),
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
    url = 'http://newsapi.org/v2/top-headlines?''country=in&''apiKey=6713ffdf1ac5461bbae3c39be1978aac&pageSize=100'
    response = requests.get(url)
    news_list = []
    json_output = json.dumps(response.json(), indent=4)
    print('before deltetion',len(Topheadline_detail.objects.all()))
    Topheadline_detail.objects.all().delete()
    news_data = json.loads(json_output)
    print('after deltetion', len(Topheadline_detail.objects.all()))
    c = 1.0
    for u in news_data['articles']:
        if u['author']=='NULL':
            u['author']='not found'
        i, created = Topheadline_detail.objects.update_or_create(id=c,source=u['source']['name'],author=u['author'],title=u['title'],description=u['description'],url=u['url'],UrlToImage=u['urlToImage'],PublishedAt=u['publishedAt'][:10],content=u['content'])
        c+=1.0

