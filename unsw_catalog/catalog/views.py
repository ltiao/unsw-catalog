from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework.viewsets import ModelViewSet
from catalog.models import Course, Class, Meeting
from catalog.serializers import CourseSerializer



class CourseList(ListView):
    model = Course
    queryset = Course.objects.all()[:25]
    context_object_name = 'course_list'

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer