# -*- coding: utf-8 -*-
import scrapy
# from scrapy.contrib.spiders import SitemapSpider
# from scrapy.selector import Selector
from urllib.parse import urlparse

from ecollect.scraper.items import EcollectItem


class MerySpider(scrapy.Spider):
    name = 'mery'
    allowed_domains = ['mery.jp']
    start_urls = [
        # 'https://mery.jp/1000745'
    ]
    sitemap_urls = [
        'https://mery.jp/sitemap-lists-beauty.xml.gz',
        'https://mery.jp/sitemap-lists-cosme.xml.gz',
        '>https://mery.jp/sitemap-lists-fashion.xml.gz',
        'https://mery.jp/sitemap-lists-gourmet.xml.gz',
        'https://mery.jp/sitemap-lists-hairstyle.xml.gz',
        'https://mery.jp/sitemap-lists-lifestyle.xml.gz',
        'https://mery.jp/sitemap-lists-love.xml.gz',
        'https://mery.jp/sitemap-lists-nail.xml.gz',
        'https://mery.jp/sitemap-lists-outing.xml.gz',
    ]

    custom_settings = {
        "DOWNLOAD_DELAY": 0.5,  # 0.5秒ごとにクロール
    }

    def parse(self, response):
        mery_item = EcollectItem()
        mery_item['title'] = response.xpath('//title/text()').extract_first()
        mery_item['body'] = response.body
        try:
            url = urlparse(response.css('#topBar li a')[1].attrib['href'])
            mery_item['category'] = url.path
        except Exception as e:
            pass

        mery_item['url'] = response.url
        return mery_item
