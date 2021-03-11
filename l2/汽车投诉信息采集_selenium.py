import requests
import pandas as pd
# 使用selenium自动下载销量数据
from selenium import webdriver
import time
from pandas import DataFrame
import xlrd
from xlrd import xldate_as_tuple
import datetime
from bs4 import BeautifulSoup
import pandas as pd


def get_html(page_num):
    chrome_driver = r"C:\Users\Lenovo\anaconda3\Lib\site-packages\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver)
    request_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml'
    base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
    if page_num>1:
        request_url = base_url + str(i + 1) + '.shtml'
    driver.get(request_url)  # 打开网页
    time.sleep(1)  # 打开网页等一下，可能会网页延迟弹出
    html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
    return html


def parse_table(content):
    # 通过html字符串创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')

    tbody = soup.find('tbody')
    tr_list = tbody.find_all('tr')
    columns = []
    for tr in tr_list:
        th_list = tr.find_all('th')
        for th in th_list:
            columns.append(th.text)

    # 创建一个空表，只有表头
    df = pd.DataFrame(columns=columns)


    # 解析数据，添加到空表中
    tbody1 = soup.find('tbody')
    tr_list = tbody1.find_all('tr')
    # 遍历所有的行，添加到df中
    for tr in tr_list:
        td_list = tr.find_all('td')
        temp = {}
        columns_index = 0
        for td in td_list:
            temp[columns[columns_index]] = td.text
            columns_index += 1
        df = df.append(temp, ignore_index=True)
    return df


page_num=10

content = get_html(1)
df = parse_table(content)

for i in range(2,page_num+1):
    # 从代码中解析table
    content = get_html(i)
    df2 = parse_table(content)
    df=pd.concat([df,df2])
    print(df)
df.dropna(how='all',inplace=True)
df.to_excel('汽车投诉信息数据dm_selenium.xlsx', index=False)
