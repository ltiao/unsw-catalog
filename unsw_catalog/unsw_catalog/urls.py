from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from catalog.views import CourseViewSet

from django.contrib import admin
admin.autodiscover()

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'unsw_catalog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
