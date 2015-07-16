# -*- coding: utf-8 -*-

# Scrapy settings for bcc_ingredients project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bbc_ingredients'

SPIDER_MODULES = ['bbc_ingredients.spiders']
NEWSPIDER_MODULE = 'bbc_ingredients.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bcc_ingredients (+http://www.yourdomain.com)'

# @chiarluc
# DOWNLOAD_DELAY = 0.10 # 10 QPS