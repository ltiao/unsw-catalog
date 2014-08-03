from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from catalog.views import CourseViewSet
from views import HomeView

from django.contrib import admin
admin.autodiscover()

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^catalog/', include('catalog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^api/', include(router.urls)),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
)