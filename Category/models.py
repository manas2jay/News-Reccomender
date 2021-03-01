from django.db import models


# Create your models here.
class sports_news(models.Model):
    id = models.DecimalField(max_digits=5, primary_key=True, decimal_places=2)
    source = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=1000, null=True, blank=True)
    UrlToImage = models.ImageField(max_length=1000, null=True, blank=True)
    PublishedAt = models.DateField()
    content = models.TextField(max_length=1000, null=True, blank=True)
    #Category = models.CharField(max_length=100)

    def __str__(self):
        return self.title

#
# class science_news(models.Model):
#     id = models.DecimalField(max_digits=5, primary_key=True, decimal_places=2)
#     source = models.CharField(max_length=100, null=True, blank=True)
#     author = models.CharField(max_length=100, null=True, blank=True)
#     title = models.CharField(max_length=200, null=True, blank=True)
#     description = models.TextField(max_length=500, null=True, blank=True)
#     url = models.URLField(max_length=1000, null=True, blank=True)
#     UrlToImage = models.ImageField(max_length=1000, null=True, blank=True)
#     PublishedAt = models.DateField()
#     content = models.TextField(max_length=1000, null=True, blank=True)
#     #Category = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.title
#
#
# class technology_news(models.Model):
#     id = models.DecimalField(max_digits=5, primary_key=True, decimal_places=2)
#     source = models.CharField(max_length=100, null=True, blank=True)
#     author = models.CharField(max_length=100, null=True, blank=True)
#     title = models.CharField(max_length=200, null=True, blank=True)
#     description = models.TextField(max_length=500, null=True, blank=True)
#     url = models.URLField(max_length=1000, null=True, blank=True)
#     UrlToImage = models.ImageField(max_length=1000, null=True, blank=True)
#     PublishedAt = models.DateField()
#     content = models.TextField(max_length=1000, null=True, blank=True)
#     #Category = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.title
#
#
# class business_news(models.Model):
#     id = models.DecimalField(max_digits=5, primary_key=True, decimal_places=2)
#     source = models.CharField(max_length=100, null=True, blank=True)
#     author = models.CharField(max_length=100, null=True, blank=True)
#     title = models.CharField(max_length=200, null=True, blank=True)
#     description = models.TextField(max_length=500, null=True, blank=True)
#     url = models.URLField(max_length=1000, null=True, blank=True)
#     UrlToImage = models.ImageField(max_length=1000, null=True, blank=True)
#     PublishedAt = models.DateField()
#     content = models.TextField(max_length=1000, null=True, blank=True)
#     #Category = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.title
#
#
# class entertainment_news(models.Model):
#     id = models.DecimalField(max_digits=5, primary_key=True, decimal_places=2)
#     source = models.CharField(max_length=100, null=True, blank=True)
#     author = models.CharField(max_length=100, null=True, blank=True)
#     title = models.CharField(max_length=200, null=True, blank=True)
#     description = models.TextField(max_length=500, null=True, blank=True)
#     url = models.URLField(max_length=1000, null=True, blank=True)
#     UrlToImage = models.ImageField(max_length=1000, null=True, blank=True)
#     PublishedAt = models.DateField()
#     content = models.TextField(max_length=1000, null=True, blank=True)
#     #Category = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.title
#
#
# class health_news(models.Model):
#     id = models.DecimalField(max_digits=5, primary_key=True, decimal_places=2)
#     source = models.CharField(max_length=100, null=True, blank=True)
#     author = models.CharField(max_length=100, null=True, blank=True)
#     title = models.CharField(max_length=200, null=True, blank=True)
#     description = models.TextField(max_length=500, null=True, blank=True)
#     url = models.URLField(max_length=1000, null=True, blank=True)
#     UrlToImage = models.ImageField(max_length=1000, null=True, blank=True)
#     PublishedAt = models.DateField()
#     content = models.TextField(max_length=1000, null=True, blank=True)
#     #Category = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.title
#
#
# class general_news(models.Model):
#     id = models.DecimalField(max_digits=5, primary_key=True, decimal_places=2)
#     source = models.CharField(max_length=100, null=True, blank=True)
#     author = models.CharField(max_length=100, null=True, blank=True)
#     title = models.CharField(max_length=200, null=True, blank=True)
#     description = models.TextField(max_length=500, null=True, blank=True)
#     url = models.URLField(max_length=1000, null=True, blank=True)
#     UrlToImage = models.ImageField(max_length=1000, null=True, blank=True)
#     PublishedAt = models.DateField()
#     content = models.TextField(max_length=1000, null=True, blank=True)
#     #Category = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.title


import requests, json


def get_sports():
    url = 'http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=4edd10e4067c48eabfbebdf072f6d9ad&pageSize=100'
    response = requests.get(url)
    news_list = []
    json_output = json.dumps(response.json(), indent=4)
    sports_news.objects.all().delete()
    # print(json_output)
    news_data = json.loads(json_output)
    c = 1.
    for u in news_data['articles']:
        if u['author'] == 'NULL':
            u['author'] = 'not found'
        sports_news.objects.create(id=c, source=u['source']['name'], author=u['author'], title=u['title'],
                                   description=u['description'], url=u['url'], UrlToImage=u['urlToImage'],
                                   PublishedAt=u['publishedAt'][:10], content=u['content'])
        c += 1.

