# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy

class StyleSpider(scrapy.Spider):
    name = 'style_spider'
    
    def __init__(self, url='', **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [url]

    def parse(self, response):
        # Extract and print <style> tags
        style_tags = response.css('style').getall()
        print("\nStyle Tags:")
        for tag in style_tags:
            print(tag)

        # Extract and print inline styles
        inline_styles = response.css('[style]').getall()
        print("\nInline Styles:")
        for tag in inline_styles:
            print(tag)

