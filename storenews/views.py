from django.shortcuts import render, HttpResponse
from .models import store, user_news


# Create your views here.

def getnews(request):
    store(request.GET['user'], request.GET['description'])
    return HttpResponse('got add')


def show(request):
    for i in user_news.objects.all():
        print(i.user, i.description)
    return HttpResponse('go to console')


def deletealluserrec(requeset):
    user_news.objects.all().delete()
    return HttpResponse('all user detail are deleted in user-read news table')


def deleteuser(request):
    if len(user_news.objects.all().filter(user=request.GET['user'])) == 0:
        return HttpResponse('user not found')
    else:
        user_news.objects.all().filter(user=request.GET['user']).delete()
        return HttpResponse('deleted')
