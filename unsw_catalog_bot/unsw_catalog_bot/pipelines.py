# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from catalog.models import Course, Class, Meeting

class BotPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item.instance, Course):
            item = self.process_course(item, spider)
        elif isinstance(item.instance, Class):
            item = self.process_class(item, spider)
        elif isinstance(item.instance, Meeting):
            item = self.process_meeting(item, spider)
        else:
            pass    
        return item

    def process_course(self, item, spider):
        try:
            obj = Course.objects.get(**{k: item.get(k, None) for k in ('code', 'career', 'year', )})
            for key, value in item.iteritems():
                setattr(obj, key, value)
                obj.save()
        except Course.DoesNotExist:
            obj = Course(**item)
            obj.save()

        return item

    def process_class(self, item, spider):
        item_dict = dict(item) # convert to dict first so we can assign arbitrary fields
        course_identifier = item_dict.pop('course_identifier')
        course = Course.objects.get(**course_identifier)
        item_dict['course_id'] = course.id
        try:
            obj = Class.objects.get(**{k: item_dict.get(k, None) for k in ('class_nbr', )})
            for key, value in item_dict.iteritems():
                setattr(obj, key, value)
                obj.save()
        except Class.DoesNotExist:
            obj = Class(**item_dict)
            obj.save()

        return item

    def process_meeting(self, item, spider):
        item_dict = dict(item) # convert to dict first so we can assign arbitrary fields
        class_identifier = item_dict.pop('class_identifier')
        classe = Class.objects.get(**class_identifier)
        item_dict['classe_id'] = classe.id
        try:
            obj = Meeting.objects.get(**{k: item_dict.get(k, None) for k in ('day', 'time_start', 'location', 'weeks')})
            for key, value in item_dict.iteritems():
                setattr(obj, key, value)
                obj.save()
        except Meeting.DoesNotExist:
            obj = Meeting(**item_dict)
            obj.save()

        return item