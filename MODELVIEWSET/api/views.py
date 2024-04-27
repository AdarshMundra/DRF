from .models import Student
from .serializers import StudentSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer