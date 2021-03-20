from django.urls import path, include
from .views import user_reccomend,ListRecommend,deleterec
from django.http import HttpResponse
import datetime
import requests

urlpatterns = [
    path('', user_reccomend),
    path('show',ListRecommend.as_view(),name='rec'),
    path('deleterec',deleterec),

]
