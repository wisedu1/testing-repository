from time import sleep
from selenium.webdriver.common.by import By

from selenium_wework_main.pages.base_page import BasePage


class AddMember(BasePage):

    # send keys
    def add_member(self):
        sleep(3)
        self.find(By.CSS_SELECTOR, '#username').send_keys('name2')
        self.find(By.ID, 'memberAdd_acctid').send_keys('account2')
        self.find(By.ID, 'memberAdd_phone').send_keys('11111111112')
        sleep(3)
        # class 名有空格，需要通过以下方式定位，否则报错，无法找到元素
        # class 名有空格，可以只截取一半
        self.find(By.CSS_SELECTOR, "[class='qui_btn ww_btn js_btn_save']").click()
        sleep(3)
        return True

    def get_member(self):
        member_name_elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        name_list = [member_name_element.get_attribute('title') for member_name_element in member_name_elements]

        return name_list
