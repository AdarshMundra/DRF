from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    stuName = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100, validators=[start_with_v])

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.stuName = validated_data.get('stuName', instance.stuName)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # field level validation
    def validate_roll(self, value):
        if value > 200:
            raise serializers.ValidationError("Seat is full")
        return value

    # object level validation
    def validate(self, data):
        name = data['stuName']
        if name == "abc":
            raise serializers.ValidationError("not abc")
        return data

    # Validatar
    def start_with_v(value):
        if value[0]=='v':
            raise serializers.ValidationError("not v")

