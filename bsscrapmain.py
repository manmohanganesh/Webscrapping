from bs4 import BeautifulSoup
from selenium import webdriver
import json

headers = {
    'authority': 'www.amazon.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}
urls = ['https://www.amazon.in/s?k=mobile&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=laptops&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=headphones&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=shirt&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=pant&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=kurti&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=bat&ref=nb_sb_noss_2']


def write(path, filename, data):
    filepath = './' + path + '/' + filename + '.json'
    with open(filepath, 'a+') as fp:
        json.dump(data, fp)


def scrapping(link):
    driver = webdriver.Chrome("/usr/bin/chromedriver")
    driver.get(link)
    page_soup = BeautifulSoup(driver.page_source, 'html.parser')
    try:
        title = page_soup.find_all("span", {'class': 'a-size-medium a-color-base a-text-normal'})
        price = page_soup.find_all("span", {'class': 'a-price-whole'})
        dat = {title[i].text: price[i].text for i in range(len(title))}
        # write('./', 'scrapdata', dat) #If you want all product data in a single file
        write('./', link[26:-17], dat)

    except:
        print('Parsing error')


for j in range(len(urls)):
    name = urls[j]
    print("\n\nParsing through", name[26: -17])
    scrapping(urls[j])


