from django.shortcuts import render
from .models import get_recommend, recommender_user
from rest_framework import generics
from .serializers import ReccomendSerializer


# Create your views here.
def user_reccomend(request):
    get_recommend(request.GET['user'])
    return ListRecommend.as_view()


class ListRecommend(generics.ListAPIView):
    queryset = recommender_user.objects.all()
    serializer_class = ReccomendSerializer
