# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlogscrapperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass



class blogItem(scrapy.Item):
    blog_title = scrapy.Field()
    blog_date = scrapy.Field()
    blog_image_url = scrapy.Field()
    blog_likes_count = scrapy.Field()



