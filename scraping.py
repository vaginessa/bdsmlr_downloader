import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os, time

class scraping:
    def __init__(self):
        options = uc.ChromeOptions()
        options.headless=True
        options.add_argument('--headless')
        self.drv = uc.Chrome(options=options)

    def login(self, email, pw):
        self.drv.get('https://bdsmlr.com/login')
        self.drv.find_element_by_name("email").send_keys(email)
        self.drv.find_element_by_name("password").send_keys(pw)
        self.drv.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/form/div[4]/div/button").click()
       
    def blog(self, maxPages, blog):
        self.drv.get(blog)
        time.sleep(1)
        # print(self.drv.find_element_by_tag_name('h1').get_attribute('innerText'))
        i = 1
        while(i <= maxPages):
            self.drv.find_element_by_tag_name('body').send_keys(Keys.CONTROL, Keys.END);
            time.sleep(1)
            i = i + 1
        source = self.drv.page_source
        self.drv.quit()
        return source





