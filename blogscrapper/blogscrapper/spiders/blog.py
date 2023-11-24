import scrapy
from blogscrapper.items import blogItem

class BlogSpider(scrapy.Spider):
    name = "blog"
    allowed_domains = ["rategain.com"]
    start_urls = ["https://rategain.com/blog"]

    custom_settings = {
        'FEEDS' :{
            'rategain.csv' : {'format':'csv', 'overwrite': True},
        }
    }

    def parse(self, response):
        articles = response.css('div.wrap')
        for article in articles:
            blog_item = blogItem()
            blog_title = article.css('.content h6 a::text').get()
            blog_date = article.css('div.content div.blog-detail div.bd-item span::text').get()
            blog_likes_count = article.css('div.content a.zilla-likes span::text').get()

            # Check if the image is present before attempting to extract the URL
            blog_image_url = article.css('.img a::attr(href)').get()
            if blog_image_url:
                blog_image_url = response.urljoin(blog_image_url)

            
            blog_item['blog_title'] = blog_title
            blog_item['blog_date'] = blog_date
            blog_item['blog_image_url'] = blog_image_url
            blog_item['blog_likes_count'] = blog_likes_count
            
            yield blog_item

        
        next_page = response.css('div.pagination.col-xs-12 a.next.page-numbers').attrib.get('href')

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
