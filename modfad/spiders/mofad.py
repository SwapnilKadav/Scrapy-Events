import scrapy
import time
from scrapy.spiders import SitemapSpider
class MofadSpider(SitemapSpider):
    name = "mofad"
    sitemap_urls = ['https://www.mofad.org/sitemap.xml', ]
    
    def parse(self, response):
        try:
            if response.status == 429:
                time.sleep(60)
                yield scrapy.Request(response, callback=self.parse)
        except:
            pass
        if 'https://www.mofad.org/calendar/' ==  str(response.url):
            pass
        elif 'https://www.mofad.org/calendar/' in str(response.url):
            link = response.url
            name = response.css('h1.eventitem-title::text').extract_first()
            date = response.css('time.event-date::text').extract_first()
            if link and name and date :
                
                yield {'LINK':[link], 'NAME_OF_EVENT':[name], 'DATE':[date]}