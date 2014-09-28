from django.conf.urls import url
from catalog.views import YearList, CourseList, CourseDetail

urlpatterns = [
	url(r'^$', YearList.as_view(), name='index'),
	url(r'^(?P<year>\d{4})/(?P<career>\w+)/$', CourseList.as_view(), name='course-index'),
	url(r'^(?P<year>\d{4})/(?P<career>\w+)/(?P<code>\w{8})/$', CourseDetail.as_view(), name='course-detail'),
]