from django.urls import path,include
from .views import ListTopHeadline,DetailTopHeadline,refresh
import datetime
import requests
urlpatterns =[

    path('topheadline',ListTopHeadline.as_view()),
    path('topheadline/<int:pk>',DetailTopHeadline.as_view()),
    path('topheadline/refresh',refresh),
]