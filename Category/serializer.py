from rest_framework import serializers
from .models import *


class SportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = sports_news
        # fields = ('source', 'author', 'title', 'description', 'url', 'UrlToImage', 'PublishedAt', 'content')
        fields = '__all__'

#
# class businessSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = business_news
#         # fields = ('source', 'author', 'title', 'description', 'url', 'UrlToImage', 'PublishedAt', 'content')
#         fields = '__all__'
#
#
# class entertainmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = entertainment_news
#         # fields = ('source', 'author', 'title', 'description', 'url', 'UrlToImage', 'PublishedAt', 'content')
#         fields = '__all__'
#
#
# class generalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = general_news
#         # fields = ('source', 'author', 'title', 'description', 'url', 'UrlToImage', 'PublishedAt', 'content')
#         fields = '__all__'
#
#
# class healthSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = health_news
#         # fields = ('source', 'author', 'title', 'description', 'url', 'UrlToImage', 'PublishedAt', 'content')
#         fields = '__all__'
#
#
# class scienceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = science_news
#         # fields = ('source', 'author', 'title', 'description', 'url', 'UrlToImage', 'PublishedAt', 'content')
#         fields = '__all__'
#
#
# class technologySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = technology_news
#         # fields = ('source', 'author', 'title', 'description', 'url', 'UrlToImage', 'PublishedAt', 'content')
#         fields = '__all__'
