from rest_framework import serializers
from .models import Topheadline_detail


class TopHeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topheadline_detail
        #fields = ('source', 'author', 'title', 'description', 'url', 'UrlToImage', 'PublishedAt', 'content')
        fields = '__all__'
