from bs4 import BeautifulSoup
import pandas as pd
import time
import requests
from scrapy.spiders import SitemapSpider
from modfad.items import ModfadItem
class MofadSpider(SitemapSpider):
    name = "mofad"
    allowed_domains = ['https://www.mofad.org']
    sitemap_urls = ['https://www.mofad.org/sitemap.xml']
    
    def sitemap_filter(self, entries):
        c=0
        data = ModfadItem()
        data['LINK'] = []
        data['NAME_OF_EVENT'] = []
        data['DATE']= []
        for entry in entries:
            if 'https://www.mofad.org/calendar/' in str(entry['loc']):
                res = requests.get(entry['loc'])
                data['LINK'].append(entry['loc'])
                try:
                    soup =  BeautifulSoup(str(res.text))
                    data['NAME_OF_EVENT'].append(soup.find("h1",{"class":"eventitem-title"}).text if soup.find("h1",{"class":"eventitem-title"}).text is not None else 0)
                    data['DATE'].append(soup.find("time",{"class":"event-date"}).text if soup.find("time",{"class":"event-date"}).text is not None else 0)
                except:
                    if res.status_code == 429:
                        time.sleep(100)
                        res = requests.get(url=entry['loc'])
                        soup =  BeautifulSoup(str(res.text))
                        data['NAME_OF_EVENT'].append(soup.find("h1",{"class":"eventitem-title"}).text if soup.find("h1",{"class":"eventitem-title"}).text is not None else 0)
                        data['DATE'].append(soup.find("time",{"class":"event-date"}).text if soup.find("time",{"class":"event-date"}).text is not None else 0)
                    else:
                        pass
            try:
                df = pd.DataFrame(data) 
                df.to_csv('mofad_data.csv', index=False, encoding='utf-8')
            except:
                pass
        yield data
          
