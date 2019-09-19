import scrapy
import pandas as pd

class LegoSpider(scrapy.Spider):
	name = 'legoSpider'
	start_urls = ['https://brickset.com/sets/year-2019']

	def parse(self,response):
		start_urls = ['https://brickset.com/sets/year-2019']
		SET_SELECTOR = '.set'
		for lego in response.css(SET_SELECTOR):
			NAME = 'h1 ::text'
			PIECES = './/dl[dt/text() = "Pieces"]/dd/a/text()'
			PRICES = './/dl[dt/text() = "RRP"]/dd/text()'



			yield {
			'name': lego.css(NAME).extract_first(),
			'pieces': lego.xpath(PIECES).extract_first(),
			'price': lego.xpath(PRICES).extract_first(),
			}
		for i in start_urls:
			yield scrapy.Request(url=i, callback=self.parse)

		follow_link = response.css('.next a ::attr(href)').extract_first()
		if follow_link:
			next_page = response.urljoin(follow_link)
			yield scrapy.Request(next_page,callback=self.parse)

