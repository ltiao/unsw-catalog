# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Identity, TakeFirst, MapCompose
from scrapy import Spider, Request
from unsw_catalog_bot.items import CourseItem, ClassItem, MeetingItem
from urlparse import urlparse
from dateutil import parser as date_parser
import posixpath as ppath
import datetime
import json
import re

class HandbookSpider(CrawlSpider):
    name = 'handbook'
    allowed_domains = ['unsw.edu.au']

    rules = (
        Rule(
            # every link in the table defined by the xpath
            LinkExtractor(
                allow = 'courses/\d{4}/[A-Z]{4}\d{4}\.html',
                restrict_xpaths = "//div[@class='column content-col']/div[@class='internalContentWrapper']/table[@class='tabluatedInfo']",
            ),
            callback = 'parse_course_item'
        ),
    )

    def __init__(self, year=None, careers=None, *args, **kwargs):
        super(HandbookSpider, self).__init__(*args, **kwargs)
        
        if careers is not None:
            # TODO: Further format checking
            self.careers = json.loads(careers) # careers.split(',')
        else:
            self.careers = 'undergraduate postgraduate research'.split()
        
        if year is not None:
            # TODO: Further format checking
            self.year = year  
        else:
            # TODO: Set default to current year
            self.year = 'current'

        self.start_urls = ['http://www.handbook.unsw.edu.au/vbook{year}/brCoursesByAtoZ.jsp?StudyLevel={level}&descr={descr}' \
            .format(year=self.year, level=career, descr='V') for career in self.careers]
    
    def parse_course_item(self, response):
        url_obj = urlparse(response.url)
        l = ItemLoader(item=CourseItem(), response=response)
        l.default_input_processor = MapCompose(unicode.strip)
        l.default_output_processor = TakeFirst()
        l.add_xpath('code', "/html/head/meta[@name='DC.Subject.ProgramCode']/@content")
        l.add_xpath('name', "/html/head/meta[@name='DC.Subject.Description.Short']/@content")
        l.add_xpath('career', "/html/head/meta[@name='DC.Subject.Level']/@content")
        l.year_in = Identity()
        l.add_value('year', ppath.basename(ppath.dirname(url_obj.path)))
        l.add_value('src_url', unicode(response.url))
        l.add_xpath('uoc', "/html/head/meta[@name='DC.Subject.UOC']/@content")
        l.gened_in = MapCompose(unicode.strip, lambda s: s == 'Y')
        l.add_xpath('gened', "/html/head/meta[@name='DC.Subject.GenED']/@content")
        l.add_xpath('faculty', "/html/head/meta[@name='DC.Subject.Faculty']/@content")
        l.add_xpath('school', ( "//div[@class='column content-col']/div[@class='internalContentWrapper']"
                                "/div[@class='summary']/p[strong[text()[contains(.,'School')]]]/a/text()"))
        l.add_xpath('campus', ( "//div[@class='column content-col']/div[@class='internalContentWrapper']"
                                "/div[@class='summary']/p[strong[text()[contains(.,'Campus')]]]/text()"))
        l.add_xpath('eftsl', ( "//div[@class='column content-col']/div[@class='internalContentWrapper']"
                                "/div[@class='summary']/p[strong[text()[contains(.,'EFTSL')]]]/text()"))
        l.add_xpath('description_markup', ( "//div[@class='column content-col']/div[@class='internalContentWrapper']"
                                            "/h2[text()='Description']/following-sibling::div"))
        course_item = l.load_item()
        yield course_item
        yield Request(url=response.xpath(("//div[@class='column content-col']/div[@class='internalContentWrapper']"
                                        "/div[@class='summary']//a[text()[contains(.,'Timetable')]]/@href")).extract()[0], 
                        callback=self.parse_class_item, 
                        meta=dict(course_identifier={k: course_item.get(k, None) for k in ('code', 'career', 'year', )}))

    def parse_class_item(self, response):
        course_identifier = response.meta.get('course_identifier')
        for sem in response.xpath(( "//table[tr[td[@class='classSearchSectionHeading']"
                                    "[text()[contains(.,'Detail')]]]]/following-sibling::table[1]")):
            for class_detail in sem.xpath("tr/td[@class='formBody']/table"):
                l = ItemLoader(item=ClassItem(), selector=class_detail)
                l.default_input_processor = MapCompose(unicode.strip)
                l.default_output_processor = TakeFirst()
                l.add_xpath('class_nbr', "tr/td[@class='label'][text()='Class Nbr']/following-sibling::td[@class='data'][1]/text()")
                l.add_xpath('activity', "tr/td[@class='label'][text()='Activity']/following-sibling::td[@class='data'][1]/text()")
                l.add_xpath('section', "tr/td[@class='label'][text()='Section']/following-sibling::td[@class='data'][1]/text()")
                l.add_xpath('teaching', "tr/td[@class='label'][a[text()='Teaching Period']]/following-sibling::td[@class='data'][1]/text()")
                l.add_xpath('status', "tr/td[@class='label'][text()='Status']/following-sibling::td[@class='data'][1]/font/text()")
                l.add_xpath('enrolments', "tr/td[@class='label'][text()='Enrols/Capacity']/following-sibling::td[@class='data'][1]/text()", re=r'(\d+)/\d+')
                l.add_xpath('capacity', "tr/td[@class='label'][text()='Enrols/Capacity']/following-sibling::td[@class='data'][1]/text()", re=r'\d+/(\d+)')
                l.offering_start_in = l.offering_end_in = l.updated_in = l.census_date_in = MapCompose(date_parser.parse)
                l.add_xpath('offering_start', "tr/td[@class='label'][text()='Offering Period']/following-sibling::td[@class='data'][1]/text()", re=r'([\d/]*)\s-\s[\d/]*')
                l.add_xpath('offering_end', "tr/td[@class='label'][text()='Offering Period']/following-sibling::td[@class='data'][1]/text()", re=r'[\d/]*\s-\s([\d/])*')
                l.add_xpath('census_date', "tr/td[@class='label'][a[text()='Census Date']]/following-sibling::td[@class='data'][1]/text()")
                l.add_xpath('consent', "tr/td[@class='label'][text()='Consent']/following-sibling::td[@class='data'][1]/text()")
                l.add_xpath('mode', "tr/td[@class='label'][text()='Instruction Mode']/following-sibling::td[@class='data'][1]/text()")
                l.add_value('src_url', unicode(response.url))
                l.add_xpath('updated', "//td[@class='note'][text()[contains(., 'Data is correct as at')]]/text()", 
                    re=r'Data is correct as at ([\w\s\-:,]*)')
                l.course_identifier_in = Identity()
                l.add_value('course_identifier', course_identifier)
                class_item = l.load_item()
                yield class_item
                for meeting in class_detail.xpath("tr/td[@class='formBody']/table/tr[@class='rowHighlight' or @class='rowLowlight']"):
                    m = MeetingItem()
                    m['class_identifier'] = {k: class_item.get(k, None) for k in ('class_nbr', )}
                    
                    d = dict(
                        zip(
                            ('day', 'time', 'location', 'weeks', 'instructor'), 
                            meeting.xpath("td[@class='data']/text()").extract()
                        )
                    )

                    time = d.pop('time')
                    d['time_start'], d['time_end'] = time.split(' - ')

                    m.update(d)

                    yield m
