from rest_framework import serializers
from .models import recommender_user


class ReccomendSerializer(serializers.ModelSerializer):
    class Meta:
        model = recommender_user
        #fields = ('source', 'author', 'title', 'description', 'url', 'UrlToImage', 'PublishedAt', 'content')
        fields = '__all__'
