from django.urls import path,include
from .views import ListTopHeadline,DetailTopHeadline,refresh,welcome
from django.http import HttpResponse
import datetime
import requests
urlpatterns =[
    path('',welcome),
    path('topheadline',ListTopHeadline.as_view()),
    path('topheadline/<int:pk>',DetailTopHeadline.as_view()),
    path('topheadline/refresh',refresh),
]