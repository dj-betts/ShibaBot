from selenium import webdriver
from time import sleep

class ShibaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get('https://instagram.com')
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\'username\']")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\'password\']")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
            .click()
        sleep(4)

        # end of bot because you can't post using the website.

ShibaBot('tails_of_two_shibas', 'pw')