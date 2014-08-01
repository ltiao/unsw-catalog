from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from catalog.models import Course
from catalog.serializers import CourseSerializer

class CourseViewSet(ModelViewSet):
		queryset = Course.objects.all()
		serializer_class = CourseSerializer