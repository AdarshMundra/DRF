from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == "GET":
        # id = request.data.get(id)
        data = request.data
        if 'id' in data:
            id = data[id]
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)
    if request.method == "POST":
        print(request.data)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'})
        return Response(serializer.errors)
    if request.method == "PUT":
        print(request.data)
        data = request.data
        if 'id' in data:
            id = data["id"]
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'data updated'})
            return Response(serializer.errors)
    if request.method == "DELETE":
        print(request.data)
        data = request.data
        if 'id' in data:
            id = data["id"]
            stu = Student.objects.get(id=id)
            stu.delete()
            return Response({'msg': 'data deleted'})

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api1(request,pk=None):
    if request.method == "GET":
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)
    if request.method == "POST":
        print(request.data)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data created'})
        return Response(serializer.errors)
    if request.method == "PUT":
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data updated'})
        return Response(serializer.errors)
    if request.method == "DELETE":
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'data deleted'})
