from django.shortcuts import render
from django.http import HttpResponse
from .models import extract_news, Topheadline_detail
from .serializers import TopHeadlineSerializer
from rest_framework import generics
import datetime


# Create your views here.
class ListTopHeadline(generics.ListAPIView):
    extract_news()
    queryset = Topheadline_detail.objects.all()
    serializer_class = TopHeadlineSerializer


class DetailTopHeadline(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topheadline_detail.objects.all()
    serializer_class = TopHeadlineSerializer


# def ref_object(request):
#
#     return HttpResponse('all refresh')
