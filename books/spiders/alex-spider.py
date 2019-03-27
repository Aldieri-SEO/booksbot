# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "Alex-tool"
    allowed_domains = ["https://www.traghettiper-isole-golfo-napoli.it/"]
    start_urls = ['https://www.traghettiper-isole-golfo-napoli.it']
    
rules = (
        Rule(LinkExtractor(allow=('tp-magazine', )),
    )
def parse_items(self, response):
        item = UrlscraperItem()
        item['url'] = response.url
        item['status'] = response.status
        item['referer'] = response.request.headers.get('Referer', None)
        item['title'] = response.xpath('/html/head/title/text()').extract()
        item['description'] = response.xpath('/html/head/meta[@name="description"]/@content').extract()
        yield item
