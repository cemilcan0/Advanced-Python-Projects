from os import link
from typing import Counter
import requests
from bs4 import BeautifulSoup

#I chose monster.com to improve myself in the requests and bs4 libraries.
class select():
    def __init__(self):
        self.url="https://www.monsternotebook.com.tr/" 
        self.model_list=[]
        self.price_list=[]
        self.score_list=[]
        self.number=1
        
    def abra(self):
        url = self.url+"abra/"
        self.calc(url)
        self.number=1
        self.model_list=[]
        self.price_list=[]
        self.score_list=[]

    def tulpar(self):
        url = self.url+"tulpar/"
        self.calc(url)
        self.number=1
        self.model_list=[]
        self.price_list=[]
        self.score_list=[]


    def semruk(self):
        url = self.url+"semruk/"
        self.calc(url)
        self.number=1
        self.model_list=[]
        self.price_list=[]
        self.score_list=[]
        

    def scores_list(self,scores):
        for i in scores:
            if i.find("span",{"class": "toplamPuan"}):
                score=i.find("span",{"class": "toplamPuan"}).text.strip()
                self.score_list.append(score)
            else:
                self.score_list.append(0)
        return self.score_list
            
    def models_list(self,models):
        for sira, marka_div in enumerate(models):
            model = marka_div.text.strip()
            self.model_list.append(model)
        return self.model_list

            
    def prices_list(self,prices):
        for i in prices:
            price=i.text.strip()
            self.price_list.append(price)
        return self.price_list     
                
            

    
    def calc(self,url):
        link = requests.get(url).content
        soup = BeautifulSoup(link,"html.parser")
        models =soup.find_all("div",{"id" : "plhUrun_urunKodu"})
        prices = soup.find_all("div",{"class" : "urunListe_satisFiyat"})
        scores = soup.find("ul",{"class": "emosInfinite ems-inline"})
        a = self.models_list(models)
        b = self.prices_list(prices)
        c = self.scores_list(scores)
    
        for x,y,z in zip(a,b,c):
            print(f'{self.number}-) {x.ljust(60)} {str(y).ljust(15)}Ürün Puanı:5/{z}')
            self.number+=1        



model_select=select()

while True:
    model=int(input("Monster Notebook Model Selection:\n1-Abra\n2-Tulpar\n3-Semruk\n4-Quit\n"))
    if model==1:
        model_select.abra()
    elif model==2:
        model_select.tulpar()
    elif model==3:
        model_select.semruk()
    else:
        break