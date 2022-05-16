"""
HW2_WebCrawling.py

임의의 프랜차이즈 카페의 매장 정보를 
웹 크롤링을 통해 추출하고 Excel 파일로 출력하는 프로그램을 작성하시오.

"""

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

from selenium import webdriver
import time

def starbucks_store():
    starbucks_URL = "https://www.starbucks.co.kr/store/store_map.do"
    wd = webdriver.Chrome('./WebDriver/chromedriver.exe')

    