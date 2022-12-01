import scrapy
import json
import pandas as pd
from modfad.items import ModfadItem
class ConnaughtSpider(scrapy.Spider):
    name = 'connaught'
    start_urls = [ 'https://www.the-connaught.co.uk/the-season/search/?page=1&pagesize=9&tags=&month=']
    
    def parse(self, response):
        data = ModfadItem()
        data['LINK'] = []
        data['NAME_OF_EVENT'] =[]
        data['DATE']=[]
        api_data = json.loads(response.body)
        for fild in api_data['Documents']:
            data['LINK'].append(fild['CanonicalUrl'])
            data['NAME_OF_EVENT'].append(fild['Title'])
            data['DATE'].append(fild['DisplayDate'])
        df = pd.DataFrame(dict(data)) 
        df.to_csv('connaught_data.csv', index=False, encoding='utf-8')
        
        yield data
            