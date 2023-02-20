from selenium import webdriver
from bs4 import BeautifulSoup
import tweepy



# url = 'https://forum.nexon.com/bluearchive/'
url2 = 'https://twitter.com/KR_BlueArchive/'

driver = webdriver.Edge('msedgedriver.exe')
# driver.get(url)

# soup = BeautifulSoup(driver.page_source, 'lxml')

# posts = soup.select('body div.main.main-type2 div.section-bot div.sticky-box a')
# print('넥슨 주요소식')
# print('----------------------------------------------------------------------')
# for post in posts:
#     category = post.find('span',class_= 'key-color').text.strip()
#     title = post.find('h3').text.strip()
#     icon = post.find('span',class_='icon-new')
#     link = post.get('href')
#     print(category,title,icon)
#     print(url+link)
# print('----------------------------------------------------------------------')

driver.get(url2)
soup = BeautifulSoup(driver.page_source, 'lxml')

