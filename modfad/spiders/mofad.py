import scrapy
from bs4 import BeautifulSoup
# from .mofad.mofad_data import MofadData
from .Mofad.mofad_data import MofadData
class MofadSpider(scrapy.Spider):
    name = "mofad"
    start_urls = [
            
            'https://www.mofad.org/sitemap.xml',
        ]
      
    def parse(self, response):
        url=[]
        soup = BeautifulSoup(str(response.text))
        for i in soup.find_all('loc'):
            if 'https://www.mofad.org/calendar/' in str(i.text):
                url.append(i.text)
            else:
                continue
        MofadData.start_requests(self , urls= url)