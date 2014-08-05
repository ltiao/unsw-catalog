from rest_framework.serializers import HyperlinkedModelSerializer
from catalog.models import Course, Class, Meeting

class CourseSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Course
        fields = ('code', 'name', 'career', 'year', 'faculty', 'school', 
        			'campus', 'description_markup', 'url')

class ClassSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Class