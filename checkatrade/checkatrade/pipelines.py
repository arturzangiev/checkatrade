# -*- coding: utf-8 -*-

from scrapy.contrib.exporter import CsvItemExporter


class CsvPipeline(object):
    def __init__(self):
        self.file = open("/home/ubuntu/checkatrade/checkatrade/checkatrade/output/items.csv", 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item