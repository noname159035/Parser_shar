# -*- coding: utf-8 -*-
import os
import bs4
import sys
import time
import urllib.request
from bs4 import BeautifulSoup
import requests
import datetime
from datetime import datetime
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



def get_hihi(html, mas):
    soup = BeautifulSoup(html)
    data = soup.find_all("dl")
    for dl in data:
        qu = str(dl.find('dt')).replace('<dt>', '').replace('</b>', '').replace('</dt>', '').replace('<dd>', '').replace('<b>', '').replace('</dd>', '')
        ans = str(dl.find('dd')).replace('<dt>', '').replace('</b>', '').replace('</dt>', '').replace('<dd>', '').replace('<b>', '').replace('</dd>', '')
        mas.append([qu, ans])
    return mas


data_prev = [["1", "1"],["1", "1"],["1", "1"],["1", "1"],["1", "1"]]
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
while True:
    data = []
    file = open("shar.txt", "a", encoding='UTF-8')
    try:
        driver.get("https://randstuff.ru/ask/")
        elem = driver.find_element_by_xpath('//*[@id="ask-last"]/span')
        elem.click()
        wait = WebDriverWait(driver, 2)
        elem = wait.until(EC.visibility_of_element_located((By.ID, 'ask-dialog')))
        data = get_hihi(driver.page_source, data)
        # print(data)
        if not ((data[0] in data_prev) or (data[1] in data_prev) or (data[2] in data_prev) or (
                data[3] in data_prev) or (data[4] in data_prev)):
            data_prev = data
            for i in range(len(data)):
                file.write(data[i][0] + '\n')
                file.write(data[i][1] + '\n')
                file.write('\n')
            print(str(datetime.now().day) + '.' + str(datetime.now().month) + '.' + str(datetime.now().year), str(datetime.now().hour) + ":" + str(datetime.now().minute), "Добавлена запись")
            file.close()
        # driver.refresh()
    except TimeoutException or WebDriverException:
        pass



