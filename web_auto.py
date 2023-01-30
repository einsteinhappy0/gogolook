from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    # user credential
    config = {'username':'', 'password': '', 'name': ''}
    # go to 104 webpage
    service = Service(executable_path=r"C:\Users\Albert\Desktop\selenium\chromedriver.exe")
    browser = webdriver.Chrome(service=service)
    browser.get('https://www.104.com.tw')
    assert '104' in browser.title
    # click to login
    loginelem = browser.find_element(By.CLASS_NAME, 'js-header_member-list_item-login-link_text')
    ActionChains(browser)\
        .click(loginelem)\
        .perform()
    # enter account and password, and submit
    browser.find_element(By.ID, 'username').send_keys(config['username'])
    browser.find_element(By.ID, 'password').send_keys(config['password'])
    submit =  browser.find_element(By.ID, 'submitBtn')
    ActionChains(browser).click(submit).perform()
    # wait util user page is ready 
    wait = WebDriverWait(browser, 20)
    logout = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[href*="logout"]')))
    # check for user name
    myname = browser.find_element(By.CSS_SELECTOR, '[class="h2 mb-3"]')
    assert config['name'] == myname.text
    # click logout button and quit
    ActionChains(browser).click(logout).perform()
    browser.quit()

if __name__ == '__main__':
    main()