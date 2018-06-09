# -*- coding: utf-8 -*-
import scrapy
# from ..items import EbayItem


class CheckatradeSpider(scrapy.Spider):
    name = "checkatrade1"
    allowed_domains = ["checkatrade.com"]
    start_urls = ['https://www.checkatrade.com/Directory/A']

    def parse(self, response):
        urls = response.xpath('//table[@class="directory"]/tbody/tr/td/a/@href').extract()[:30]
        for url in urls:
            full_url = response.urljoin(url)
            yield scrapy.Request(full_url, callback=self.individual_page)

    def individual_page(self, response):
        page_url = response.url
        contact_name = response.xpath('//div[@class="contact-card__contact-name"]/text()').extract_first().strip()
        company_name = response.xpath('//h1[@itemprop="name"]/text()').extract_first()
        address = response.xpath('//span[@itemprop="addressLocality"]/text()').extract_first()
        phone_number = response.xpath('//span[@itemprop="telephone"]/text()').extract_first()
        email = response.xpath('//a[@itemprop="email"]/text()').extract_first()

        yield {"test": page_url}


        # for box in boxs:
        #     id = box.xpath('.//a[@class="s-item__link"]/@href').re_first(r"^.+?/(\d+)\?.+$")
        #     name = box.xpath('.//h3[@class="s-item__title"]/text()').extract_first()
        #     orders = box.xpath('.//span[@class="NEGATIVE"]/text()').re_first(r"(\d+,*\d*) sold")
        #     if orders != None:
        #         orders = orders.replace(',', '')
        #     full_url = box.xpath('.//a[@class="s-item__link"]/@href').extract_first()
        #
        #     fields = EbayItem(id=id, name=name, orders=orders, url=full_url, parent_url=parent_url)
        #
        #     yield fields

            # Calling next page
            # next_page_url = response.xpath('//a[@rel="next"]/@href').extract_first()
            # yield scrapy.Request(next_page_url, callback=self.individual_page)