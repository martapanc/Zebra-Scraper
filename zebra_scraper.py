#!/usr/bin/python3

import requests
import configparser

from selenium import webdriver

config = configparser.RawConfigParser()
config.read('config.properties')

USERNAME = config.get('Login', 'site.username');
PASSWORD = config.get('Login', 'site.password');
CHROMEDRIVER = config.get('Chromedriver', 'chromedriver.path');

LOGIN_URL = "https://www.zebrapower.co.uk/#/login"
URL = "https://www.zebrapower.co.uk/#/accountManagement"
LIVE_BALANCE_URL = config.get('Api', 'api.url');

driver = webdriver.Chrome(executable_path=CHROMEDRIVER)

def site_login():
    driver.get(LOGIN_URL)
    driver.find_element_by_id("loginemail").send_keys(USERNAME)
    driver.find_element_by_id ("loginpassword").send_keys(PASSWORD)
    driver.find_element_by_class_name("btn-primary").click()

site_login()

driver.get(URL)
driver.set_window_position(0, 0)
driver.set_window_size(100000, 200000)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# now print the response
# print(driver.page_source)

# print('/n')

headers = {
    "user-agent": "Mozilla/5.0", 
    "authorization": config.get('Api', 'api.auth')
}
r = requests.get(LIVE_BALANCE_URL, headers = headers).json()
print(r)

# import requests
# from lxml import html
# from lxml import etree



# LOGIN_URL = "https://www.zebrapower.co.uk/#/login"
# URL = "https://www.zebrapower.co.uk/#/accountManagement"

# def main():
#     session_requests = requests.session()

#     # Get login csrf token
#     result = session_requests.get(LOGIN_URL)

#     # print(result.text)
#     tree = html.fromstring(result.text)

#     # print(tree)

#     # doc = etree.parse(result.text)

#     # print(doc)
#     # authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

#     # Create payload
#     payload = {
#         "email": USERNAME, 
#         "password": PASSWORD
#     }

#     # Perform login
#     result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

#     print(result)
#     # Scrape url
#     result = session_requests.get(URL, headers = dict(referer = URL))
#     print(result)

#     tree = html.fromstring(result.content)
#     print(tree)
#     # bucket_names = tree.xpath("//div[@class='accountBalanceCard']/h2/text()")

#     # page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
#     # tree = html.fromstring(page.content)

#     bucket_names = tree.xpath("//div/text()")
    
#     print(bucket_names)

# if __name__ == '__main__':
#     main()