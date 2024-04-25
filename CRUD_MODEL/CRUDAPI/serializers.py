from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    # stuName = serializers.CharField(read_only=True)

    class Meta:
        model = Student
        # field = ['stuName','roll','city']
        fields = '__all__'
        read_only_field = ['stuName']