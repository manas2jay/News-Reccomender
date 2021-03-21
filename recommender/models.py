from django.db import models
import requests, json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
# from nltk import word_tokenize
# from nltk.stem import WordNetLemmatizer
# import nltk
# from nltk.corpus import stopwords
from .rec import similarity

# Create your models here.

class recommender_user(models.Model):
    id = models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
    #source = models.CharField(max_length=1000, null=True, blank=True)
    author = models.CharField(max_length=1000, null=True, blank=True)
    title = models.CharField(max_length=2000, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
    url = models.URLField(max_length=10000, null=True, blank=True)
    UrlToImage = models.URLField(max_length=10000, null=True, blank=True)
    PublishedAt = models.DateField()
    content = models.TextField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.title


def corpus(topic='description'):
    a = []
    url = 'https://newsapi.org/v2/everything?q=india&apiKey=4edd10e4067c48eabfbebdf072f6d9ad&pageSize=100'
    response = requests.get(url)
    news_list = []
    recommender_user.objects.all().delete()
    json_output = json.dumps(response.json(), indent=4)
    news_data = json.loads(json_output)
    c = 1.0
    for u in news_data['articles']:
        i = recommender_user.objects.create(id=c,author=u['author'], title=u['title'],
                                                               description=u['description'], url=u['url'],
                                                               UrlToImage=u['urlToImage'],
                                                               PublishedAt=u['publishedAt'][:10],
                                                               content=u['content'])
        c += 1.0


def get_recommend(user):
    url = 'http://192.168.1.45:8000/adduser/recommend?user=' + str(user)
    response = requests.get(url)
    #print(response.text)
    s = response.content
    s = str(s).split("''")
    #print(s)
    s[0]=s[0][3:]
    s[-1] = s[-1][:-2]
    sample = []
    for i in s:
        sample.append(i)
    print(['*'*400],'\n',sample)
    corpus()
    corp = []
    for i in recommender_user.objects.all():
        corp.append(i.description)

    simliarity_list = similarity(sample,corp)
    pivot=(sum(simliarity_list.values())/len(simliarity_list.values()))+0.05
    print(pivot)
    dele = []
    for key,val in simliarity_list.items():
        if val>=pivot:
            continue
        else:
            dele.append(key)
    for i in dele:
        del simliarity_list[i]
    for i in recommender_user.objects.all():
        if i.description in simliarity_list.keys():
            continue
        else:
            recommender_user.objects.all().filter(description=i.description).delete()

    for i in simliarity_list.keys():
        print(i,simliarity_list[i])