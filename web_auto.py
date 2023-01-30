from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep

def main():
    config = {'username':'', 'password': '', 'name': ''}
    service = Service(executable_path=r"C:\Users\Albert\Desktop\selenium\chromedriver.exe")
    browser = webdriver.Chrome(service=service)
    browser.get('https://www.104.com.tw')
    assert '104' in browser.title

    loginelem = browser.find_element(By.CLASS_NAME, 'js-header_member-list_item-login-link_text')
    ActionChains(browser)\
        .click(loginelem)\
        .perform()

    browser.find_element(By.ID, 'username').send_keys(config['username'])
    browser.find_element(By.ID, 'password').send_keys(config['password'])
    submit =  browser.find_element(By.ID, 'submitBtn')
    ActionChains(browser)\
        .click(submit)\
        .perform()
    sleep(5)
    personinfo = browser.find_element(By.ID, 'introjs-1')
    assert config['name'] in personinfo
    browser.find_element(By.PARTIAL_LINK_TEXT, 'logout').click()
    browser.quit()

if __name__ == '__main__':
    main()