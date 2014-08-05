from django.conf.urls import url
from catalog.views import CourseList

urlpatterns = [
	url(r'^$', CourseList.as_view(), name='course-index'),
]