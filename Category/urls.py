from django.urls import path
from .views import *
import datetime
import requests
urlpatterns =[

    path('sports',Listsports.as_view()),
    # path('business',Listbusiness.as_view()),
    # path('entertainment',Listentertainment.as_view()),
    # path('general',Listgeneral.as_view()),
    # path('health',Listhealth.as_view()),
    # path('science',Listscience.as_view()),
    # path('technology',Listtechnology.as_view()),
    path('sports/<int:pk>',Detailsports.as_view()),
    # path('business/<int:pk>',Detailbusiness.as_view()),
    # path('entertainment/<int:pk>',Detailentertainment.as_view()),
    # path('general/<int:pk>',Detailgeneral.as_view()),
    # path('health/<int:pk>',Detailhealth.as_view()),
    # path('science/<int:pk>',Detailscience.as_view()),
    # path('technology/<int:pk>',Detailtechnology.as_view()),

]