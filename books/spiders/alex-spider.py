# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "Alex-Bot"
    allowed_domains = ["traghettiper-isole-golfo-napoli.it"]
    start_urls = [
        'https://www.traghettiper-isole-golfo-napoli.it/',
    ]

    def parse_book_page(self, response):
        item = {}
        item["title"] = product.css("h1 ::text").extract_first()
        item['category'] = response.xpath(
            "/html/body/div[2]/div/div[1]/ol/span/span/a"
        ).extract_first()
        item['description'] = response.xpath(
            "//div[@id='product_description']/following-sibling::p/text()"
        ).extract_first()
        item['price'] = response.css('p.price_color ::text').extract_first()
        yield item
