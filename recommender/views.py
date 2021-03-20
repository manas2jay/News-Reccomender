from django.shortcuts import render
from .models import get_recommend, recommender_user
from rest_framework import generics
from .serializers import ReccomendSerializer
from django.http import HttpResponse


# Create your views here.
def user_reccomend(request):
    get_recommend(request.GET['user'])
    return HttpResponse('hmm')


class ListRecommend(generics.ListAPIView):
    queryset = recommender_user.objects.all()
    serializer_class = ReccomendSerializer

def deleterec(request):
    recommender_user.objects.all().delete()
    return HttpResponse('all recc is delete')