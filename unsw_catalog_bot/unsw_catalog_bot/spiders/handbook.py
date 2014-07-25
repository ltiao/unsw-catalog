# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import log
import json
import re

class NewHandbookSpider(CrawlSpider):
    name = 'new-handbook'
    allowed_domains = ['unsw.edu.au']
    
    def process_javascript_link(value):
        mo = re.search(r"javascript:\s*doBrowse\('(?P<relpath>.*)',\s*'(?P<descr>.*)'\);", value)
        if mo:
            print mo.group('relpath')
            print mo.group('descr')
        return value
    
    rules = (
        Rule(
            LinkExtractor(
                allow = 'javascript',
                restrict_xpaths = "//div[@class='column nav-col']/div[@class='sideNavWrapper']/div[@class='sideNav']/ul",
                process_value = process_javascript_link
            ),
        ),
    )
    
    def __init__(self, year=None, careers=None, *args, **kwargs):
        super(NewHandbookSpider, self).__init__(*args, **kwargs)
        
        if careers is not None:
            # TODO: Further format checking
            self.careers = json.loads(careers) # careers.split(',')
        else:
            self.careers = 'undergraduate|postgraduate|research|nonaward'.split('|')
        
        if year is not None:
            # TODO: Further format checking
            self.year = year  
        else:
            self.year = 'current'
        
        self.start_urls = ['http://www.handbook.unsw.edu.au/{career}/{year}/'.format(career=career, year=self.year) for career in self.careers]


class HandbookSpider(CrawlSpider):
    name = 'handbook'
    allowed_domains = ['unsw.edu.au']
    start_urls = (
        'http://www.handbook.unsw.edu.au',
    )

    def process_value(value):
        print '####### ' + value
        return value

    def process_javascript_link(value):
        print '## Javascript original: {0}'.format(value)
        "javascript: doBrowse('/vbook2013/brProgramsByAtoZ.jsp','A');"
        
        return value

    rules = (
        Rule(
            LinkExtractor(
                # allow = '/(?:undergraduate|postgraduate|research|nonaward)/\d{4}/',
                allow = '/undergraduate/\d{4}/',
                restrict_xpaths = "//div[@class='column two-col']/div[@class='infoBox']/div[@class='infoBoxContent']",
                process_value = process_value
            ),
        ),
        Rule(
            LinkExtractor(
                allow = 'previousEditions\.html',
                restrict_xpaths = "//div[@class='rightButtons']",
                process_value = process_value
            ),
        ),
        Rule(
            LinkExtractor(
                allow = '/\d{4}/',
                restrict_xpaths = "//div[@class='internalContentWrapper']/div[4]/table",
                process_value = process_value
            ),
        ),
        Rule(
            LinkExtractor(
                # allow = '/\d{4}/',
                restrict_xpaths = "//div[@class='column nav-col']/div[@class='sideNavWrapper']/div[@class='sideNav']/ul",
                process_value = process_value
            ),
        ),
    )