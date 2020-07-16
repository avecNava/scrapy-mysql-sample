# -*- coding: utf-8 -*-
import scrapy
from ..items import QuotesItem

class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    # allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        items = QuotesItem()
        all_div_quotes = response.css("div.quote")

        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags = quote.css("a.tag::text").extract()
             
            items['title'] = title.strip(u'\u201c\u201d')     #strip unicode chars u'\u201c\u201d 
            # items['title'] = title     
            items['author'] = author
            items['tag'] = ", ".join(str(x) for x in tags)      #convert list to string separated by commas

            yield items

    # def parse(self, response):
    #     # title = response.css('title::text').extract()
    #     # title = all_div_quotes.css('span.text::text').extract()
    #     # author = all_div_quotes.css('.author::text').extract()
    #     # tags = all_div_quotes.css("a.tag::text").extract()
    #     # yield {'titletext' : title}

    #     all_div_quotes = response.css("div.quote")

    #     for quote in all_div_quotes:
    #         title = quote.css('span.text::text').extract()
    #         author = quote.css('.author::text').extract()
    #         tag = quote.css("a.tag::text").extract()
            
    #         yield {
    #             'title' : title,
    #             'author' : author,
    #             'tag' : tag
    #         }
