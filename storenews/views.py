from django.shortcuts import render, HttpResponse
from .models import store, user_news
from .serializers import UserSerializer
from rest_framework import generics
import json


class ListUserNews(generics.ListAPIView):
    queryset = user_news.objects.all()
    serializer_class = UserSerializer

def recomend(request):
    a=[]
    for i in user_news.objects.all().filter(user=request.GET['user']):
        a.append(i.description)
    print(a)
    return HttpResponse(a)

# Create your views here.



def getnews(request):
    store(request.GET['user'], request.GET['description'])
    return HttpResponse('got add')


# def show(request):
#     for i in user_news.objects.all().filter(user=request.GET['user']):
#         print(i.user, i.description)
#
#     class ListUserNews(generics.ListAPIView):
#         queryset = user_news.objects.all()
#         serializer_class = UserSerializer
#     return ListUserNews.as_view


def deletealluserrec(requeset):
    user_news.objects.all().delete()
    return HttpResponse('all user detail are deleted in user-read news table')


def deleteuser(request):
    if len(user_news.objects.all().filter(user=request.GET['user'])) == 0:
        return HttpResponse('user not found')
    else:
        user_news.objects.all().filter(user=request.GET['user']).delete()
        return HttpResponse('deleted')
