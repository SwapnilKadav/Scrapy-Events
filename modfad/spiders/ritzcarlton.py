
import scrapy
import pandas as pd
class LouvreSpider(scrapy.Spider):
    name = "ritzcarlton"
    
    start_urls = [
            'https://www.ritzcarlton.com/content/TRC-LiveCopy/en/hotels/china/hong-kong/hotel-overview/calendar/jcr:content/par_content/events.filteredComponent.html'
        ]
    def parse(self, response):
        data = {}
        data['LINK'] = []
        data['NAME_OF_EVENT'] =[]
        data['DATE']=[]
        for url in response.css('a::attr(href)').getall():
            if 'https://' not in url:
                data['LINK'].append('None')
            else:
                data['LINK'].append(url)
        data['NAME_OF_EVENT'] = response.css('h3::text').extract()
        card_data = response.xpath('/html/body/div[2]/div/div/div')
        for card in card_data:
                day  = card.css('p.day::text').extract_first()
                date = card.css('p.dates::text').extract_first()
                time = card.css('p.time::text').extract_first()
                data['DATE'].append(f'{day}, {date}, {time}')
        df = pd.DataFrame(data)
        df.to_csv('ritzcarlton_data.csv', index=False, encoding='utf-8')
        yield data