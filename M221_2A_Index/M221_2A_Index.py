

# ! -*- coding:utf-8 -*-
# 增加index部位的手数
import time
import re
import pymysql
import requests
from lxml import etree
import time
import datetime
from math import floor

from selenium import webdriver


# 2019.5.29 初步定的基金投资组合
# 　所有数据都已２０１９年５月２９日收盘时为准
# 广发证券	北方稀土	上海电力	上海电气	远兴能源　　上证指数


# 变换数据源，从东方财富网，换成网页财经

# 都假定做多

# 成本价
C6 = 13.16#广发证券
C8 =13.55 #　北方稀土
NOC6= 8.31  # 上海电力
NOC8=5.33# 上海电气
Arfa =2.83  # 远兴能源
#　投资组合收益，通过上面的５个股票附上权重之后计算所得　Profilo=
Index=2914.70   # 上证指数

# 一个收益率一个一个计算



def call_page(url):
    driver.get(url)
    html = driver.page_source
    return html

# 　选择依次请求５个股票和一个指数后再关闭浏览器




def parse_Index():
    url = 'http://quotes.money.163.com/0000001.html#1b01'
    html = call_page(url)
    selector = etree.HTML(html)
    Index_now = selector.xpath('/html/body/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[1]/span/strong/text()')
    Index_now_F = Index_now[0]
    items_float = float(Index_now_F)
    Index_PL = (items_float-Index)/Index  *100
    index_PL_2 = round(Index_PL, 2)
    index_PL_str = str(index_PL_2)
    big_list.append(index_PL_str)








def parse_C6():
    url = 'http://quotes.money.163.com/1000776.html#9b01'
    html = call_page(url)
    selector = etree.HTML(html)
    C6_now = selector.xpath('/html/body/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[1]/span/strong/text()')
    C6_now_F = C6_now[0]
    items_float = float(C6_now_F)
    C6_PL = (items_float-C6)/C6  *100
    C6_PL_006 = C6_PL  *0.06
    C6_PL_2 = round(C6_PL_006, 2)
    C6_PL_2_str = str(C6_PL_2)
    big_list.append(C6_PL_2_str)


def parse_C8():
    url = 'http://quotes.money.163.com/0600111.html#9b01'
    html = call_page(url)
    selector = etree.HTML(html)
    C8_now = selector.xpath('/html/body/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[1]/span/strong/text()')
    C8_now_F = C8_now[0]
    items_float = float(C8_now_F)
    C8_PL = (items_float-C8)/C8  *100
    C8_PL_008 = C8_PL *0.08
    C8_PL_2 = round(C8_PL_008, 2)
    C8_PL_2_str = str(C8_PL_2)
    big_list.append(C8_PL_2_str)



def parse_NOC8():
    url = 'http://quotes.money.163.com/0601727.html#9b01'
    html = call_page(url)
    selector = etree.HTML(html)
    NOC8_now = selector.xpath('/html/body/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[1]/span/strong/text()')
    NOC8_now_F = NOC8_now[0]
    items_float = float(NOC8_now_F)
    NOC8_PL = (items_float-NOC8)/NOC8  *100
    NOC8_PL_008 =  NOC8_PL *0.08
    NOC8_PL_2 = round(NOC8_PL_008, 2)
    NOC8_PL_2_str = str(NOC8_PL_2)
    big_list.append(NOC8_PL_2_str)


def parse_NOC6():
    url = 'http://quotes.money.163.com/0600021.html#9b01'
    html = call_page(url)
    selector = etree.HTML(html)
    NOC6_now = selector.xpath('/html/body/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[1]/span/strong/text()')
    NOC6_now_F = NOC6_now[0]
    items_float = float(NOC6_now_F)
    NOC6_PL = (items_float-NOC6)/NOC6  *100
    NOC6_PL_006 = NOC6_PL *0.06
    NOC6_PL_2 = round(NOC6_PL_006, 2)
    NOC6_PL_2_str = str(NOC6_PL_2)
    big_list.append(NOC6_PL_2_str)

def parse_Arfa():
    url = 'http://quotes.money.163.com/1000683.html#9b01'
    html = call_page(url)
    selector = etree.HTML(html)
    Arfa_now = selector.xpath('/html/body/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[1]/span/strong/text()')
    Arfa_now_F = Arfa_now[0]
    items_float = float(Arfa_now_F)
    Arfa_PL = (items_float-Arfa)/Arfa  *100
    Arfa_PL_02 = Arfa_PL *0.2
    Arfa_PL_2 = round(Arfa_PL_02, 2)
    Arfa_PL_2_str = str(Arfa_PL_2)
    big_list.append(Arfa_PL_2_str)








def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='FundsModels',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    try:
    # 这里是判断big_list的长度，不是content字符的长度
        cursor.executemany('insert into M221_2A_Index (Index_pl,c6_pl,c8_pl,noc8_pl,noc6_pl,arfa_pl,Portfolio_pl) values (%s,%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except :
        print('出列啦')



if __name__ == '__main__':

    while True:
        driver = webdriver.Chrome()

        big_list = []
        parse_Index()
        time.sleep(2)
        parse_C6()
        time.sleep(0.2)
        parse_C8()
        time.sleep(0.2)
        parse_NOC8()
        time.sleep(0.2)
        parse_NOC6()
        time.sleep(0.2)
        parse_Arfa()
        Portfolio = float(big_list[1]) + float(big_list[2]) + float(big_list[3]) + float(big_list[4]) + float(
            big_list[5])
        Portfolio_PL_2 = round(Portfolio, 2)
        big_list.append(str(Portfolio_PL_2)) # 这里专门将组合取２位小数

        driver.quit()

        l_tuple = tuple(big_list)
        content = []
        content.append(l_tuple)
        insertDB(content)
        print(datetime.datetime.now())

# 为了保证数据完整，１分钟的到一次数据

#
#  Index_pl,c6_pl,c8_pl,noc8_pl,noc6_pl,arfa_pl,Portfolio_pl


# create table M221_2A_Index(
# id int not null primary key auto_increment,
# Index_pl varchar(10),
# c6_pl varchar(10),
# c8_pl varchar(10),
# noc8_pl varchar(10),
# noc6_pl varchar(10),
# arfa_pl varchar(10),
# Portfolio_pl varchar(50)
# ) engine=InnoDB  charset=utf8;


# drop  table M221_2A_Index;

