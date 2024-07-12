from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .models import Courses, Teachers, Students
from .serializers import CoursesSerializer, TeacherSerializer, StudentsSerializer


class CoursesView(ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [permissions.IsAdminUser]

class CoursesDestroyUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [permissions.IsAdminUser]


class TeacherView(ListCreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer


class TeacherDestroyUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer


class StudentsView(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StudentsDestroyUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
