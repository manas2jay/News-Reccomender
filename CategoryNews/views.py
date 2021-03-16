from django.shortcuts import render
from .models import *
from django.shortcuts import render
from django.http import HttpResponse
from .serializer import *
from rest_framework import generics
import requests
#
import datetime


#
# #
# Create your views here.
def home(request):
    return HttpResponse('helllo')


def alldeletenews(request):
    newscat.objects.all().delete()
    return HttpResponse('all deleted')


def businessrefresh():
    print('entering business refresh')
    print(len(newscat.objects.all()))
    newscat.objects.all().filter(category='business').delete()
    print(len(newscat.objects.all()))
    extract_news_business()
    # return HttpResponse('business updated')


def sprotsrefresh():
    print('entering sprots refresh')
    print(len(newscat.objects.all()))
    newscat.objects.all().filter(category='sports').delete()
    print(len(newscat.objects.all()))
    extract_news_sports()
    # return HttpResponse('Sports updated')


def generalrefresh():
    print('entering general refresh')
    print(len(newscat.objects.all()))
    newscat.objects.all().filter(category='general').delete()
    print(len(newscat.objects.all()))
    extract_news_general()
    # return HttpResponse('general updated')


def healthrefresh():
    print('entering health refresh')
    print(len(newscat.objects.all()))
    newscat.objects.all().filter(category='health').delete()
    print(len(newscat.objects.all()))
    extract_news_Health()
    # return HttpResponse('health updated')


def generalrefresh():
    print('entering general refresh')
    print(len(newscat.objects.all()))
    newscat.objects.all().filter(category='general').delete()
    print(len(newscat.objects.all()))
    extract_news_general()
    # return HttpResponse('general updated')


def sciencerefresh():
    print('entering science refresh')
    print(len(newscat.objects.all()))
    newscat.objects.all().filter(category='science').delete()
    print(len(newscat.objects.all()))
    extract_news_science()
    # return HttpResponse('science updated')


def technologyrefresh():
    print('entering technology refresh')
    print(len(newscat.objects.all()))
    newscat.objects.all().filter(category='technology').delete()
    print(len(newscat.objects.all()))
    extract_news_techonology()
    # return HttpResponse('technology updated')


def entetainmentrefresh():
    print('entering entertainment refresh')
    print(len(newscat.objects.all()))
    newscat.objects.all().filter(category='entertainment').delete()
    print(len(newscat.objects.all()))
    extract_news_entertainment()
    # return HttpResponse('entertainment updated')


class ListSportsNews(generics.ListAPIView):
    # sprotsrefresh(requests.post)
    print('sport after extraction', len(newscat.objects.all().filter(category='sports')))
    queryset = newscat.objects.all().filter(category='sports')
    serializer_class = SportSerializer


#
class ListBusinessNews(generics.ListAPIView):
    # businessrefresh(requests.post)
    print('busines after extraction', len(newscat.objects.all().filter(category='business')))
    queryset = newscat.objects.all().filter(category='business')
    serializer_class = BusinessSerializer


def refresh(request):
    sprotsrefresh()
    businessrefresh()
    generalrefresh()
    healthrefresh()

    sciencerefresh()
    technologyrefresh()
    entetainmentrefresh()
    return HttpResponse('all refreshed')


#
#
class ListGeneralNews(generics.ListAPIView):
    queryset = newscat.objects.all().filter(category='general')
    serializer_class = GeneralSerializer


class ListHealthNews(generics.ListAPIView):
    queryset = newscat.objects.all().filter(category='health')
    serializer_class = HealthSerializer


class ListEntertainmnentNews(generics.ListAPIView):
    queryset = newscat.objects.all().filter(category='entertainment')
    serializer_class = EntertainmentSerializer


class ListTechonologyNews(generics.ListAPIView):
    queryset = newscat.objects.all().filter(category='technology')
    serializer_class = TechnologySerializer


class ListScienceNews(generics.ListAPIView):
    queryset = newscat.objects.all().filter(category='science')
    serializer_class = ScienceSerializer
