import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from lxml import etree
import pandas as pd
import random


# taobao_sniper
def tb_sc(name, a, b, c):
    driver = webdriver.Edge()
    # name = "眼镜蛇腰带"
    url = "https://uland.taobao.com/sem/tbsearch?refpid=mm_26632360_8858797_29866178&keyword={" \
          "}&clk1=851812a4f2c6a6ee6b54de8c11e7ff56&upsId=851812a4f2c6a6ee6b54de8c11e7ff56".format(name)
    driver.get(url)
    time.sleep(3)
    driver.maximize_window()
    html_str = driver.page_source
    html_parse = etree.HTML(html_str)
    it = []
    for i in range(3):
        it.append({})
        try:
            it[i]['name'] = \
                driver.find_elements(By.XPATH, "//div[@class='pc-items-item-title pc-items-item-title-row2']/span")[
                    i].text
        except:
            it[i]['name'] = '/'
        try:
            it[i]['price'] = \
                driver.find_elements(By.XPATH, "//div[@class='price-con']/span[@class='coupon-price-afterCoupon']")[
                    i].text
        except:
            it[i]['price'] = '/'
        try:
            it[i]['brand'] = re.split('', driver.find_elements(By.XPATH, "//div[@class='seller-info']/div")[i].text)[1]
        except:
            it[i]['brand'] = '/'
        try:
            it[i]['volume'] = re.split("[+]", re.split("销", driver.find_elements(By.XPATH,
                                                                                  "//div[@class='item-footer']/div[@class='sell-info']")[
                i].text)[1])[0]
            try:
                idxOfWan = it[i]['volume'].find('万')
                if idxOfWan != -1:
                    it[i]['volume'] = re.split("万", it[i]['volume'])[0] + "0000"
            except:
                it[i]['volume'] = it[i]['volume']

        except:
            it[i]['volume'] = '/'
        it[i]['discuss'] = str(random.randint(1, 10) * 1000)
        it[i]['url'] = html_parse.xpath("//li[@class='pc-items-item item-undefined']/a/@href")[i]
        it[i]['good_discuss'] = "/"
        if it[i]['volume'] == '0':
            it[i]['score'] = round((float(it[i]['price']) * float(a) + float(b) + (float(it[i]['discuss']) / 1000) * float(c), 2))
        else:
            it[i]['score'] = round((float(it[i]['price']) * float(a) + (100 / float(it[i]['volume'])) * 0.01) * float(b) + (
                float(it[i]['discuss']) / 1000) * float(c), 2)
        it[i]['type'] = '淘宝/天猫商城'
        print(it)
        time.sleep(4)
    tb_data_f = pd.DataFrame(it)
    driver.quit()

    return tb_data_f
#
fin = tb_sc("五年高考三年模拟数学", 0.8,0.1,0.1)  # test
print(fin)
