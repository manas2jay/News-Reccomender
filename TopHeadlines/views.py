from django.shortcuts import render
from django.http import HttpResponse
from .models import extract_news, Topheadline_detail
from .serializers import TopHeadlineSerializer
from rest_framework import generics
import datetime


def welcome(request):
    return HttpResponse('welcome')


# Create your views here.
class ListTopHeadline(generics.ListAPIView):
    queryset = Topheadline_detail.objects.all()
    serializer_class = TopHeadlineSerializer


class DetailTopHeadline(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topheadline_detail.objects.all()
    serializer_class = TopHeadlineSerializer


def refresh(request):
    extract_news()
    return HttpResponse('updated')

# def ref_object(request):
#
#     return HttpResponse('all refresh')
