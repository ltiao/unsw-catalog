# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.contrib.djangoitem import DjangoItem
from scrapy.item import Field

from catalog.models import Course

class CourseItem(DjangoItem):
    django_model = Course