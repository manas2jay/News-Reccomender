from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializer import *
from rest_framework import generics
import datetime


# Create your views here.
class Listsports(generics.ListAPIView):
    get_sports()
    queryset = sports_news.objects.all()
    serializer_class = SportsSerializer


class Detailsports(generics.RetrieveUpdateDestroyAPIView):
    queryset = sports_news.objects.all()
    serializer_class = SportsSerializer

#
# class Listbusiness(generics.ListAPIView):
#     get_business()
#     queryset = business_news.objects.all()
#     serializer_class = businessSerializer
#
#
# class Detailbusiness(generics.RetrieveUpdateDestroyAPIView):
#     queryset = business_news.objects.all()
#     serializer_class = businessSerializer
#
#
# class Listentertainment(generics.ListAPIView):
#     get_entertainment()
#     queryset = entertainment_news.objects.all()
#     serializer_class = entertainmentSerializer
#
#
# class Detailentertainment(generics.RetrieveUpdateDestroyAPIView):
#     queryset = entertainment_news.objects.all()
#     serializer_class = entertainmentSerializer
#
#
# class Listgeneral(generics.ListAPIView):
#     get_general()
#     queryset = general_news.objects.all()
#     serializer_class = generalSerializer
#
#
# class Detailgeneral(generics.RetrieveUpdateDestroyAPIView):
#     queryset = general_news.objects.all()
#     serializer_class = generalSerializer
#
#
# class Listhealth(generics.ListAPIView):
#     get_health()
#     queryset = health_news.objects.all()
#     serializer_class = healthSerializer
#
#
# class Detailhealth(generics.RetrieveUpdateDestroyAPIView):
#     queryset = health_news.objects.all()
#     serializer_class = healthSerializer
#
#
# class Listtechnology(generics.ListAPIView):
#     get_techonlogy()
#     queryset = technology_news.objects.all()
#     serializer_class = technologySerializer
#
#
# class Detailtechnology(generics.RetrieveUpdateDestroyAPIView):
#     queryset = technology_news.objects.all()
#     serializer_class = technologySerializer
#
# class Listscience(generics.ListAPIView):
#     get_science()
#     queryset = science_news.objects.all()
#     serializer_class = scienceSerializer
#
#
# class Detailscience(generics.RetrieveUpdateDestroyAPIView):
#     queryset = science_news.objects.all()
#     serializer_class = scienceSerializer
#
#
#
