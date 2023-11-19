# import libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import datetime

import smtplib

# connect website

URL = 'https://www.amazon.ca/Crucial-2x16GB-3200MT-Desktop-CP2K16G4DFRA32A/dp/B0C29R9LNL/ref=sr_1_2?crid=36NSIZRVO7ZKT&keywords=ram+stick&psr=EY17&qid=1700353734&s=black-friday&sprefix=ram+stick%2Cblack-friday%2C65&sr=1-2'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find(class_='a-offscreen').get_text()

rating = soup2.find(class_='a-size-base a-nowrap').get_text()

delivery_element = soup2.find(attrs={'data-csa-c-delivery-time': True})
delivery_text = delivery_element['data-csa-c-delivery-time']
#print(delivery_text)


#print(rating)

#Formatting Data
price = price.strip()
title = title.strip()
rating = rating.strip()
delivery_text = delivery_text.strip()
today = datetime.date.today()

#print (title)
#print (price)
#print(today)


#Creation of CSV File

import csv

header = ['Title', 'Price', 'Rating', 'Delivery Date', 'Date Accessed']
data = [title, price, rating, delivery_text, today]

with open('ProductDataScraper.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    

#Append CSV File
with open('ProductDataScraper.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

#Overall Function
def check_price():
    URL = 'https://www.amazon.ca/Crucial-2x16GB-3200MT-Desktop-CP2K16G4DFRA32A/dp/B0C29R9LNL/ref=sr_1_2?crid=36NSIZRVO7ZKT&keywords=ram+stick&psr=EY17&qid=1700353734&s=black-friday&sprefix=ram+stick%2Cblack-friday%2C65&sr=1-2'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(class_='a-offscreen').get_text()
    
    rating = soup2.find(class_='a-size-base a-nowrap').get_text()

    delivery_element = soup2.find(attrs={'data-csa-c-delivery-time': True})
    delivery_text = delivery_element['data-csa-c-delivery-time']

    price = price.strip()
    title = title.strip()
    rating = rating.strip()
    delivery_text = delivery_text.strip()
    
    today = datetime.date.today()
    
    header = ['Title', 'Price', 'Rating', 'Delivery Date', 'Date Accessed']
    data = [title, price, rating, delivery_text, today]

    with open('ProductDataScraper.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


while(True):
    check_price()
    time.sleep(86400) #How often you want the data checked



