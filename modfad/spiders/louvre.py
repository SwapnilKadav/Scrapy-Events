import scrapy
import pandas as pd
class LouvreSpider(scrapy.Spider):
    name = "louvre"
    
    start_urls = [
            'https://www.louvre.fr/en/what-s-on/exhibitions'
        ]
    def parse(self, response):
        data = {}
        data['LINK'] = []
        data['NAME OF EVENT'] =[]
        data['DATE']=[]
        url_card = response.css('.extended-click')
        url = url_card.xpath('@href').extract()
        for href in url:
            data['LINK'].append('https://www.louvre.fr{}'.format(href))
        if response.css('a.Card_Main_link.extended-click::text').extract_first() is not None:
            if len(response.css('p.Card_Main_subtitle::text').extract()) > 0:
                data['NAME OF EVENT']+=response.css('a.Card_Main_link.extended-click::text').extract_first_()+' '+response.css('a.Card_Main_date::text').extract_first()
            data['NAME OF EVENT']+=response.css('a.Card_Main_link.extended-click::text').extract()
            data['DATE']+=response.css('p.Card_Main_date::text').extract()
        if response.css('a.Card_Secondary_link.extended-click::text').extract_first() is not None:
            if len(response.css('p.Card_Secondary_subtitle::text').extract())>0: 
                data['NAME OF EVENT']+=[response.css('a.Card_Secondary_link.extended-click::text').extract_first()+' '+response.css('p.Card_Secondary_subtitle::text').extract_first()]
            data['NAME OF EVENT']+=response.css('a.Card_Secondary_link.extended-click::text')[1:].extract()
            data['DATE']+=response.css('p.Card_Secondary_date::text').extract()
        df = pd.DataFrame(data) 
        df.to_csv('louvre_data.csv', index=False, encoding='utf-8')
        