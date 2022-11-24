import scrapy
from bs4 import BeautifulSoup
from .Mofad.louvre_data import LouvreData
class LouvreSpider(scrapy.Spider):
    name = "louvre"
    
    start_urls = [
            'https://www.louvre.fr/en/what-s-on/exhibitions'
        ]
    def parse(self, response):
        url = []
        soup = BeautifulSoup(response.text)
        link = soup.find_all('div', { "class", "Card_child"})
        for href in link:
            if href.find('h2',{ "class", "Card_Main_title"}):
                url.append('https://www.louvre.fr{}'.format(href.find('a',{ "class", "Card_Main_link extended-click"}).get('href')))
            elif href.find('h2',{ "class", "Card_Secondary_title louvre-24"}):
                url.append('https://www.louvre.fr{}'.format(href.find('a',{ "class", "Card_Secondary_link extended-click"}).get('href')))
        LouvreData.start_request(self, url)