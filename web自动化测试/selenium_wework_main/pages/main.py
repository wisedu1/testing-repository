from time import sleep
from selenium.webdriver.common.by import By
from selenium_wework_main.pages.add_member import AddMember
from selenium_wework_main.pages.base_page import BasePage


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_add_member(self):
        # common_entrance = self._driver.find_elements(By.CSS_SELECTOR, '.index_service_cnt_item_title')
        # 添加成员
        # common_entrance[0].click()
        self.find(By.ID, 'menu_contacts').click()
        sleep(3)
        self.finds(By.CSS_SELECTOR, "[class='qui_btn ww_btn js_add_member']")[1].click()
        return AddMember(self._driver)
