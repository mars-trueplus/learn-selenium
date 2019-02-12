# -*- coding: utf-8 -*-


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchAttributeException, NoSuchElementException, StaleElementReferenceException


def get_driver():
    driver = webdriver.Firefox()
    return driver

def login(driver):
    driver.get('http://192.168.120.100/login')
    user = 'admin'
    password = 'goteam1@3'

    user_elm = WebDriverWait(driver, 60).until(lambda x: x.find_element_by_name('username'))
    password_elm = driver.find_element_by_name('password')

    user_elm.clear()
    user_elm.send_keys(user)
    password_elm.clear()
    password_elm.send_keys(password)

    list_button_elm = driver.find_elements_by_tag_name('button')
    for elm in list_button_elm:
        if 'submit' in elm.get_attribute('type'):
            elm.click()
            break


def check_loged_in(driver):
    try:
        loged_in_name = WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'oe_topbar_name')))
        print('login ngon')
        driver.refresh()
    except NoSuchElementException:
        print("Wrong username or password")


def upload_file(driver):
    driver.get('http://192.168.120.100/project/walter-general-oil-2019/wiki/demo-selenium')
    input_file_el = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#add-attach')))
    input_file_el.send_keys('/home/mars/Pictures/icon/filezilla.png')
    save_icon_el = WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tg-svg[svg-icon="icon-save"]')))
    save_icon_el.click()

if __name__ == '__main__':
    driver = get_driver()
    login(driver)
    upload_file(driver)
    # check_loged_in(driver)
    # time.sleep(10)
    driver.close()