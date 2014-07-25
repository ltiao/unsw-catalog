# -*- coding: utf-8 -*-

# Scrapy settings for unsw_catalog_bot project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import sys
from unipath import Path

PROJECT_DIR = Path(__file__).ancestor(3)

# Setting up Django project root path.
sys.path.insert(0, PROJECT_DIR.child('unsw_catalog'))

BOT_NAME = 'unsw_catalog_bot'

SPIDER_MODULES = ['unsw_catalog_bot.spiders']
NEWSPIDER_MODULE = 'unsw_catalog_bot.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'unsw_catalog_bot (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'unsw_catalog_bot.pipelines.BotPipeline': 1,
}