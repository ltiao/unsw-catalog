from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from rest_framework.viewsets import ModelViewSet
from catalog.models import Course, Class, Meeting
from catalog.serializers import CourseSerializer

class YearList(TemplateView):

	template_name = 'catalog/index.html'

	def get_context_data(self, **kwargs):
		context = super(YearList, self).get_context_data(**kwargs)
		# `order_by` in conjunction with `distinct` 
		# supported by postgres only 
		context['year_career_list'] = Course.objects.order_by('year', 'career').values('year', 'career').distinct()
		return context

class CourseList(ListView):
    model = Course
    queryset = Course.objects.all()
    context_object_name = 'course_list'

    def get_queryset(self):
        return super(CourseList, self).get_queryset() \
        	.filter(year=self.kwargs['year'], career__iexact=self.kwargs['career'])

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer