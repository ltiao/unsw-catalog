from django.conf.urls import url
from catalog.views import YearList, CourseList

urlpatterns = [
	url(r'^$', YearList.as_view(), name='index'),
	url(r'^(?P<year>\d{4})/(?P<career>\w+)/', CourseList.as_view(), name='course-index'),
]