from selenium.webdriver.common.by import By

from selenium_wework_main.pages.base_page import BasePage


class AddMember(BasePage):

    # send keys
    def add_member(self, member) -> bool:
        self.find(By.CSS_SELECTOR, '#username').send_keys(member['username'])
        self.find(By.ID, 'memberAdd_acctid').send_keys(member['acctid'])
        self.find(By.ID, 'memberAdd_phone').send_keys(member['phone'])
        # class 名有空格，需要通过以下方式定位，否则报错，无法找到元素
        # class 名有空格，可以只截取一半
        self.find(By.CSS_SELECTOR, "[class='qui_btn ww_btn js_btn_save']").click()
        return True

    def update_page(self) -> list:
        self.wait_for_click((By.CSS_SELECTOR, '.ww_checkbox'))
        content: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        return [int(x) for x in content.split('/', 1)]

    def get_member(self, value) -> bool:
        while True:
            cur_page, total_page = self.update_page()
            member_name_elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            for element in member_name_elements:
                if value == element.get_attribute('title'):
                    return True
            if cur_page == total_page:
                return False
            self.find(By.CSS_SELECTOR, '.js_next_page').click()
