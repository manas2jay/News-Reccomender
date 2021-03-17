from django.db import models
import requests, json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords


# Create your models here.

class recommender_user(models.Model):
    id = models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
    source = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=1000, null=True, blank=True)
    UrlToImage = models.URLField(max_length=1000, null=True, blank=True)
    PublishedAt = models.DateField()
    content = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title


def corpus(topic='description'):
    a = []
    url = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=4edd10e4067c48eabfbebdf072f6d9ad'
    response = requests.get(url)
    news_list = []
    json_output = json.dumps(response.json(), indent=4)
    news_data = json.loads(json_output)
    if topic == 'description':
        for i in news_data:
            a.append(i[topic])
        return a
    else:
        return news_data


def get_recommend(user):
    url = '192.168.1.45:8000/news/show?user=' + str(user)
    response = requests.get(url)
    news_list = []
    json_output = json.dumps(response.json(), indent=4)

    recommender_user.objects.all().delete()
    news_data = json.loads(json_output)
    for i in news_data:
        news_list.append(i['description'])

    nltk.download('punkt')
    stop_words = set(stopwords.words('english'))

    # Interface lemma tokenizer from nltk with sklearn
    class LemmaTokenizer:
        ignore_tokens = [',', '.', ';', ':', '"', '``', "''", '`']

        def __init__(self):
            self.wnl = WordNetLemmatizer()

        def __call__(self, doc):
            return [self.wnl.lemmatize(t) for t in word_tokenize(doc) if t not in self.ignore_tokens]

    # Lemmatize the stop words
    tokenizer = LemmaTokenizer()
    token_stop = tokenizer(' '.join(stop_words))

    search_terms = news_list
    documents = corpus()

    # Create TF-idf model
    vectorizer = TfidfVectorizer(stop_words=token_stop,
                                 tokenizer=tokenizer)
    doc_vectors = vectorizer.fit_transform([search_terms] + documents)

    # Calculate similarity
    cosine_similarities = linear_kernel(doc_vectors[0:1], doc_vectors).flatten()
    document_scores = [item.item() for item in cosine_similarities[1:]]

    # append news after reccomend
    for i in document_scores:
        print(i)
    print(type(document_scores))
    document_scores = document_scores.sort()
    c = 1.0
    for u in corpus("all"):
        if u['description'] in document_scores[:5]:
            i, created = recommender_user.objects.update_or_create(id=c, source=u['source']['name'],
                                                                   author=u['author'], title=u['title'],
                                                                   description=u['description'], url=u['url'],
                                                                   UrlToImage=u['urlToImage'],
                                                                   PublishedAt=u['publishedAt'][:10],
                                                                   content=u['content'])
            c += 1.0
