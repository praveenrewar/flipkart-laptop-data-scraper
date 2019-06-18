import requests
from bs4 import BeautifulSoup
import numpy
import pandas as pd

products = []
prices = []
configs = []
ratings = []
url = "https://www.flipkart.com/laptops/pr?sid=6bo,b5g&marketplace=FLIPKART&page="
page = 1
while True:
    soup = BeautifulSoup(requests.get(
        url+str(page)).content, features="html.parser")
    if (soup.find('a', href=True, attrs={'class': '_31qSD5'}) == None):
        break
    for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
        name = a.find('div', attrs={'class': '_3wU53n'})
        price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
        config = a.find('div', attrs={'class': '_3ULzGw'})
        rating = a.find('div', attrs={'class': 'hGSR34'})
        products.append(name.text)
        prices.append(price.text)
        configs.append(config.text)
        if (rating == None):
            ratings.append("Not Available")
        else:
            ratings.append(rating.text)
    page += 1

df = pd.DataFrame({'Product Name': products, 'Price': prices,
                   'Configuration': configs, 'Customer Rating': ratings})
df.to_csv('laptops.csv', index=False, encoding='utf-8')
