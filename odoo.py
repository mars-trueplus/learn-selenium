# -*- coding: utf-8 -*-

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
    driver.get('http://192.168.120.100:8000')
    user = 'admin'
    password = 'goteam123@#'
    user_elm = driver.find_element_by_id('login')
    password_elm = driver.find_element_by_id('password')

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


if __name__ == '__main__':
    driver = get_driver()
    login(driver)
    check_loged_in(driver)
    driver.close()