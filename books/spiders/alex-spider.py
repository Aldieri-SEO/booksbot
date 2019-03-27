import urlparse
import scrapy
from scrapy.linkextractors import LinkExtractor

from scrapy.http import Request


class BooksSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["traghettilines"]
    #                 ^ allowed domain should be name of domain that you wanna scrap
    start_urls = (
        'https://www.traghettilines.it/',
    )

    def parse(self, response):
    # My Link Extractor
        next_page_urls = LinkExtractor(restrict_xpaths='//*[@class="next"]').extract_links(response)
        # This is how we use LinkExtractor or you can create spider Rule for next page.
        # Read more about LinkExtractor form https://doc.scrapy.org/en/latest/topics/link-extractors.html
        for next_page in next_page_urls:
            yield Request(next_page.url,callback=self.parse_item)

    def parse_item(self, response):
    # My Page Saver    
        filename = response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
            return
