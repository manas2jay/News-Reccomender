from django.db import models


# Create your models here.
class newscat(models.Model):
    id = models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
    source = models.CharField(max_length=1000, null=True, blank=True)
    author = models.CharField(max_length=1000, null=True, blank=True)
    title = models.CharField(max_length=2000, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
    url = models.URLField(max_length=1000, null=True, blank=True)
    UrlToImage = models.URLField(max_length=1000, null=True, blank=True)
    PublishedAt = models.DateField()
    content = models.TextField(max_length=10000, null=True, blank=True)
    category = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.title


import requests, json


# from newsapi import NewsApiClient
#
# newsapi = NewsApiClient(api_key='6713ffdf1ac5461bbae3c39be1978aac')

def extract_news_sports():
    url = 'http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=6713ffdf1ac5461bbae3c39be1978aac&pageSize=100'
    response = requests.get(url)
    news_list = []
    json_output = json.dumps(response.json(), indent=4)
    # print('before sports deltetion', len(newscat.objects.all()))
    # newscat.objects.all().delete()
    # print('after sportsdeltetion', len(newscat.objects.all()))
    news_data = json.loads(json_output)
    for u in news_data['articles']:
        if u['author'] is None:
            u['author']='not found'
        if u['urlToImage'] is None:
            u['urlToImage'] = 'https://newsinterpretation.com/wp-content/uploads/2020/03/news33.jpg'
        i, created = newscat.objects.update_or_create(source=u['source']['name'], author=u['author'], title=u['title'],
                                                      description=u['description'], url=u['url'],
                                                      UrlToImage=u['urlToImage'],
                                                      PublishedAt=u['publishedAt'][:10], content=u['content'],
                                                      category='sports')
    print('After sports updation', len(newscat.objects.all().filter(category='sports')))
    print('Total ', len(newscat.objects.all()))
    # for i in newscat.objects.all():
    #     print(i.title)


def extract_news_business():
    url = 'http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=6713ffdf1ac5461bbae3c39be1978aac&pageSize=100'
    response = requests.get(url)
    json_output = json.dumps(response.json(), indent=4)
    # print('before business deltetion', len(newscat.objects.all()))
    # print('after business deltetion', len(newscat.objects.all()))
    news_data = json.loads(json_output)
    for u in news_data['articles']:
        if u['author'] is None:
            u['author']='not found'
        if u['urlToImage'] is None:
            u['urlToImage'] = 'https://newsinterpretation.com/wp-content/uploads/2020/03/news33.jpg'
        i, created = newscat.objects.update_or_create(source=u['source']['name'], author=u['author'], title=u['title'],
                                                      description=u['description'], url=u['url'],
                                                      UrlToImage=u['urlToImage'],
                                                      PublishedAt=u['publishedAt'][:10], content=u['content'],
                                                      category='business')


def extract_news_general():
    url = 'http://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=4edd10e4067c48eabfbebdf072f6d9ad&pageSize=100'
    response = requests.get(url)
    news_list = []
    json_output = json.dumps(response.json(), indent=4)
    # newscat.objects.all().delete()
    # for i in newscat.objects.all():
    #     print(i.title)
    # print('general',len(json_output))
    news_data = json.loads(json_output)
    for u in news_data['articles']:
        if u['author'] is None:
            u['author']='not found'
        if u['urlToImage'] is None:
            u['urlToImage'] = 'https://newsinterpretation.com/wp-content/uploads/2020/03/news33.jpg'
        i, created = newscat.objects.update_or_create(source=u['source']['name'], author=u['author'], title=u['title'],
                                                      description=u['description'], url=u['url'],
                                                      UrlToImage=u['urlToImage'],
                                                      PublishedAt=u['publishedAt'][:10], content=u['content'],
                                                      category='general')


#     # for i in newscat.objects.all():
#     #     print(i.title)
#
def extract_news_Health():
    url = 'http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=4edd10e4067c48eabfbebdf072f6d9ad&pageSize=100'
    response = requests.get(url)
    news_list = []
    json_output = json.dumps(response.json(), indent=4)

    # newscat.objects.all().delete()
    # for i in newscat.objects.all():
    #     print(i.title)
    # print('health',len(json_output))
    news_data = json.loads(json_output)
    for u in news_data['articles']:
        if u['author'] is None:
            u['author']='not found'
        if u['urlToImage'] is None:
            u['urlToImage'] = 'https://newsinterpretation.com/wp-content/uploads/2020/03/news33.jpg'
        i, created = newscat.objects.update_or_create(source=u['source']['name'], author=u['author'], title=u['title'],
                                                      description=u['description'], url=u['url'],
                                                      UrlToImage=u['urlToImage'],
                                                      PublishedAt=u['publishedAt'][:10], content=u['content'],
                                                      category='health')


#     # for i in newscat.objects.all():
#     #     print(i.title)

def extract_news_science():
    url = 'http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=4edd10e4067c48eabfbebdf072f6d9ad&pageSize=100'
    response = requests.get(url)
    news_list = []
    json_output = json.dumps(response.json(), indent=4)
    # print('before science deltetion', len(newscat.objects.all()))
    # print('after science deltetion', len(newscat.objects.all()))
    # newscat.objects.all().delete()
    # for i in newscat.objects.all():
    #     print(i.title)
    # print('science',len(json_output))
    news_data = json.loads(json_output)

    for u in news_data['articles']:
        if u['author'] is None:
            u['author']='not found'
        if u['urlToImage'] is None:
            u['urlToImage'] = 'https://newsinterpretation.com/wp-content/uploads/2020/03/news33.jpg'
        i, created = newscat.objects.update_or_create(source=u['source']['name'], author=u['author'], title=u['title'],
                                                      description=u['description'], url=u['url'],
                                                      UrlToImage=u['urlToImage'],
                                                      PublishedAt=u['publishedAt'][:10], content=u['content'],
                                                      category='science')
        # print('After science updation', len(newscat.objects.all().filter(category='business')))
        # print('Total ', len(newscat.objects.all()))


#     # for i in newscat.objects.all():
#     #     print(i.title)

def extract_news_techonology():
    url = 'http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=4edd10e4067c48eabfbebdf072f6d9ad&pageSize=100'
    response = requests.get(url)
    news_list = []
    json_output = json.dumps(response.json(), indent=4)
    # print('before  deltetion', len(newscat.objects.all()))
    print('after technology deltetion', len(newscat.objects.all()))
    # newscat.objects.all().delete()
    # for i in newscat.objects.all():
    #     print(i.title)
    # print('technology',len(json_output))
    news_data = json.loads(json_output)

    for u in news_data['articles']:
        if u['author'] is None:
            u['author']='not found'
        if u['urlToImage'] is None:
            u['urlToImage'] = 'https://newsinterpretation.com/wp-content/uploads/2020/03/news33.jpg'
        i, created = newscat.objects.update_or_create(source=u['source']['name'], author=u['author'], title=u['title'],
                                                      description=u['description'], url=u['url'],
                                                      UrlToImage=u['urlToImage'],
                                                      PublishedAt=u['publishedAt'][:10], content=u['content'],
                                                      category='technology')
    print('After technology updation', len(newscat.objects.all().filter(category='technology')))
    print('Total ', len(newscat.objects.all()))


#     # for i in newscat.objects.all():
#     #     print(i.title)

def extract_news_entertainment():
    url = 'http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=4edd10e4067c48eabfbebdf072f6d9ad&pageSize=100'
    response = requests.get(url)
    news_list = []
    json_output = json.dumps(response.json(), indent=4)
    # newscat.objects.all().delete()
    # for i in newscat.objects.all():
    #     print(i.title)
    # print('entertainmnet',len(json_output))
    news_data = json.loads(json_output)
    for u in news_data['articles']:
        if u['author'] is None:
            u['author']='not found'
        if u['urlToImage'] is None:
            u['urlToImage'] = 'https://newsinterpretation.com/wp-content/uploads/2020/03/news33.jpg'
        i, created = newscat.objects.update_or_create(source=u['source']['name'], author=u['author'], title=u['title'],
                                                      description=u['description'], url=u['url'],
                                                      UrlToImage=u['urlToImage'],
                                                      PublishedAt=u['publishedAt'][:10], content=u['content'],
                                                      category='entertainment')

#     # for i in newscat.objects.all():
#     print(i.title)
