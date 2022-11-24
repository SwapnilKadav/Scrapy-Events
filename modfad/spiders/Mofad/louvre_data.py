import pandas as pd
from bs4 import BeautifulSoup
import requests
import time


class LouvreData():
    def start_request(self, urls):
        name = []
        date = []
        link = []
        for url in urls:
            res = requests.get(url=url)
            link.append(url)
            try:
                soup =  BeautifulSoup(str(res.text))
                if soup.find("span",{"class":"Cover_subtitle"}):
                    string = ''
                    string = soup.find("span",{"class":"Cover_expo"}).text+' '+soup.find("span",{"class":"Cover_subtitle"}).text
                    name.append(string)
                    date.append(soup.find("p",{"class":"Cover_text"}).text if soup.find("p",{"class":"Cover_text"}).text is not None else 0)
                else:
                    name.append(soup.find("span",{"class":"Cover_expo"}).text if soup.find("span",{"class":"Cover_expo"}).text is not None else 0)
                    date.append(soup.find("p",{"class":"Cover_text"}).text if soup.find("p",{"class":"Cover_text"}).text is not None else 0)
            except Exception as e:
                print(e)  
        df = pd.DataFrame({'LINK':link,'NAME OF EVENT':name,'DATE':date}) 
        df.to_csv('louvre_data.csv', index=False, encoding='utf-8')
            
            