from django.urls import path, include
from .views import getnews,deleteuser,deletealluserrec,ListUserNews
from django.http import HttpResponse
import datetime
import requests

urlpatterns = [
    path('', getnews),
    path('show',ListUserNews.as_view()),
    path('deleteall',deletealluserrec),
    path('delete',deleteuser),

]