#
# def get_science():
#     url = 'http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=4edd10e4067c48eabfbebdf072f6d9ad' \
#           '&pageSize=100 '
#     response = requests.get(url)
#     news_list = []
#     json_output = json.dumps(response.json(), indent=4)
#     #science_news.objects.all().delete()
#     # print(json_output)
#     news_data = json.loads(json_output)
#     c = 1.
#     for u in news_data['articles']:
#         if u['author'] == 'NULL':
#             u['author'] = 'not found'
#         science_news.objects.create(id=c, source=u['source']['name'], author=u['author'], title=u['title'],
#                                     description=u['description'], url=u['url'], UrlToImage=u['urlToImage'],
#                                     PublishedAt=u['publishedAt'][:10], content=u['content'])
#         c += 1.
#
#
# def get_techonlogy():
#     url = 'http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=4edd10e4067c48eabfbebdf072f6d9ad' \
#           '&pageSize=100 '
#     response = requests.get(url)
#     news_list = []
#     json_output = json.dumps(response.json(), indent=4)
#     #technology_news.objects.all().delete()
#     # print(json_output)
#     news_data = json.loads(json_output)
#     c = 1.
#     for u in news_data['articles']:
#         if u['author'] == 'NULL':
#             u['author'] = 'not found'
#         technology_news.objects.create(id=c, source=u['source']['name'], author=u['author'], title=u['title'],
#                                        description=u['description'], url=u['url'], UrlToImage=u['urlToImage'],
#                                        PublishedAt=u['publishedAt'][:10], content=u['content'])
#         c += 1.
#
#
# def get_business():
#     url = 'http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=4edd10e4067c48eabfbebdf072f6d9ad' \
#           '&pageSize=100 '
#     response = requests.get(url)
#     news_list = []
#     json_output = json.dumps(response.json(), indent=4)
#     #business_news.objects.all().delete()
#     # print(json_output)
#     news_data = json.loads(json_output)
#     c = 1.
#     for u in news_data['articles']:
#         if u['author'] == 'NULL':
#             u['author'] = 'not found'
#         business_news.objects.create(id=c, source=u['source']['name'], author=u['author'], title=u['title'],
#                                      description=u['description'], url=u['url'], UrlToImage=u['urlToImage'],
#                                      PublishedAt=u['publishedAt'][:10], content=u['content'])
#         c += 1.
#
#
# def get_entertainment():
#     url = 'http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey' \
#           '=4edd10e4067c48eabfbebdf072f6d9ad&pageSize=100 '
#     response = requests.get(url)
#     news_list = []
#     json_output = json.dumps(response.json(), indent=4)
#     #entertainment_news.objects.all().delete()
#     # print(json_output)
#     news_data = json.loads(json_output)
#     c = 1.
#     for u in news_data['articles']:
#         if u['author'] == 'NULL':
#             u['author'] = 'not found'
#         entertainment_news.objects.create(id=c, source=u['source']['name'], author=u['author'], title=u['title'],
#                                           description=u['description'], url=u['url'], UrlToImage=u['urlToImage'],
#                                           PublishedAt=u['publishedAt'][:10], content=u['content'])
#         c += 1.
#
#
# def get_general():
#     url = 'http://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=4edd10e4067c48eabfbebdf072f6d9ad' \
#           '&pageSize=100 '
#     response = requests.get(url)
#     news_list = []
#     json_output = json.dumps(response.json(), indent=4)
#     #general_news.objects.all().delete()
#     # print(json_output)
#     news_data = json.loads(json_output)
#     c = 1.
#     for u in news_data['articles']:
#         if u['author'] == 'NULL':
#             u['author'] = 'not found'
#         general_news.objects.create(id=c, source=u['source']['name'], author=u['author'], title=u['title'],
#                                     description=u['description'], url=u['url'], UrlToImage=u['urlToImage'],
#                                     PublishedAt=u['publishedAt'][:10], content=u['content'])
#         c += 1.
#
#
# def get_health():
#     url = 'http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=4edd10e4067c48eabfbebdf072f6d9ad' \
#           '&pageSize=100 '
#     response = requests.get(url)
#     news_list = []
#     json_output = json.dumps(response.json(), indent=4)
#     #health_news.objects.all().delete()
#     # print(json_output)
#     news_data = json.loads(json_output)
#     c = 1.
#     for u in news_data['articles']:
#         if u['author'] == 'NULL':
#             u['author'] = 'not found'
#         health_news.objects.create(id=c, source=u['source']['name'], author=u['author'], title=u['title'],
#                                    description=u['description'], url=u['url'], UrlToImage=u['urlToImage'],
#                                    PublishedAt=u['publishedAt'][:10], content=u['content'])
#         c += 1.
