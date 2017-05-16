import requests
from bs4 import BeautifulSoup
import feedparser
from pymongo import MongoClient

client = MongoClient() #connect mongoclient to an instance of mogod
db = client.webevents #create a db test

#collections = db["sample"]

def trade_spider():
    info  =' '
    url="http://www.eventsdoha.com/the-backyard-the-end-of-the-seadon-19th-may-sheraton-gran/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for d in soup.find_all('p'):
        print d.text
        #info = str(div_tag.text)+str(div_tag.next_sibling)
        #print "hello"
        #info.append(d.text)
        info =info + d.text + "\n"
    details = {"information": info}
    print "***********"
    results2 = db.eventinfor.insert_one(details)
    results2.inserted_id
        # for link in soup.find_all('p', ):
        #   href = link.get('href')
        #  print(href)
    return 0

trade_spider()