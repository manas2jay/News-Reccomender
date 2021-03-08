from django.urls import path, include
from .views import getnews,show,deleteuser,deletealluserrec,recommender,ListUserNews
from django.http import HttpResponse
import datetime
import requests

urlpatterns = [
    path('', getnews),
    path('show',show),
    path('deleteall',deletealluserrec),
    path('delete',deleteuser),
    path('recommend',ListUserNews.as_view()),
    #path('showallusernewstable',ListUserNews.as_view()),
]
