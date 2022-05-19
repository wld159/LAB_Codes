"""
HW2_WebCrawling.py

임의의 프랜차이즈 카페의 매장 정보를 
웹 크롤링을 통해 추출하고 Excel 파일로 출력하는 프로그램을 작성하시오.

"""

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
import time
import platform

def get_pascucci_store(result):
    """
    This function will crawl inforamtion of each store
    """
    num_last_page = 53
    for page in range(1, num_last_page + 1):
        pascucci_URL = f"https://www.caffe-pascucci.co.kr/store/storeList.asp?page={page}"
        print(pascucci_URL)
        data = urllib.request.Request(pascucci_URL)
        html = urllib.request.urlopen(pascucci_URL).read()

        soupPascucci = BeautifulSoup(html, 'html.parser')
        tag_tbody = soupPascucci.find('tbody')
        
        for store in tag_tbody.find_all('tr'):
            if len(store) <= 3:
                break
            store_td = store.find_all('td')
            store_num = store_td[0].string
            store_name = store_td[1].string
            store_address = store_td[4].text.split('\n')[1]
            store_time = store_td[4].text.split('\n')[2]
            store_phone = store_td[5].text.split('\n')[1]
            result.append([store_num] + [store_name] + [store_address] + [store_time] + [store_phone])

    return 0

def main():
    result = []
    print("### Caffe Pascucci Store WebCrawling Initiated ###")
    get_pascucci_store(result)
    df_pascucci = pd.DataFrame(result, columns=['No.', 'Name', 'Address', 'Time', 'Phone'])
    df_pascucci.to_csv('pascucci.csv', encoding='cp949', mode='w', index=True)
    del result[:]

if __name__ == '__main__':
    main()