from rest_framework import serializers
from .models import NewsCat


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCat
        fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCat
        fields = '__all__'


class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCat
        fields = '__all__'


class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCat
        fields = '__all__'


class EntertainmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCat
        fields = '__all__'


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCat
        fields = '__all__'


class ScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCat
        fields = '__all__'
