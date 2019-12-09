# -*- coding: utf-8 -*-
import scrapy

dictionary = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5}
pages = 5
class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/page-{}.html'.format(i+1) for i in range(pages)]

    def parse(self, response):
        data={}
        books=response.css('ol.row')
        for book in books:
            for b in book.css('article.product_pod'):
                data['title'] = b.css('a::attr(title)').getall()
                data['price'] = b.css('div.product_price p.price_color::text').getall()
                data['stock'] = b.css('div.product_price p.instock.availability::text').getall()[1].strip()
                data['star'] = b.css('p::attr(class)').getall()[0].split()[-1]
                data['star'] = [v for k,v in dictionary.items() if k in data['star']][0]
                yield data
