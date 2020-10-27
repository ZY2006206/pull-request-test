import scrapy
import json
from pa.items import PaItem
import time


class SpiSpider(scrapy.Spider):
    name = 'spi'
    allowed_domains = ['api.github.com']
    start_urls = ['https://api.github.com/']

    def start_requests(self): # 生成初始请求，返回可迭代对象
        base_url = 'https://api.github.com/repos/'
        for rank in range(0, self.settings.get('PA_NUM')):
            cur_url = base_url + self.settings.get('PA_LIST')[rank][0] + '/' + self.settings.get('PA_LIST')[rank][1]
            self.logger.debug(cur_url)
            time.sleep(3.0)
            yield scrapy.Request(cur_url, self.parse)

    def parse(self, response):
        # print(type(response.text))
        result = json.loads(response.text)
        item = PaItem()
        item['id'] = result['id']
        item['node_id'] = result['node_id']
        item['name'] = result['name']
        item['full_name'] = result['full_name']
        item['private'] = result['private']
        item['url'] = result['url']
        item['pulls_url'] = result['pulls_url']
        yield item