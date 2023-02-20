import requests as rq
from bs4 import BeautifulSoup
from selenium import webdriver
import time
# 파서 차이
# # lxml        c언어 구현, c언어 의존적, xml처리 가능, html, body태그 구성
# html5lib      파이썬 구현, 파이썬 의존적 아님, 웹브라우저 형태, html,head,body
# html.parser   버전에 따라 실행 여부가 다름.(파이썬 2.7.2이하, 3.2.2 이하 버전에서만 사용 가능) 추천하지 않음 
# 속도 : lxml > html.parser > html5lib

html = """<html><head></head><p>test</p></html>"""

startTime = time.time()
soup = BeautifulSoup(html,'lxml')
endTime = time.time() - startTime


startTime2 = time.time()
soup2 = BeautifulSoup(html,'html5lib')
endTime2 = time.time() - startTime2


# driver = webdriver.Edge('msedgedriver.exe')

print(endTime)
print(endTime2)