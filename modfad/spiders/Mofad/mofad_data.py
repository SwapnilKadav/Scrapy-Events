import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
class MofadData():
    def start_requests(self, urls):
        name = []
        date = []
        link = []
        for url in urls:
            res = requests.get(url=url)
            link.append(url)
            try:
                soup =  BeautifulSoup(str(res.text))
                name.append(soup.find("h1",{"class":"eventitem-title"}).text if soup.find("h1",{"class":"eventitem-title"}).text is not None else 0)
                date.append(soup.find("time",{"class":"event-date"}).text if soup.find("time",{"class":"event-date"}).text is not None else 0)
            except:
                if res.status_code == 429:
                    time.sleep(100)
                    res = requests.get(url=url)
                    soup =  BeautifulSoup(str(res.text))
                    name.append(soup.find("h1",{"class":"eventitem-title"}).text if soup.find("h1",{"class":"eventitem-title"}).text is not None else 0)
                    date.append(soup.find("time",{"class":"event-date"}).text if soup.find("time",{"class":"event-date"}).text is not None else 0)
                else:
                    pass
        df = pd.DataFrame({'LINK':link,'NAME OF EVENT':name,'DATE':date}) 
        df.to_csv('mofad_data.csv', index=False, encoding='utf-8')