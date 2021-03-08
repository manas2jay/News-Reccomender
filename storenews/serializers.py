from rest_framework import serializers
from .models import user_news


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_news
        #fields = ('source', 'author', 'title', 'description', 'url', 'UrlToImage', 'PublishedAt', 'content')
        fields = '__all__'
