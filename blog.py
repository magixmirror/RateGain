import scrapy


class BlogSpider(scrapy.Spider):
    name = "blog"
    allowed_domains = ["rategain.com"]
    start_urls = ["https://rategain.com/blog"]

    def parse(self, response):
        pass
