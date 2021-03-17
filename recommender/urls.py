from django.urls import path, include
from .views import user_reccomend
from django.http import HttpResponse
import datetime
import requests

urlpatterns = [
    path('', user_reccomend),

]
