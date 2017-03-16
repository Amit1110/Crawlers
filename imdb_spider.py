import scrapy

class ImdbSpider(scrapy.Spider):
	name = "imdb"
	start_urls = [
	'http://www.imdb.com/chart/boxoffice',
	]

	def parse(self, response):
		for cs in response.css('tr'):
				if(cs.css('td.titleColumn a::text').extract_first() is not None):
					yield{
						'name':cs.css('td.titleColumn a::text').extract_first(),
						'colthis':cs.css('td.ratingColumn::text').extract_first().strip(),
						'colwhole':cs.css('td.ratingColumn span.secondaryInfo::text').extract_first(),
						'weeks':cs.css('td.weeksColumn::text').extract_first(),
						}


		

