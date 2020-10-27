# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'PaItem'
    id = scrapy.Field()
    node_id = scrapy.Field()
    name = scrapy.Field()
    full_name = scrapy.Field()
    private = scrapy.Field()

    url = scrapy.Field()
    pulls_url = scrapy.Field()

