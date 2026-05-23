"""
web scrapping
"""

"""step1 Crawl"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://quotes.toscrape.com/"

header={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

response=requests.get(url,headers=header)
data=BeautifulSoup(response.text,'html.parser')

"""step2 parse and transform"""

card_data=data.find_all('div',attrs={'class':"quote"})

''' step 3 store'''
scrapped_text=[]

for card in card_data:
    details={}
    quote=card.find('span',attrs={'class':'text'})
    author=card.find('small' ,attrs={'class':'author'})
    details['quote']=quote.text
    details['author']=author.text

    scrapped_text.append(details)

#create datafram from list of dictonaries
dataframe=pd.DataFrame.from_dict(scrapped_text)
print(dataframe.to_string())
dataframe.to_csv('quotes_data.csv', index=False)
    

