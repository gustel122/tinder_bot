from selenium import webdriver
import time

class TinderBot:

    def __init__(self):
        self.driver = webdriver.Chrome('/home/gustel122/tinder_bot/chromedriver_linux64/chromedriver')
        self.driver.maximize_window()

    def login(self):
        self.driver.get("https://tinder.com")

        time.sleep(5)


        fb_btn = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()

        popup = self.driver.window_handles[1]
        self.driver.switch_to_window(popup)

        fb_email = self.driver.find_element_by_xpath('//*[@id="email"]')
        fb_email.send_keys("justinmatthias66@gmail.com")

        fb_pwd = self.driver.find_element_by_xpath('//*[@id="pass"]')
        fb_pwd.send_keys("Nachhause15")

        fb_login = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        fb_login.click()

        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(base_window)

        time.sleep(5)

        popup1 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup1.click()

        popup2 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup2.click()

    def like(self):
        while (True):
            time.sleep(0.5)
            try:
                like = self.driver.find_element_by_xpath(
                    '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
                like.click()
            except Exception:
                self.close_popup()

    def dislike(self):
        pass

    def close_popup(self):
        popup_3 =self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

bot = TinderBot()
bot.login()
time.sleep(5)
bot.like()





