from rest_framework import serializers
from .models import Stundet

class StudentSerializer(serializers.Serializer):
    stuName = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Stundet.objects.create(**validated_data)
