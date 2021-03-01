from django.urls import path
from .views import ListTopHeadline,DetailTopHeadline
import datetime
import requests
urlpatterns =[

    path('topheadline',ListTopHeadline.as_view()),
    path('topheadline/<int:pk>',DetailTopHeadline.as_view())
    # path('topheadline/refresh',ref_object),
]