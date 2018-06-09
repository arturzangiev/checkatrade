# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from ..items import CheckatradeItem


class SunshinetourSpider(scrapy.Spider):
    name = "checkatrade"
    allowed_domains = ["checkatrade.com"]
    start_urls = [
        'https://www.checkatrade.com/Directory/A',
        'https://www.checkatrade.com/Directory/B',
        'https://www.checkatrade.com/Directory/C',
        'https://www.checkatrade.com/Directory/D',
        'https://www.checkatrade.com/Directory/E',
        'https://www.checkatrade.com/Directory/F',
        'https://www.checkatrade.com/Directory/G',
        'https://www.checkatrade.com/Directory/H',
        'https://www.checkatrade.com/Directory/I',
        'https://www.checkatrade.com/Directory/J',
        'https://www.checkatrade.com/Directory/K',
        'https://www.checkatrade.com/Directory/L',
        'https://www.checkatrade.com/Directory/M',
        'https://www.checkatrade.com/Directory/N',
        'https://www.checkatrade.com/Directory/O',
        'https://www.checkatrade.com/Directory/P',
        'https://www.checkatrade.com/Directory/Q',
        'https://www.checkatrade.com/Directory/R',
        'https://www.checkatrade.com/Directory/S',
        'https://www.checkatrade.com/Directory/T',
        'https://www.checkatrade.com/Directory/U',
        'https://www.checkatrade.com/Directory/V',
        'https://www.checkatrade.com/Directory/W',
        'https://www.checkatrade.com/Directory/X',
        'https://www.checkatrade.com/Directory/Y',
        'https://www.checkatrade.com/Directory/Z',
        ]

    def __init__(self):
        # self._driver = webdriver.Chrome('/Users/artur/PycharmProjects/checkatrade/checkatrade/chromedriver')
        self._driver = webdriver.PhantomJS('/home/ubuntu/checkatrade/checkatrade/phantomjs')

    def parse(self, response):
        urls = response.xpath('//table[@class="directory"]/tbody/tr/td/a/@href').extract()
        for url in urls:
            full_url = response.urljoin(url)
            yield scrapy.Request(full_url, callback=self.individual_page)

    def individual_page(self, response):
        self._driver.get(response.url)
        page_code = Selector(text=self._driver.page_source)
        contact_name = page_code.xpath('//div[@class="contact-card__contact-name"]/text()').extract_first().strip()
        company_name = page_code.xpath('//h1[@itemprop="name"]/text()').extract_first()
        address = page_code.xpath('//span[@itemprop="addressLocality"]/text()').extract_first()
        phone_number = page_code.xpath('//span[@itemprop="telephone"]/text()').extract_first()
        email = page_code.xpath('//a[@itemprop="email"]/text()').extract_first()

        fields = CheckatradeItem(contact_name=contact_name,
                                 company_name=company_name,
                                 address=address,
                                 phone_number=phone_number,
                                 email=email)

        yield fields